#!/usr/bin/env python3
"""Append complete Lean source to arxiv.md → arxiv_with_code.md (build artifact)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

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


def main() -> None:
    arxiv_path = ROOT / "arxiv.md"
    arxiv = arxiv_path.read_text()
    title = paper_title(arxiv)
    body = narrative_body(arxiv)

    parts: list[str] = []
    parts.append(
        "<!-- AUTO-GENERATED: run scripts/generate_arxiv_with_code.sh to refresh -->\n"
        "<!-- AGENTS: do not read or grep this file. Use arxiv.md; see .cursorignore -->\n"
    )
    parts.append(f"# {title} — full narrative + complete Lean source\n\n")
    parts.append(
        "> **Generated artifact — not for agents.** Inventory and narrative live in "
        "[`arxiv.md`](arxiv.md). Regenerate with `scripts/generate_arxiv_with_code.sh`. "
        "This file is stale whenever it is older than `arxiv.md` or any listed `.lean` file.\n\n"
    )
    parts.append(
        f"*Generated {date.today().isoformat()} from `arxiv.md` and all library "
        "`.lean` files in dependency order (`Scott1964.lean`).*\n\n"
    )
    parts.append(
        "**Review copy.** The narrative body matches [`arxiv.md`](arxiv.md) "
        "(excluding the title block through the first `---`). "
        "This file appends **Appendix A: Complete Lean source** with every line "
        "of the formalization inlined below.\n\n"
    )
    parts.append("---\n\n")
    parts.append("## Document map\n\n")
    parts.append("| Part | Contents |\n")
    parts.append("| --- | --- |\n")
    parts.append("| **§1–§10** | Full `arxiv.md` narrative |\n")
    parts.append("| **Appendix A** | Complete Lean 4 source, one subsection per file |\n\n")
    parts.append("### Appendix A — file index\n\n")

    total_lines = 0
    for f in FILES:
        n = len((ROOT / f).read_text().splitlines())
        total_lines += n
        parts.append(f"- [`{f}`](#{f.replace('/', '').replace('.', '').lower()}) — {n} lines\n")

    parts.append(f"\n**Total:** {len(FILES)} files, {total_lines} lines of Lean.\n\n")
    parts.append("---\n\n")
    parts.append("# Narrative (from arxiv.md)\n\n")
    parts.append(body)
    parts.append("\n\n---\n\n")
    parts.append("# Appendix A: Complete Lean source\n\n")
    parts.append("| Role | File |\n")
    parts.append("| --- | --- |\n")
    for f in FILES:
        parts.append(f"| {FILE_ROLES[f]} | `{f}` |\n")
    parts.append(
        "\nPrimary source (PDF): [`sources/ScottMeasurement1964.pdf`]"
        "(sources/ScottMeasurement1964.pdf) — Dana S. Scott, *Measurement Structures "
        "and Linear Inequalities* (J. Math. Psychology 1, 1964).\n\n"
    )
    parts.append(
        "Files appear in `Scott1964.lean` import order. "
        "Each block is a verbatim copy of the repository file at generation time.\n\n"
    )

    for f in FILES:
        content = (ROOT / f).read_text().rstrip() + "\n"
        # Nested ``` in docstrings would break markdown lean fences in arxiv_with_code.md.
        content = content.replace("```", "'''")
        n = len(content.splitlines())
        parts.append(f"## `{f}`\n\n")
        parts.append(f"*{n} lines.*\n\n")
        parts.append("```lean\n")
        parts.append(content)
        parts.append("```\n\n")

    out = ROOT / "arxiv_with_code.md"
    out.write_text("".join(parts))
    print(f"wrote {out} ({total_lines} Lean lines across {len(FILES)} files)")


if __name__ == "__main__":
    main()
