#!/usr/bin/env bash
# Regenerate arxiv.tex, compile arxiv.pdf (tracked), and dist/arxiv_submit.zip.
set -euo pipefail
cd "$(dirname "$0")/.."

TEX="arxiv.tex"
PDF="arxiv.pdf"

echo "==> Regenerating arxiv.tex + lean-listings/ + figures/"
bash scripts/build_arxiv_tex.sh

echo "==> Compiling PDF (pdfLaTeX via latexmk)"
latexmk -C "$TEX" >/dev/null 2>&1 || true
rm -f arxiv.aux arxiv.out arxiv.toc
latexmk -pdf \
  -pdflatex="pdflatex -interaction=nonstopmode -halt-on-error" \
  -interaction=nonstopmode \
  -halt-on-error \
  "$TEX" >/dev/null 2>&1 || {
  echo "latexmk reported errors; tail of log:" >&2
  tail -n 40 arxiv.log >&2 || true
  exit 1
}

if [[ -f arxiv.log ]]; then
  overfull="$(grep -c 'Overfull \\hbox' arxiv.log || true)"
  if [[ "$overfull" != "0" ]]; then
    echo "error: $overfull Overfull \\hbox line(s) in arxiv.log" >&2
    grep 'Overfull \\hbox' arxiv.log | head -20 >&2 || true
    exit 1
  fi
fi

echo "wrote $PDF ($(du -h "$PDF" | cut -f1))"

echo "==> Packaging arXiv submission zip"
bash scripts/package_arxiv_submit.sh --skip-tex-build
