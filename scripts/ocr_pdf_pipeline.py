#!/usr/bin/env python3
"""
Segment a source PDF into PNGs and OCR each page via Cursor vision (3 passes + merge).

Requires:
  - pdftoppm (poppler)
  - Python venv: .venv-ocr/ with cursor-sdk, pyyaml
  - API key in ../tokens_ssto.yaml (CURSOR_API_KEY) — never commit that file

Usage (from repo root):
  bash scripts/ocr_pdf_pipeline.sh ScottMeasurement1964.pdf
  bash scripts/ocr_pdf_pipeline.sh ScottMeasurement1964.pdf --pages 1-3
  bash scripts/ocr_pdf_pipeline.sh ScottMeasurement1964.pdf --png-only
  bash scripts/ocr_pdf_pipeline.sh ScottMeasurement1964.pdf --merge-only
  bash scripts/ocr_pdf_pipeline.sh ScottMeasurement1964.pdf --status
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml
from cursor_sdk import Agent, AgentOptions, CursorAgentError, LocalAgentOptions, SDKImage, UserMessage

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT.parent / "tokens_ssto.yaml"
PAGES_ROOT = ROOT / "sources" / "pages"
SOURCES = ROOT / "sources"

# Three prompt variants (approximate "different seeds" — vary instruction, not RNG).
PASS_PROMPTS = [
    """Transcription pass A (literal): Transcribe this page exactly as printed.
Output Markdown only. Reflow broken lines into sentences/paragraphs.
Use LaTeX for math: $\\varphi$, $\\succsim$, $\\sum_{i<n}$, $\\mu$, etc.
Do not include standalone printed page numbers. Do not add commentary.""",
    """Transcription pass B (math-first): Transcribe this page; prioritize correct
mathematical notation as LaTeX (inline $...$ or display $$...$$).
Prose as normal paragraphs. Reflow line breaks. Markdown only.""",
    """Transcription pass C (conservative): Transcribe this page; mark any character
you are not confident about as [?x]. Use LaTeX for math symbols.
Reflow paragraphs. Markdown only.""",
]

MERGE_PROMPT = """You are reconciling three independent OCR transcriptions of the same
PDF page (image attached). Each pass may differ on OCR glitches.

Pass 1:
---
{pass1}
---

Pass 2:
---
{pass2}
---

Pass 3:
---
{pass3}
---

