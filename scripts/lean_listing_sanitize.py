#!/usr/bin/env python3
"""Prepare Lean sources for ``\\lstinputlisting`` in the arXiv pdfLaTeX build.

Listings use the ``leanbox`` style in ``tex_preamble_arxiv.tex``. A character in
that ``literate`` table stays as UTF-8 and is rendered as LaTeX. Anything else
is rewritten through ``LEAN_UNICODE_REPLACEMENTS``. An unmapped non-ASCII
character is an error: the build must not silently print ``?``.
"""

from __future__ import annotations

import re
import unicodedata
from functools import lru_cache
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
_PREAMBLE = _SCRIPTS / "tex_preamble_arxiv.tex"
_LEANBOX_LITERATE_RE = re.compile(r"\{([^}]+)\}\{\{")

# Order matters: longer / composite replacements first where needed.
LEAN_UNICODE_REPLACEMENTS: tuple[tuple[str, str], ...] = (
    # Composites (including combining-mark spellings used in docstrings)
    ("⋢", " sqsubneq "),
    ("⊑\u0338", " sqsubneq "),
    ("⁻¹", "^-1"),
    ("⟶", " --> "),
    ("⟷", " <-> "),
    ("⟨", "<"),
    ("⟩", ">"),
    ("↦", " |-> "),
    ("⊢", " |- "),
    ("⊨", " |= "),
    ("⊬", " |/- "),
    ("⊭", " |/= "),
    # modal / hybrid operators
    ("□", "[] "),
    ("◇", "<> "),
    ("∼", "~"),
    ("⋀", " /\\ "),
    ("⋁", " \\/ "),
    # logical connectives / quantifiers
    ("∀", "forall "),
    ("∃", "exists "),
    ("¬", "not "),
    ("∧", " /\\ "),
    ("∨", " \\/ "),
    ("↔", " <-> "),
    ("→", " -> "),
    ("←", " <- "),
    ("⇒", " => "),
    ("⊥", "False"),
    # set theory
    ("∈", " in "),
    ("∉", " notin "),
    ("∪", " U "),
    ("∩", " I "),
    ("⊆", " subseteq "),
    ("⊇", " supseteq "),
    ("∅", "{}"),
    # relations
    ("≠", " != "),
    ("≤", " <= "),
    ("≥", " >= "),
    ("≅", " ~= "),
    ("≪", " << "),
    ("⊑", " sqsub "),
    ("⊔", " sqsup "),
    ("⊓", " sqcap "),
    ("⊤", " top "),
    ("⊣", " dashv "),
    ("↟", " Up "),
    ("⇄", " <=> "),
    ("⨆", " bigcup "),
    ("𝕆", " O "),
    ("∞", " inf "),
    ("′", "'"),
    ("ḡ", "g"),
    ("̄", ""),  # combining macron (often after explicit pairs above)
    ("̸", ""),  # combining long slash overlay
    # arrows / misc operators
    ("↑", ""),
    ("↓", ""),
    ("↥", ""),
    ("▸", " |> "),
    ("∘", " comp "),
    ("·", "*"),
    ("×", " x "),
    ("§", "S"),
    ("—", "--"),
    ("–", "-"),
    ("…", "..."),
    # Greek letters (identifiers in Lean source)
    ("Γ", "Gamma"),
    ("Δ", "Delta"),
    ("Θ", "Theta"),
    ("Σ", "Sigma"),
    ("Η", "Eta"),
    ("Κ", "Kappa"),
    ("φ", "phi"),
    ("ψ", "psi"),
    ("χ", "chi"),
    ("σ", "sigma"),
    ("τ", "tau"),
    ("α", "a"),
    ("β", "b"),
    ("λ", "fun "),
    # double-struck / blackboard
    ("ℕ", "Nat"),
    ("ℤ", "Int"),
    # sub/superscripts
    ("₀", "_0"),
    ("₁", "_1"),
    ("₂", "_2"),
    ("₃", "_3"),
    ("ₙ", "_n"),
    ("ₚ", "_p"),
    ("ᵢ", "_i"),
    ("₊", "_+"),
    ("⁺", "^+"),
    ("⁻", "^-"),
    ("¹", "1"),
    # box drawing (set-builder bars and ASCII-art flowcharts in fenced blocks)
    ("│", "|"),
    ("─", "-"),
    ("━", "-"),
    ("├", "+"),
    ("┤", "+"),
    ("┬", "+"),
    ("┴", "+"),
    ("┼", "+"),
    ("┌", "+"),
    ("┐", "+"),
    ("└", "+"),
    ("┘", "+"),
    ("║", "|"),
    ("═", "="),
    ("╔", "+"),
    ("╗", "+"),
    ("╚", "+"),
    ("╝", "+"),
    ("╠", "+"),
    ("╣", "+"),
    ("•", "*"),
    ("▪", "*"),
    ("▶", ">"),
    ("◀", "<"),
)


