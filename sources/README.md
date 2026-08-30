# Source materials

`ScottMeasurement1964.pdf` is Dana S. Scott, *Measurement Structures and
Linear Inequalities*, Journal of Mathematical Psychology 1 (1964), 233–247.
Copyright 1964 by Academic Press Inc. It is included for citation and
transcription checking only. It is **not** licensed under this repository's
Apache-2.0 terms.

## Vision OCR (triple pass + merge)

From the repo root (needs `pdftoppm`, and `CURSOR_API_KEY` in
`../tokens_ssto.yaml`):

```bash
bash scripts/ocr_pdf_pipeline.sh                          # full PDF
bash scripts/ocr_pdf_pipeline.sh --pages 1-3              # smoke test
bash scripts/ocr_pdf_pipeline.sh --png-only               # render pages only
bash scripts/ocr_pdf_pipeline.sh --status                 # resume state
bash scripts/ocr_pdf_pipeline.sh --merge-only             # restitch merged.md
```

Outputs (gitignored page PNGs / logs; commit the stitched draft when ready):

| Path | Role |
|------|------|
| `sources/pages/ScottMeasurement1964/` | Per-page PNGs + `pass{1,2,3}.md` + `merged.md` |
| `sources/ScottMeasurement1964_vision.md` | Stitched draft transcription |
| `sources/ocr_ScottMeasurement1964_run.log` | Run log |

After human review, promote the draft to `ScottMeasurement1964.md` (working
ground truth for Challenge wording). Scott's wording remains under Scott's /
the publisher's copyright.

Do not treat the PDF or transcriptions as redistributable under Apache-2.0.