Produce ONE final Markdown transcription:
- Where all three agree, use that text.
- Where they disagree, use the image to decide; if still uncertain, use [?…].
- Proper LaTeX for all mathematics.
- Reflowed prose paragraphs; preserve section headings and numbered statements.
- Omit standalone printed page numbers (e.g. lines that are only "233" or "234").
- Output ONLY the final page content (no meta-commentary)."""

DEFAULT_RETRIES = 5
DEFAULT_RETRY_BASE_SEC = 15.0
DEFAULT_MODEL = "composer-2.5"

# J. Math. Psychology 1 (1964) pagination: pages 233-247.
JOURNAL_PAGE = re.compile(r"^\s*(23[3-9]|24[0-7])\s*$")


@dataclass
class PageJob:
    pdf_stem: str
    page_num: int
    png_path: Path
    work_dir: Path

    def log_label(self) -> str:
        return f"{self.pdf_stem} page {self.page_num}"


def load_api_key() -> str:
    if not TOKENS.exists():
        raise SystemExit(f"Missing API key file: {TOKENS}")
    data = yaml.safe_load(TOKENS.read_text())
    key = (data.get("CURSOR_API_KEY") or data.get("cursor_api_key") or "").strip()
    if not key:
        raise SystemExit(f"No CURSOR_API_KEY in {TOKENS}")
    return key


def resolve_pdf(arg: Path) -> Path:
    """Find PDF by absolute path, CWD-relative path, repo root, or sources/."""
    if arg.is_absolute():
        if arg.exists():
            return arg.resolve()
        raise SystemExit(f"PDF not found: {arg}")
    candidates = [
        Path.cwd() / arg,
        ROOT / arg,
        SOURCES / arg,
        SOURCES / arg.name,
        ROOT / arg.name,
    ]
    for c in candidates:
        if c.exists():
            return c.resolve()
    raise SystemExit(
        f"PDF not found: {arg}\n"
        f"Tried: {', '.join(str(c) for c in candidates)}"
    )


def pdf_page_count(pdf: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":")[1].strip())
    raise RuntimeError(f"Could not read page count: {pdf}")


def log(msg: str, log_path: Path | None) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] {msg}"
    if log_path:
        with log_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
        print(line, file=sys.stderr)
    else:
        print(line, file=sys.stderr)


def render_pdf_to_png(pdf: Path, out_dir: Path, dpi: int = 200, skip_if_exists: bool = False) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(out_dir.glob("page-*.png"))
    if skip_if_exists and existing:
        return existing
    prefix = out_dir / "page"
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(prefix)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    pngs = sorted(out_dir.glob("page-*.png"))
    if not pngs:
        raise RuntimeError(f"No PNGs produced in {out_dir}")
    return pngs


def page_work_dir(png_dir: Path, page_num: int) -> Path:
    return png_dir / f"page-{page_num:02d}"


def page_png_path(png_dir: Path, page_num: int) -> Path | None:
    """Resolve PNG from pdftoppm (padding width varies with total page count)."""
    for name in (
        f"page-{page_num}.png",
        f"page-{page_num:02d}.png",
        f"page-{page_num:03d}.png",
        f"page-{page_num:04d}.png",
    ):
        p = png_dir / name
        if p.exists():
            return p
    return None


def parse_page_range(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(1, total + 1))
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            pages.update(range(int(a), int(b) + 1))
        else:
            pages.add(int(part))
    return sorted(p for p in pages if 1 <= p <= total)


def vision_prompt_once(api_key: str, png: Path, text: str, model: str) -> str:
    result = Agent.prompt(
        UserMessage(text=text, images=[SDKImage.from_file(png)]),
        AgentOptions(
            api_key=api_key,
            model=model,
            local=LocalAgentOptions(cwd=str(ROOT)),
        ),
    )
    if result.status != "finished":
        detail = getattr(result, "result", None) or getattr(result, "error", None) or ""
        raise RuntimeError(f"status={result.status} {detail}".strip())
    body = (result.result or "").strip()
    body = re.sub(r"^```(?:markdown|md)?\s*\n", "", body)
    body = re.sub(r"\n```\s*$", "", body)
    return body.strip() + "\n"


def vision_prompt(
    api_key: str,
    png: Path,
    text: str,
    *,
    model: str,
    retries: int,
    retry_base_sec: float,
    log_path: Path | None,
    label: str,
) -> str:
    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            t0 = time.monotonic()
            out = vision_prompt_once(api_key, png, text, model)
            elapsed = time.monotonic() - t0
            log(f"{label} ok ({elapsed:.1f}s)", log_path)
            return out
        except CursorAgentError as err:
            last_err = err
            wait = retry_base_sec * (2 ** (attempt - 1))
            log(
                f"{label} startup error attempt {attempt}/{retries}: {err.message} "
                f"(retryable={err.is_retryable}, wait {wait:.0f}s)",
                log_path,
            )
            if attempt == retries or not err.is_retryable:
                raise
            time.sleep(wait)
        except RuntimeError as err:
            last_err = err
            wait = retry_base_sec * (2 ** (attempt - 1))
            log(f"{label} run error attempt {attempt}/{retries}: {err} (wait {wait:.0f}s)", log_path)
            if attempt == retries:
                raise
            time.sleep(wait)
    raise RuntimeError(f"{label} failed after {retries} attempts: {last_err}")


def ocr_page_triple(
    api_key: str,
    job: PageJob,
    force: bool,
    *,
    model: str,
    retries: int,
    retry_base_sec: float,
    log_path: Path | None,
) -> None:
    merged = job.work_dir / "merged.md"
    tag = job.log_label()
    if merged.exists() and not force:
        log(f"{tag}: skipped (merged.md exists)", log_path)
        return

    job.work_dir.mkdir(parents=True, exist_ok=True)
    passes: list[str] = []
    for i, prompt in enumerate(PASS_PROMPTS, start=1):
        out = job.work_dir / f"pass{i}.md"
        if out.exists() and not force:
            log(f"{tag} pass{i}: cached", log_path)
            passes.append(out.read_text(encoding="utf-8"))
            continue
        log(f"{tag} pass{i}: OCR...", log_path)
        text = vision_prompt(
            api_key,
            job.png_path,
            prompt,
            model=model,
            retries=retries,
            retry_base_sec=retry_base_sec,
            log_path=log_path,
            label=f"{tag} pass{i}",
        )
        out.write_text(text, encoding="utf-8")
        passes.append(text)
        time.sleep(2)

    log(f"{tag} merge: reconciling 3 passes...", log_path)
    merge_text = MERGE_PROMPT.format(pass1=passes[0], pass2=passes[1], pass3=passes[2])
    final = vision_prompt(
        api_key,
        job.png_path,
        merge_text,
        model=model,
        retries=retries,
        retry_base_sec=retry_base_sec,
        log_path=log_path,
        label=f"{tag} merge",
    )
    merged.write_text(final, encoding="utf-8")
    log(f"{tag}: done", log_path)


def strip_book_page_numbers(text: str) -> str:
    """Remove printed journal page numbers accidentally transcribed as standalone lines."""
    return "\n".join(
        line for line in text.splitlines() if not JOURNAL_PAGE.match(line)
    ).strip() + "\n"


def collect_page_status(png_dir: Path, total: int) -> tuple[list[int], list[int], list[int]]:
    """Return (completed, partial, pending) page numbers in 1..total."""
    completed: list[int] = []
    partial: list[int] = []
    pending: list[int] = []
    for n in range(1, total + 1):
        work_dir = page_work_dir(png_dir, n)
        merged = work_dir / "merged.md"
        if merged.exists():
            completed.append(n)
            continue
        passes = [work_dir / f"pass{i}.md" for i in range(1, len(PASS_PROMPTS) + 1)]
        if any(p.exists() for p in passes):
            partial.append(n)
        else:
            pending.append(n)
    return completed, partial, pending


def log_resume_summary(
    pdf_stem: str,
    total: int,
    page_nums: list[int],
    png_dir: Path,
    out_md: Path,
    log_path: Path | None,
) -> tuple[list[int], list[int], list[int]]:
    completed, partial, pending = collect_page_status(png_dir, total)
    in_range = set(page_nums)
    completed_run = [n for n in completed if n in in_range]
    partial_run = [n for n in partial if n in in_range]
    pending_run = [n for n in pending if n in in_range]
    log(
        f"resume {pdf_stem}: {len(completed)} complete, {len(partial)} partial, "
        f"{len(pending)} not started (of {total} pages)",
        log_path,
    )
    if completed:
        log(f"  complete (skip OCR): {completed}", log_path)
    if partial:
        log(f"  partial (reuse cached passes): {partial}", log_path)
    if completed_run:
        log(f"  this run will skip OCR: {completed_run}", log_path)
    if partial_run:
        log(f"  this run will finish partial: {partial_run}", log_path)
    if pending_run:
        preview = pending_run[:20]
        suffix = "..." if len(pending_run) > 20 else ""
        log(f"  this run still needs OCR: {preview}{suffix}", log_path)
    if out_md.exists():
        log(f"  output exists: {out_md}", log_path)
    else:
        log(f"  output will be rebuilt: {out_md}", log_path)
    return completed, partial, pending


def list_completed_pages(pdf_stem: str) -> list[int]:
    png_dir = PAGES_ROOT / pdf_stem
    completed: list[int] = []
    for d in sorted(png_dir.glob("page-*")):
        if not d.is_dir():
            continue
        m = re.match(r"page-(\d+)$", d.name)
        if m and (d / "merged.md").exists():
            completed.append(int(m.group(1)))
    return sorted(completed)


def contiguous_prefix_from(completed: set[int], start: int) -> list[int]:
    """`start, start+1, …` while each page is completed — no gaps, no later pages."""
    pages: list[int] = []
    n = start
    while n in completed:
        pages.append(n)
        n += 1
    return pages


def stitch_document(
    pdf_stem: str,
    page_nums: list[int] | None,
    out_md: Path,
    *,
    log_path: Path | None = None,
    reason: str = "",
) -> int:
    """Full rewrite of `out_md` from per-page `merged.md` (never append).

    Only includes a **contiguous run** from the run's first page: if pages 1 and 2 are
    done but 3–7 are not, page 8 (e.g. from an old smoke test) is withheld until the gap
    is filled. `--merge-only` without `--pages` starts from page 1.
    """
    available = set(list_completed_pages(pdf_stem))
    if page_nums is not None:
        start = min(page_nums)
        in_scope = available & set(page_nums)
    else:
        start = 1
        in_scope = available
    stitch_pages = contiguous_prefix_from(in_scope, start)
    withheld = sorted(in_scope - set(stitch_pages))
    if withheld:
        log(
            f"stitch withheld {len(withheld)} completed page(s) out of order: {withheld}",
            log_path,
        )
    meta = f"""---