@lru_cache(maxsize=1)
def leanbox_literate_chars(*, preamble_path: Path | None = None) -> frozenset[str]:
    """Characters the ``leanbox`` listing style renders via ``literate``."""
    path = preamble_path or _PREAMBLE
    text = path.read_text(encoding="utf-8")
    start = text.find("\\lstdefinestyle{leanbox}")
    if start < 0:
        raise RuntimeError(f"leanbox style not found in {path}")
    end = text.find("\\lstset{style=leanbox}", start)
    if end < 0:
        raise RuntimeError(f"leanbox literate block not terminated in {path}")
    chars: set[str] = set()
    for key in _LEANBOX_LITERATE_RE.findall(text[start:end]):
        chars.update(key)
    return frozenset(chars)


def _replacements_for_listings(allowed: frozenset[str]) -> tuple[tuple[str, str], ...]:
    """Drop ASCII fallbacks for glyphs ``leanbox`` already typesets."""
    return tuple(
        (src, dst)
        for src, dst in LEAN_UNICODE_REPLACEMENTS
        if not (len(src) == 1 and src in allowed)
    )


class UnmappedLeanCharError(RuntimeError):
    """A Lean listing contains a character with no LaTeX rendering."""


def sanitize_lean_for_arxiv(
    text: str,
    *,
    preamble_path: Path | None = None,
    source_name: str | None = None,
) -> str:
    allowed = leanbox_literate_chars(preamble_path=preamble_path)
    out = text
    for src, dst in _replacements_for_listings(allowed):
        out = out.replace(src, dst)

    missing: set[str] = set()
    cleaned: list[str] = []
    for ch in out:
        if ord(ch) < 128 or ch in allowed:
            cleaned.append(ch)
            continue
        decomp = "".join(
            c
            for c in unicodedata.normalize("NFD", ch)
            if unicodedata.category(c) != "Mn"
        )
        if decomp and all(ord(c) < 128 or c in allowed for c in decomp):
            cleaned.append(decomp)
            continue
        missing.add(ch)
    if missing:
        where = source_name or "listing"
        samples: list[str] = []
        for lineno, line in enumerate(text.splitlines(), 1):
            bad = [ch for ch in line if ch in missing]
            if not bad:
                continue
            shown = ", ".join(f"U+{ord(ch):04X} {ch!r}" for ch in dict.fromkeys(bad))
            samples.append(f"  {where}:{lineno}: {shown}: {line.strip()[:160]}")
            if len(samples) >= 20:
                break
        raise UnmappedLeanCharError(
            "Unmapped Lean characters; refusing to replace them with '?'. "
            "Add a leanbox literate entry in scripts/tex_preamble_arxiv.tex.\n"
            + "\n".join(samples)
        )
    return "".join(cleaned)


def chunk_line_ranges(line_count: int, chunk_size: int = 350) -> list[tuple[int, int]]:
    if line_count <= chunk_size:
        return [(1, line_count)]
    ranges: list[tuple[int, int]] = []
    start = 1
    while start <= line_count:
        end = min(start + chunk_size - 1, line_count)
        ranges.append((start, end))
        start = end + 1
    return ranges
