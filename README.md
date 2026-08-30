[![Lean 4](https://img.shields.io/github/actions/workflow/status/catskillsresearch/scott1964/build.yml?label=Lean%204)](https://github.com/catskillsresearch/scott1964/actions/workflows/build.yml)

# scott1964

Lean 4 formalization of Dana Scott's **1964** *Measurement Structures and
Linear Inequalities* (J. Math. Psychology 1 (1964), 233–247).

Scott applies the general solvability criterion for finite systems of linear
inequalities to three representation problems: intransitive indifference
(Theorem 2.1), ordered differences (Theorem 3.2), and subjective probability
(Theorem 4.1).

Standalone package — no dependency on the 1972/1976/1980/1982 domain-theory
formalizations. This repo is submitted to
[Palomar](https://palomar-registry.org/about) on its own (see
`PROVENANCE.md`).

The pin is `leanprover/lean4:v4.33.0` (same as
[`scott1976`](../scott1976)).

Original Lean and author-written docs are Apache-2.0. Scott's paper PDF
`sources/ScottMeasurement1964.pdf` is **not** under that license; see
`NOTICE` and `sources/README.md`.

## Status

Early scaffold. `Challenge.lean` states Theorems 2.1, 3.2, and 4.1 with
deliberate `sorry`s; `Scott1964/MeasurementStructures/` is empty apart from
`Basic.lean`, so `comparator.json` compares no declaration yet. A name moves
into `theorem_names` only once its proof reaches `Solution.lean`.

## Files (Palomar)

| File | Role |
|---|---|
| `arxiv.md` | Formalization narrative and theorem inventory |
| `sources/ScottMeasurement1964.pdf` | Primary source PDF (Scott 1964) |
| `Scott1964/` | Sorry-free development |
| `Challenge.lean` | Palomar statement of record |
| `Solution.lean` | Palomar solution module: imports `Scott1964/*` proofs |
| `comparator.json` | Comparator config for the compared theorems and definitions |
| `formalization.yaml` | Palomar / formalization.yaml v0.4 metadata |
| `PROVENANCE.md` | Standalone Palomar submission; relation to siblings |

## Build

```bash
lake exe cache get
lake build
```

`lake build` typechecks `Scott1964`, `Challenge.lean`, and `Solution.lean`. Before a
Palomar submission, run:

```bash
bash scripts/palomar_preflight.sh
```

## Source OCR

Triple-pass Cursor vision OCR (from [`scott_models`](../scott_models)):

```bash
bash scripts/ocr_pdf_pipeline.sh                 # sources/ScottMeasurement1964.pdf
bash scripts/ocr_pdf_pipeline.sh --pages 1-3     # smoke test
bash scripts/ocr_pdf_pipeline.sh --status
```

See `sources/README.md`. Page PNGs and `.venv-ocr/` are gitignored.

`Challenge.lean` imports only Mathlib and states the compared results with
deliberate `sorry`s. Their proofs are to live in
`Scott1964/MeasurementStructures/*`, imported by `Solution.lean`. See
`arxiv.md` for the theorem inventory and known gaps.
