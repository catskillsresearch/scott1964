#!/usr/bin/env python3
"""Append Lean module index to arxiv.md → arxiv_with_code.md (build artifact)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/catskillsresearch/scott1964"

# Library files in a readable dependency order (Basic last: it re-exports).
FILES = [
    "Scott1964.lean",
    "Scott1964/MeasurementStructures/FinHead.lean",
    "Scott1964/MeasurementStructures/LinearInequalities/Definitions.lean",
    "Scott1964/MeasurementStructures/LinearInequalities/Separation.lean",
    "Scott1964/MeasurementStructures/LinearInequalities/Rationalization.lean",
    "Scott1964/MeasurementStructures/LinearInequalities/Sequences.lean",
    "Scott1964/MeasurementStructures/LinearInequalities/ScottTheorems.lean",
    "Scott1964/MeasurementStructures/LinearInequalities/OrderedGroup.lean",
    "Scott1964/MeasurementStructures/Preference/Direct.lean",
    "Scott1964/MeasurementStructures/Preference/Cycle.lean",
    "Scott1964/MeasurementStructures/Preference/Intransitive.lean",
    "Scott1964/MeasurementStructures/Differences/Pair.lean",
    "Scott1964/MeasurementStructures/Differences/Ordered.lean",
    "Scott1964/MeasurementStructures/Probability/Basic.lean",
    "Scott1964/MeasurementStructures/Probability/Atoms.lean",
    "Scott1964/MeasurementStructures/Probability/Finite.lean",
    "Scott1964/MeasurementStructures/Probability/KPSCounterexample.lean",
    "Scott1964/MeasurementStructures/Probability/Infinite/EventSpace.lean",
    "Scott1964/MeasurementStructures/Probability/Infinite/HahnBanach.lean",
    "Scott1964/MeasurementStructures/Probability/Infinite/Kelley.lean",
    "Scott1964/MeasurementStructures/Probability/Infinite/Reconstructed.lean",
    "Scott1964/MeasurementStructures/Basic.lean",
]

FILE_ROLES: dict[str, str] = {
    "Scott1964.lean": "Root import graph",
    "Scott1964/MeasurementStructures/FinHead.lean": "Stable distinguished sequence index",
    "Scott1964/MeasurementStructures/LinearInequalities/Definitions.lean":
        "Scott's finite inequality predicates",
    "Scott1964/MeasurementStructures/LinearInequalities/Separation.lean":
        "Finite convex separation",
    "Scott1964/MeasurementStructures/LinearInequalities/Rationalization.lean":
        "Rational coefficient reduction",
    "Scott1964/MeasurementStructures/LinearInequalities/Sequences.lean":
        "Explicit finite sequence conditions",
    "Scott1964/MeasurementStructures/LinearInequalities/ScottTheorems.lean":
        "Theorems 1.1–1.4",
    "Scott1964/MeasurementStructures/LinearInequalities/OrderedGroup.lean":
        "Ordered-group consequences and obstruction",
    "Scott1964/MeasurementStructures/Preference/Direct.lean":
        "Finite Scott–Suppes staircase representation",
    "Scott1964/MeasurementStructures/Preference/Cycle.lean":
        "Local cycle reductions",
    "Scott1964/MeasurementStructures/Preference/Intransitive.lean":
        "Theorem 2.1",
    "Scott1964/MeasurementStructures/Differences/Pair.lean":
        "Theorem 3.1",
    "Scott1964/MeasurementStructures/Differences/Ordered.lean":
        "Theorem 3.2",
    "Scott1964/MeasurementStructures/Probability/Basic.lean":
        "Finite qualitative probability definitions",
    "Scott1964/MeasurementStructures/Probability/Atoms.lean":
        "Atom-vector representation",
    "Scott1964/MeasurementStructures/Probability/Finite.lean":
        "Theorem 4.1 and signed charges",
    "Scott1964/MeasurementStructures/Probability/KPSCounterexample.lean":
        "Kraft–Pratt–Seidenberg counterexample",
    "Scott1964/MeasurementStructures/Probability/Infinite/EventSpace.lean":
        "Universal event space",
    "Scott1964/MeasurementStructures/Probability/Infinite/HahnBanach.lean":
        "Closed-cone separation",
    "Scott1964/MeasurementStructures/Probability/Infinite/Kelley.lean":
        "Generalized Kelley cover",
    "Scott1964/MeasurementStructures/Probability/Infinite/Reconstructed.lean":
        "Modern infinite reconstruction",
    "Scott1964/MeasurementStructures/Basic.lean": "Complete library re-export",
}


def github_blob(rel: str) -> str:
    return f"{GITHUB}/blob/main/{rel}"


def paper_title(arxiv_text: str) -> str:
    first = arxiv_text.splitlines()[0] if arxiv_text else "# Scott 1964"
    if first.startswith("# "):
        return first[2:].strip()
    return first.strip()


def narrative_body(arxiv_text: str) -> str:
    body = arxiv_text
    if body.startswith("# "):
        idx = body.find("\n---\n")
        if idx != -1:
            body = body[idx + len("\n---\n") :]
        else:
            body = body[body.find("\n") + 1 :]
    return body.rstrip()


def measurement_source_appendix(files: list[str]) -> str:
    """Directory subsections, then one heading and fenced listing per file."""
    prefix = "Scott1964/MeasurementStructures/"
    parts = [
        "# Appendix B: Complete Lean source\n\n",
        "The complete source of `Scott1964/MeasurementStructures`, checked by "
        f"`lake build`. Directory names are subsections. Each filename is a "
        f"heading in this appendix. Repository: [{GITHUB}]({GITHUB}).\n\n",
    ]
    open_dirs: list[str] = []
    for rel in files:
        pieces = rel[len(prefix) :].split("/")
        dirs, fname = pieces[:-1], pieces[-1]
        shared = 0
        while (
            shared < len(open_dirs)
            and shared < len(dirs)
            and open_dirs[shared] == dirs[shared]
        ):
            shared += 1
        open_dirs = open_dirs[:shared]
        for directory in dirs[shared:]:
            open_dirs.append(directory)
            parts.append(f"{'#' * (2 + len(open_dirs))} {directory}\n\n")
        parts.append(f"{'#' * (3 + len(dirs))} {fname}\n\n")
        code = (ROOT / rel).read_text(encoding="utf-8")
        if not code.endswith("\n"):
            code += "\n"
        parts.append(f"```lean\n{code}```\n\n")
    return "".join(parts)


def main() -> None:
    arxiv_path = ROOT / "arxiv.md"
    arxiv = arxiv_path.read_text(encoding="utf-8")
    title = paper_title(arxiv)
    body = narrative_body(arxiv)

    parts: list[str] = []
    parts.append(
        "<!-- AUTO-GENERATED: run scripts/generate_arxiv_with_code.sh to refresh -->\n"
        "<!-- AGENTS: do not read or grep this file. Use arxiv.md; see .cursorignore -->\n"
    )
    parts.append(f"# {title} — narrative + Lean module index\n\n")
    parts.append(
        "> **Generated artifact — not for agents.** Inventory and narrative live in "
        "[`arxiv.md`](arxiv.md). Regenerate with `scripts/generate_arxiv_with_code.sh`. "
        "This file is stale whenever it is older than `arxiv.md` or any listed `.lean` file.\n\n"
    )
    parts.append(
        f"*Generated {date.today().isoformat()} from `arxiv.md` and the module list "
        "in `scripts/generate_arxiv_with_code.py`.*\n\n"
    )
    parts.append(
        "**Review copy.** The narrative body matches [`arxiv.md`](arxiv.md) "
        "(excluding the title block through the first `---`). "
        "This file appends **Appendix B: Complete Lean source** for "
        "`Scott1964/MeasurementStructures`, with one heading per file, and "
        "**Appendix C: Scott 1964 source paper**. Appendix A is the Concordance "
        "methodology section from `arxiv.md`.\n\n"
    )
    parts.append("---\n\n")
    parts.append("## Document map\n\n")
    parts.append("| Part | Contents |\n")
    parts.append("| --- | --- |\n")
    parts.append("| **Narrative** | Full `arxiv.md` body with inline Lean gists |\n")
    parts.append("| **Appendix A** | Concordance methodology |\n")
    parts.append("| **Appendix B** | Full `MeasurementStructures` source |\n")
    parts.append("| **Appendix C** | Scott 1964 source PDF |\n\n")
    parts.append("---\n\n")
    parts.append("# Narrative (from arxiv.md)\n\n")
    parts.append(body)
    parts.append("\n\n---\n\n")
    source_files = [
        f for f in FILES if f.startswith("Scott1964/MeasurementStructures/")
    ]
    parts.append(measurement_source_appendix(source_files))
    total_lines = sum(len((ROOT / f).read_text().splitlines()) for f in source_files)
    parts.append("---\n\n")
    parts.append("# Appendix C: Scott 1964 source paper\n\n")
    parts.append(
        "The following pages reproduce the working source used throughout this "
        "report: Dana S. Scott, *Measurement Structures and Linear Inequalities*, "
        "Journal of Mathematical Psychology **1** (1964), 233--247, from "
        "`sources/ScottMeasurement1964.pdf`. The journal PDF is not licensed "
        "under this repository's Apache-2.0 terms; see `NOTICE` and "
        "`sources/README.md`.\n\n"
    )

    out = ROOT / "arxiv_with_code.md"
    out.write_text("".join(parts))
    print(f"wrote {out} ({total_lines} Lean lines indexed across {len(FILES)} files)")


if __name__ == "__main__":
    main()
