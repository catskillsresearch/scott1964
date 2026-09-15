#!/usr/bin/env python3
r"""Convert arxiv_with_code.md to a CMU SCS technical report (arXiv-ready).

Pipeline:
  1. Drop the GitHub-only navigation preamble (auto-gen note, document map, file index).
  2. Lift the `## Abstract` section into a LaTeX \begin{abstract}.
  3. Demote the Appendix-A structural headings so LaTeX numbers everything once, then
     insert \\appendix before the combined Lean-source appendix.
  4. Strip manual section numbers (any depth, e.g. `1.`, `1.3`, `5.1`) so LaTeX does
     the numbering and we never get duplicates like "5.1 5.1".
  5. Replace fenced code with \\lstinputlisting blocks (ASCII-sanitized for arXiv pdfLaTeX).
  5b. Render ```mermaid blocks to PNG via mermaid-cli (mmdc) for arXiv pdfLaTeX.
  6. Inject AI model-card acknowledgements from `scripts/ai_model_cards.py` (before HTML-comment strip).
  7. pandoc → LaTeX, then splice the listing/math/figure placeholders back in.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from ai_model_cards import inject_model_cards
from lean_listing_sanitize import chunk_line_ranges, sanitize_lean_for_arxiv

SRC = ROOT / "arxiv_with_code.md"
OUT = ROOT / "arxiv.tex"
PREAMBLE = SCRIPTS / "tex_preamble_arxiv.tex"
LISTINGS_DIR = ROOT / "lean-listings"
FIGURES_DIR = ROOT / "figures"
PUPPETEER_CONFIG = SCRIPTS / "puppeteer-config.json"
LISTING_CHUNK_LINES = 400

GITHUB_URL = r"https://github.com/catskillsresearch/scott1964"
REPORT_NUMBER = "CMU-CS-26-XXX"
REPORT_DATE = "September 2026"
ERICSON_EMAIL = "lars.ericson@catskillsresearch.com"


def find_chrome() -> str | None:
    env = os.environ.get("PUPPETEER_EXECUTABLE_PATH")
    if env and Path(env).exists():
        return env
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    return None


def render_mermaid(code: str, idx: int) -> str:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    mmd_path = FIGURES_DIR / f"figure-{idx:03d}.mmd"
    png_path = FIGURES_DIR / f"figure-{idx:03d}.png"
    mmd_path.write_text(code.strip() + "\n", encoding="utf-8")

    mmdc = shutil.which("mmdc")
    if not mmdc:
        raise RuntimeError(
            "mermaid-cli (mmdc) not found; install with "
            "`npm install -g @mermaid-js/mermaid-cli`"
        )
    env = os.environ.copy()
    chrome = find_chrome()
    if chrome:
        env["PUPPETEER_EXECUTABLE_PATH"] = chrome
    cmd = [mmdc, "-i", str(mmd_path), "-o", str(png_path), "-b", "white"]
    if PUPPETEER_CONFIG.is_file():
        cmd += ["-p", str(PUPPETEER_CONFIG)]
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True, check=False)
    if proc.returncode != 0 or not png_path.is_file():
        sys.stderr.write(proc.stdout + "\n" + proc.stderr + "\n")
        raise RuntimeError(f"mmdc failed to render figure {idx}")
    return png_path.relative_to(ROOT).as_posix()


def extract_title() -> str:
    first = (ROOT / "arxiv.md").read_text(encoding="utf-8").splitlines()[0]
    title = first[2:].strip() if first.startswith("# ") else first.strip()
    title = re.sub(r"\*([^*]+)\*", r"\\emph{\1}", title)
    return title


TITLE = extract_title()

GITHUB_INLINE_MATH = re.compile(r"\$`([^`\n]+?)`\$")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
FENCE_RE = re.compile(r"^```([^\n]*)\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
MANUAL_SECTION_NUM = re.compile(r"^(#{1,6})[ \t]+\d+(?:\.\d+)*\.?[ \t]+", re.MULTILINE)
NARRATIVE_MARKER = "# Narrative (from arxiv.md)"
LEAN_MODULE_RE = re.compile(r"^###\s+(Scott1964(?:\.lean|/[^\s{]+))\s*$", re.MULTILINE)
FIGURE_CAPTION_RE = re.compile(
    r"<!--\s*figure-caption:\s*(.*?)\s*-->\s*\n```mermaid",
    re.IGNORECASE | re.DOTALL,
)


def github_math_to_tex(text: str) -> str:
    return GITHUB_INLINE_MATH.sub(r"$\1$", text)


def strip_html_comments(text: str) -> str:
    return HTML_COMMENT.sub("", text)


def strip_manual_section_numbers(text: str) -> str:
    return MANUAL_SECTION_NUM.sub(r"\1 ", text)


def drop_github_nav(text: str) -> str:
    idx = text.find(NARRATIVE_MARKER)
    if idx == -1:
        return text
    return text[idx + len(NARRATIVE_MARKER) :].lstrip("\n")


def normalize_appendix_headings(text: str) -> str:
    text = re.sub(
        r"^#\s+Appendix A: (?:Complete Lean source|Lean module index)\s*$",
        "## Lean module index",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^##\s+`(Scott1964(?:\.lean|/[^`]+))`\s*$",
        r"### \1",
        text,
        flags=re.MULTILINE,
    )
    return text


def extract_abstract(text: str) -> tuple[str, str]:
    m = re.search(r"^##\s+Abstract\s*\n(.*?)(?=^##\s)", text, re.DOTALL | re.MULTILINE)
    if not m:
        return "", text
    abstract_md = m.group(1).strip()
    body = text[: m.start()] + text[m.end() :]
    return abstract_md, body


def write_listing(code: str, listing_name: str) -> tuple[str, int]:
    LISTINGS_DIR.mkdir(parents=True, exist_ok=True)
    source = sanitize_lean_for_arxiv(code.rstrip("\n"))
    listing_path = LISTINGS_DIR / listing_name
    listing_path.write_text(source + "\n", encoding="utf-8")
    rel_path = listing_path.relative_to(ROOT).as_posix()
    return rel_path, (len(source.splitlines()) if source else 0)


def lean_block_latex(code: str, listing_name: str) -> str:
    rel_path, line_count = write_listing(code, listing_name)
    ranges = chunk_line_ranges(line_count, LISTING_CHUNK_LINES)

    parts: list[str] = []
    for first, last in ranges:
        if first == 1 and last == line_count:
            parts.append(
                "\\vspace{0.5\\baselineskip}\n"
                "\\noindent\\textcolor{green!40!black}{\\textbf{Lean 4 source}}"
                "\\par\\vspace{0.25\\baselineskip}\n"
                f"\\lstinputlisting[style=leanbox]{{{rel_path}}}\n"
                "\\vspace{0.5\\baselineskip}\n\n"
            )
        else:
            parts.append(
                f"\\noindent\\textcolor{{green!40!black}}{{\\textbf{{Lean 4 source "
                f"(lines {first}--{last})}}}}\\par\\vspace{{0.25\\baselineskip}}\n"
                f"\\lstinputlisting[style=leanbox,firstline={first},lastline={last}]"
                f"{{{rel_path}}}\n\n"
            )
    return "".join(parts)


def parse_figure_captions(text: str) -> list[str]:
    return [m.group(1).strip() for m in FIGURE_CAPTION_RE.finditer(text)]


def escape_latex_caption(text: str) -> str:
    out: list[str] = []
    for ch in text:
        if ch in "&%$#_{}":
            out.append(f"\\{ch}" if ch != "}" else "\\}")
        elif ch == "~":
            out.append(r"\textasciitilde{}")
        elif ch == "^":
            out.append(r"\textasciicircum{}")
        elif ch == "\\":
            out.append(r"\textbackslash{}")
        else:
            out.append(ch)
    return "".join(out)


def extract_lean_titles(text: str) -> dict[str, str]:
    titles: dict[str, str] = {}
    lean_starts = [m.start() for m in re.finditer(r"^```lean\s*$", text, re.MULTILINE)]
    for idx, pos in enumerate(lean_starts):
        prefix = text[:pos].rstrip("\n")
        module = None
        for line in reversed(prefix.splitlines()[-4:]):
            m = re.match(r"^###\s+(Scott1964(?:\.lean|/[^\s{]+))", line.strip())
            if m:
                module = m.group(1)
                break
        titles[f"LEANINCLUDE{idx:03d}"] = module or f"module-{idx + 1}"
    return titles


def replace_fences(text: str, figure_captions: list[str]) -> tuple[str, dict[str, str]]:
    lean_titles = extract_lean_titles(text)
    placeholders: dict[str, str] = {}
    lean_idx = 0
    other_idx = 0
    figure_idx = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal lean_idx, other_idx, figure_idx
        lang = match.group(1).strip().lower()
        body = match.group(2)
        if lang == "lean":
            key = f"LEANINCLUDE{lean_idx:03d}"
            module = lean_titles.get(key, f"module-{lean_idx}")
            lean_idx += 1
            safe_name = module.replace("/", "-")
            if not safe_name.endswith(".lean"):
                safe_name += ".lean"
            placeholders[key] = lean_block_latex(body, safe_name)
            return f"\n\n{key}\n\n"
        if lang == "math":
            key = f"MATHINCLUDE{other_idx:03d}"
            other_idx += 1
            placeholders[key] = f"\\[\n{body.strip()}\n\\]\n"
            return f"\n\n{key}\n\n"
        if lang == "mermaid":
            key = f"FIGINCLUDE{other_idx:03d}"
            rel_path = render_mermaid(body, figure_idx)
            if figure_idx < len(figure_captions):
                caption = figure_captions[figure_idx]
            else:
                caption = f"Dependency diagram {figure_idx + 1}."
            label = f"fig:scott1964-{figure_idx + 1:02d}"
            figure_idx += 1
            other_idx += 1
            cap = escape_latex_caption(caption)
            placeholders[key] = (
                "\\begin{figure}[htbp]\n\\centering\n"
                f"\\includegraphics[max width=\\linewidth,"
                f"max totalheight=0.85\\textheight,keepaspectratio]{{{rel_path}}}\n"
                f"\\caption{{{cap}}}\n"
                f"\\label{{{label}}}\n"
                "\\end{figure}\n"
            )
            return f"\n\n{key}\n\n"
        key = f"CODEINCLUDE{other_idx:03d}"
        rel_path, _ = write_listing(body, f"snippet-{other_idx:03d}.txt")
        other_idx += 1
        placeholders[key] = f"\\lstinputlisting[style=leanbox]{{{rel_path}}}\n"
        return f"\n\n{key}\n\n"

    converted = FENCE_RE.sub(repl, text)
    return converted, placeholders


def pandoc_to_latex(markdown: str, shift: bool = True) -> str:
    cmd = [
        "pandoc",
        "-f",
        "markdown+tex_math_dollars+raw_tex+smart",
        "-t",
        "latex",
        "--wrap=none",
    ]
    if shift:
        cmd += ["--shift-heading-level-by=-1"]
    proc = subprocess.run(cmd, input=markdown, text=True, capture_output=True, check=False)
    if proc.returncode != 0:
        print(proc.stderr, file=sys.stderr)
        raise RuntimeError("pandoc failed")
    return proc.stdout


def inject_placeholders(latex: str, placeholders: dict[str, str]) -> str:
    out = latex
    for key, value in placeholders.items():
        patterns = [
            key,
            f"\\emph{{{key}}}",
            f"\\text{{{key}}}",
            f"\\passthrough{{\\lstinline!{key}!}}",
        ]
        for pat in patterns:
            if pat in out:
                out = out.replace(pat, value)
                break
        else:
            out = out.replace(key, value)
    return out


def break_texttt_paths(latex: str) -> str:
    """Allow line breaks after `/` and `_` in \\texttt paths and identifiers."""

    def fix(match: re.Match[str]) -> str:
        inner = match.group(1)
        inner = inner.replace("/", "/\\allowbreak{}")
        inner = inner.replace(r"\_", r"\_\allowbreak{}")
        inner = re.sub(r"(?<=[a-z])(?=[A-Z])", r"\\allowbreak{}", inner)
        inner = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", r"\\allowbreak{}", inner)
        inner = inner.replace(".lean", ".\\allowbreak{}lean")
        inner = re.sub(r"\.(?=[A-Za-z])", r".\\allowbreak{}", inner)
        return "\\texttt{" + inner + "}"

    return re.sub(r"\\texttt\{([^{}]*)\}", fix, latex)


def cleanup_pandoc_latex(latex: str) -> str:
    latex = latex.replace("\\pandocbounded{", "{")
    latex = re.sub(r"\\tightlist\n", "", latex)
    latex = break_texttt_paths(latex)
    for cmd in ("section", "subsection", "subsubsection", "paragraph"):
        latex = re.sub(
            rf"(\\{cmd}\{{)\d+(?:\.\d+)*\.?\s+",
            r"\1",
            latex,
        )
    latex = re.sub(
        r"\\section\{Appendix A\. Lean source index\}",
        "",
        latex,
    )
    latex = re.sub(
        r"\\section\{Appendix A: (?:Complete Lean source|Lean module index)\}",
        r"\\section{Lean module index}",
        latex,
    )
    latex = re.sub(
        r"\\section\{Appendix A\. Lean module index\}",
        r"\\section{Lean module index}",
        latex,
    )
    latex = re.sub(r"\n{3,}", "\n\n", latex)
    return latex


def insert_list_of_figures(latex: str) -> str:
    """Insert \\listoffigures immediately before the References section."""
    anchor = r"\hypertarget{references}{%"
    if anchor not in latex:
        anchor = r"\section{References}"
    if anchor not in latex:
        print("warning: missing References anchor; skipping \\listoffigures", file=sys.stderr)
        return latex
    block = "\\clearpage\n\\listoffigures\n\\clearpage\n\n"
    return latex.replace(anchor, block + anchor, 1)


def insert_appendix_command(latex: str) -> str:
    marker = r"\section{Lean module index}"
    if marker not in latex:
        raise RuntimeError(f"missing {marker!r} in LaTeX output")
    return latex.replace(marker, r"\appendix" + "\n" + marker, 1)


def cleanup_abstract_latex(latex: str) -> str:
    """Keep the abstract pdfLaTeX/arXiv-safe: ASCII plus standard LaTeX escapes."""
    latex = latex.replace("\\pandocbounded{", "{")
    latex = latex.replace("\\textbf{{[}", "\\textbf{[")
    latex = latex.replace("\\texttt{{[}", "\\texttt{[")
    latex = latex.replace("{]}}", "]}")
    latex = re.sub(r"\\begin\{center\}\\rule\{.*?\}\\end\{center\}\s*", "", latex, flags=re.DOTALL)
    return latex


def build_title_page(abstract_latex: str) -> str:
    ericson_email_latex = rf"\texttt{{{ERICSON_EMAIL}}}"
    github_latex = rf"\url{{{GITHUB_URL}}}"
    return textwrap.dedent(
        f"""
        \\title{{{TITLE}}}

        \\author{{
          Lars Warren Ericson \\\\
          {{\\normalfont\\small Independent researcher, d/b/a Catskills Research Company}} \\\\
          {{\\normalfont\\small {ericson_email_latex}}} \\\\[1.5ex]
          Dana S. Scott \\\\
          {{\\normalfont\\small Computer Science Department, Carnegie Mellon University, Emeritus}}
        }}

        \\date{{{REPORT_DATE}}}
        \\trnumber{{{REPORT_NUMBER}}}
        \\keywords{{Lean 4; formal verification; measurement theory; linear inequalities;
          cancellation conditions; utility theory; subjective probability}}
        \\citationinfo{{This report will be cross-archived on arXiv in
          \\texttt{{cs.LO}} and \\texttt{{math.LO}}.\\\\
          Source repository: {github_latex}}}
        \\copyrightnotice{{Copyright \\copyright\\ 2026 Lars Warren Ericson and Dana S. Scott}}
        \\abstract{{
        {abstract_latex.strip()}
        }}
        \\hypersetup{{
          pdftitle={{{TITLE}}},
          pdfauthor={{Lars Warren Ericson; Dana S. Scott}},
          pdfsubject={{Carnegie Mellon University School of Computer Science Technical Report {REPORT_NUMBER}}},
          pdfkeywords={{Lean 4, formal verification, measurement theory, linear inequalities}}
        }}

        \\begin{{document}}

        \\maketitle
        """
    ).strip()


def main() -> int:
    if not SRC.is_file():
        print(f"error: missing {SRC}; run scripts/generate_arxiv_with_code.sh first", file=sys.stderr)
        return 1
    if not PREAMBLE.is_file():
        print(f"error: missing {PREAMBLE}", file=sys.stderr)
        return 1

    for d in (LISTINGS_DIR, FIGURES_DIR):
        if d.exists():
            for path in d.iterdir():
                if path.is_file():
                    path.unlink()
        d.mkdir(parents=True, exist_ok=True)

    raw = SRC.read_text(encoding="utf-8")
    body = drop_github_nav(raw)
    body = inject_model_cards(body)
    figure_captions = parse_figure_captions(body)
    body = strip_html_comments(body)
    body = normalize_appendix_headings(body)
    abstract_md, body = extract_abstract(body)
    body = strip_manual_section_numbers(body)
    body = github_math_to_tex(body)
    body, placeholders = replace_fences(body, figure_captions)

    latex_body = pandoc_to_latex(body, shift=True)
    latex_body = inject_placeholders(latex_body, placeholders)
    latex_body = cleanup_pandoc_latex(latex_body)
    latex_body = insert_list_of_figures(latex_body)
    latex_body = insert_appendix_command(latex_body)

    abstract_latex = pandoc_to_latex(github_math_to_tex(abstract_md), shift=False) if abstract_md else ""
    abstract_latex = cleanup_abstract_latex(abstract_latex)

    preamble = PREAMBLE.read_text(encoding="utf-8")
    title_page = build_title_page(abstract_latex)
    document = preamble + "\n\n" + title_page + "\n\n" + latex_body + "\n\n\\end{document}\n"
    OUT.write_text(document, encoding="utf-8")
    n_listings = sum(1 for p in LISTINGS_DIR.iterdir() if p.is_file())
    n_figures = sum(1 for p in FIGURES_DIR.glob("*.png"))
    print(
        f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size:,} bytes, "
        f"{n_listings} listings, {n_figures} mermaid figures)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
