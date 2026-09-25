#!/usr/bin/env bash
# Build arxiv.tex and zip everything arXiv needs to compile it (pdfLaTeX).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TEX="arxiv.tex"
CMU_STYLE="cmu-titlepage2.sty"
SCOTT_PDF="sources/ScottMeasurement1964.pdf"
LISTINGS_DIR="lean-listings"
FIGURES_DIR="figures"
OUT_DIR="dist"
ZIP="${OUT_DIR}/arxiv_submit.zip"

mapfile -t LEAN_FILES < <(
  printf '%s\n' Scott1964.lean Challenge.lean Solution.lean
  find Scott1964 -name '*.lean' | sort
)

if [[ "${1:-}" != "--skip-tex-build" ]]; then
  echo "==> Regenerating arxiv_with_code.md, arxiv.tex, listings, and figures"
  bash scripts/build_arxiv_tex.sh
fi

mapfile -t FIGURE_PNGS < <(find "$FIGURES_DIR" -maxdepth 1 -name '*.png' 2>/dev/null | sort)

missing=0
if [[ ! -f "$TEX" ]]; then
  echo "error: missing $TEX" >&2
  missing=1
fi
if [[ ! -f "$CMU_STYLE" ]]; then
  echo "error: missing $CMU_STYLE" >&2
  missing=1
fi
if [[ ! -f "$SCOTT_PDF" ]]; then
  echo "error: missing $SCOTT_PDF" >&2
  missing=1
fi
if [[ ! -d "$LISTINGS_DIR" ]]; then
  echo "error: missing $LISTINGS_DIR" >&2
  missing=1
fi
lean_count="$(find "$LISTINGS_DIR" -maxdepth 1 -type f 2>/dev/null | wc -l)"
if [[ "$lean_count" -eq 0 ]]; then
  echo "error: no listing files in $LISTINGS_DIR" >&2
  missing=1
fi
if [[ ${#FIGURE_PNGS[@]} -eq 0 ]]; then
  echo "error: no mermaid figure PNGs in $FIGURES_DIR" >&2
  missing=1
fi
for f in "${LEAN_FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "error: missing $f" >&2
    missing=1
  fi
done
if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

mkdir -p "$OUT_DIR"
rm -f "$ZIP"

echo "==> Writing 00README.json (mark listing files and figures as include)"
python3 - <<'PY'
import json
from pathlib import Path

sources = [
    {"filename": "arxiv.tex", "usage": "toplevel"},
    {"filename": "references.bib", "usage": "include"},
    {"filename": "cmu-titlepage2.sty", "usage": "include"},
    {"filename": "sources/ScottMeasurement1964.pdf", "usage": "include"},
]
for path in sorted(p for p in Path("lean-listings").iterdir() if p.is_file()):
    sources.append({"filename": path.as_posix(), "usage": "include"})
for path in sorted(Path("figures").glob("*.png")):
    sources.append({"filename": path.as_posix(), "usage": "include"})
lean = (
    ["Scott1964.lean", "Challenge.lean", "Solution.lean"]
    + sorted(p.as_posix() for p in Path("Scott1964").rglob("*.lean"))
)
for name in lean:
    sources.append({"filename": name, "usage": "include"})
readme = {"process": {"compiler": "pdflatex"}, "sources": sources}
Path("00README.json").write_text(json.dumps(readme, indent=2) + "\n")
print(f"  {len(sources)} sources")
PY

echo "==> Packaging"
zip -r "$ZIP" \
  00README.json \
  "$TEX" \
  references.bib \
  "$CMU_STYLE" \
  "$SCOTT_PDF" \
  "$LISTINGS_DIR" \
  "${LEAN_FILES[@]}" \
  "${FIGURE_PNGS[@]}"

echo "wrote $ZIP ($(du -h "$ZIP" | cut -f1))"
echo "Contents:"
zipinfo -1 "$ZIP" | sed 's/^/  /' | head -50
echo
echo "Upload $ZIP to arXiv (pdfLaTeX; UTF-8 Lean listings render via the listings literate"
echo "table; mermaid diagrams ship as pre-rendered figures/*.png since AutoTeX cannot run mmdc)."
echo "On arXiv Add Files: Delete All before uploading (uploads merge, they do not replace)."
echo "On arXiv Review Files: if any lean-listings/* or figures/*.png are marked for"
echo "deletion, UNCHECK them."
