[![Lean 4](https://img.shields.io/github/actions/workflow/status/catskillsresearch/scott1964/build.yml?label=Lean%204)](https://github.com/catskillsresearch/scott1964/actions/workflows/build.yml)

# scott1964

Lean 4 formalization of Dana Scott's **1964** *Measurement Structures and
Linear Inequalities* (J. Math. Psychology 1 (1964), 233–247).

Scott proves four general finite linear-inequality results (Theorems 1.1--1.4)
and applies them to intransitive indifference (Theorem 2.1), additive utility
for pairs and ordered differences (Theorems 3.1--3.2), and finite subjective
probability (Theorem 4.1).

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

Complete sorry-free formalizations of all eight numbered theorems in the
paper are re-exported by `Scott1964/MeasurementStructures/Basic.lean`.
`Challenge.lean` is the Mathlib-only statement of record and contains the
deliberate Palomar proof holes; `Solution.lean` imports the completed proofs.
The Comparator checks all eight source theorems plus the separately labelled
modern infinite reconstruction.

The probability development also includes the finite
Kraft--Pratt--Seidenberg counterexample. The infinite theorem is not attributed
to Scott as a published result: Scott only announced an extension in 1964,
whereas this repository proves a modern Hahn--Banach/Kelley reconstruction
under an explicit generalized Kelley condition.

Additional source-facing results include:

- `LinearInequalities/OrderedGroup.lean`: every finite subset of a linearly
  ordered abelian group has an order-reflecting local real model that preserves
  visible addition equations (`finite_local_real_embedding`), while the
  lexicographic `ℤ × ℤ` example is strictly monotonic on its generated
  positive monoid but admits no global additive real realization;
- the literal characteristic-vector form `ProbVectorCancellation` of
  condition `(4_B)` and the equivalent `theorem_4_1_vector`;
- Scott's p. 15 signed-charge characterization, in atom-count and literal
  vector-sum forms (`scott_p15_signed_charge` and
  `scott_p15_signed_charge_vector`); and
- bundled `DeFinettiAxioms` together with the integrated KPS order, which
  satisfies those five axioms but proves `¬ RealizableProbability KPSGe`.

The current proof of Theorem 2.1 is the direct finite Scott--Suppes staircase
construction. `Preference/Cycle.lean` separately formalizes Scott's local
cycle-shortening reductions from the 1964 argument.

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
deliberate `sorry`s. `Solution.lean` imports the corresponding kernel-checked,
sorry-free proofs. The proofs use only the standard axioms disclosed in
`comparator.json`: `propext`, `Quot.sound`, and `Classical.choice`.