source_pdf: {pdf_stem}.pdf
ocr_method: cursor-vision-triple-merge
verification_status: draft
---

# Transcription (LLM vision OCR)

"""
    parts = [meta]
    for n in stitch_pages:
        merged = PAGES_ROOT / pdf_stem / f"page-{n:02d}" / "merged.md"
        if not merged.exists():
            print(f"WARN: missing {merged}", file=sys.stderr)
            continue
        parts.append(f"\n<!-- page {n} -->\n\n")
        parts.append(strip_book_page_numbers(merged.read_text(encoding="utf-8")))
        if not parts[-1].endswith("\n"):
            parts.append("\n")
    out_md.write_text("".join(parts), encoding="utf-8")
    label = f" ({reason})" if reason else ""
    if stitch_pages:
        msg = f"{pdf_stem}: re-stitched {out_md.name}: {len(stitch_pages)} page(s){label}"
        print(msg.replace("re-stitched", "Stitched"), file=sys.stderr)
    else:
        msg = f"{pdf_stem}: re-stitched {out_md.name}: header only (no merged.md in range){label}"
        print(f"WARN: {pdf_stem}: no merged.md to stitch; wrote header only", file=sys.stderr)
    log(msg, log_path)
    return len(stitch_pages)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "pdf",
        type=Path,
        nargs="?",
        default=Path("ScottMeasurement1964.pdf"),
        help="PDF name or path (default: ScottMeasurement1964.pdf under sources/)",
    )
    ap.add_argument("--pages", help="Page range, e.g. 1-5 or 1,3,7")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--png-only", action="store_true")
    ap.add_argument("--merge-only", action="store_true", help="Skip OCR; stitch existing merged.md")
    ap.add_argument(
        "--status",
        action="store_true",
        help="Show resume state (completed / partial / pending) and exit",
    )
    ap.add_argument("--force", action="store_true", help="Re-OCR even if pass*.md exist")
    ap.add_argument(
        "--skip-render",
        action="store_true",
        help="Skip pdftoppm when page-*.png already exist",
    )
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"Vision model (default: {DEFAULT_MODEL})")
    ap.add_argument("--retries", type=int, default=DEFAULT_RETRIES)
    ap.add_argument("--retry-base-sec", type=float, default=DEFAULT_RETRY_BASE_SEC)
    ap.add_argument(
        "--log",
        type=Path,
        help="Append timestamped progress to this log file",
    )
    ap.add_argument(
        "--out",
        type=Path,
        help="Output stitched MD (default: sources/<stem>_vision.md)",
    )
    args = ap.parse_args()

    pdf = resolve_pdf(args.pdf)

    stem = pdf.stem
    png_dir = PAGES_ROOT / stem
    out_md = args.out or (SOURCES / f"{stem}_vision.md")
    if not out_md.is_absolute():
        out_md = ROOT / out_md
    log_path = args.log or (SOURCES / f"ocr_{stem}_run.log")
    if not log_path.is_absolute():
        log_path = ROOT / log_path

    total = pdf_page_count(pdf)
    page_nums = parse_page_range(args.pages, total)

    # Always identify the paper first — essential when several PDFs run in parallel.
    paper_banner = f"paper: {stem} ({pdf.name})"
    if args.status or args.merge_only:
        log(paper_banner, None)
    else:
        log(paper_banner, log_path)

    if args.status:
        log_resume_summary(stem, total, page_nums, png_dir, out_md, None)
        completed = list_completed_pages(stem)
        if completed:
            print(
                f"To rebuild {out_md} from {len(completed)} completed page(s), run:\n"
                f"  bash scripts/ocr_pdf_pipeline.sh {pdf.name} --merge-only",
                file=sys.stderr,
            )
        return

    if args.merge_only:
        stitch_document(stem, None, out_md, log_path=log_path, reason="merge-only")
        return

    log_resume_summary(stem, total, page_nums, png_dir, out_md, log_path)
    stitch_document(stem, page_nums, out_md, log_path=log_path, reason="restart")

    log(f"start {pdf.name} pages={page_nums} model={args.model}", log_path)
    pngs = render_pdf_to_png(pdf, png_dir, dpi=args.dpi, skip_if_exists=args.skip_render)
    if len(pngs) != total:
        log(f"WARN: expected {total} PNGs, got {len(pngs)}", log_path)

    if args.png_only:
        log(f"PNG-only: {len(pngs)} files in {png_dir}", log_path)
        return

    api_key = load_api_key()
    for n in page_nums:
        png = page_png_path(png_dir, n)
        if png is None:
            log(f"SKIP missing PNG for {stem} page {n} in {png_dir}", log_path)
            continue
        log(f"{stem} page {n}/{total} ({png.name})...", log_path)
        job = PageJob(stem, n, png, page_work_dir(png_dir, n))
        try:
            ocr_page_triple(
                api_key,
                job,
                force=args.force,
                model=args.model,
                retries=args.retries,
                retry_base_sec=args.retry_base_sec,
                log_path=log_path,
            )
        except Exception as err:
            log(f"FATAL {stem} page {n}: {err}", log_path)
            stitch_document(stem, page_nums, out_md, log_path=log_path, reason=f"after error on page {n}")
            raise
        stitch_document(stem, page_nums, out_md, log_path=log_path, reason=f"after page {n}")

    stitch_document(stem, page_nums, out_md, log_path=log_path, reason="finished")


if __name__ == "__main__":
    main()
