#!/usr/bin/env bash
# Vision OCR pipeline wrapper (see scripts/ocr_pdf_pipeline.py).
# Default PDF: sources/ScottMeasurement1964.pdf
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [[ ! -x .venv-ocr/bin/python ]]; then
  python3 -m venv .venv-ocr
  .venv-ocr/bin/pip install -r scripts/requirements-ocr.txt
fi
# If the first argument is a flag (or missing), Python uses the default PDF.
if [[ $# -eq 0 ]] || [[ "${1:-}" == -* ]]; then
  echo "ocr_pdf_pipeline: no PDF given; default is sources/ScottMeasurement1964.pdf" >&2
  echo "  Example: bash scripts/ocr_pdf_pipeline.sh MyPaper.pdf --pages 14" >&2
fi
exec .venv-ocr/bin/python scripts/ocr_pdf_pipeline.py "$@"
