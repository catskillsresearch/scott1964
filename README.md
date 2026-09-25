[![Lean 4](https://img.shields.io/github/actions/workflow/status/catskillsresearch/scott1964/build.yml?label=Lean%204)](https://github.com/catskillsresearch/scott1964/actions/workflows/build.yml)

# scott1964

Lean 4 formalization of Dana Scott's **1964** *Measurement Structures and
Linear Inequalities* (J. Math. Psychology 1 (1964), 233–247).

The accompanying report, *Formalization of Scott's Measurement Structures
and Linear Inequalities in Lean 4*, is by **Lars Warren Ericson** (independent
researcher, d/b/a Catskills Research Company), **Dana S. Scott** (Computer
Science Department, Carnegie Mellon University, Emeritus), **Vijay D'Silva**
(Google Research), and **Brian Milnes** (Unaffiliated).
It is being prepared for the Carnegie Mellon University School of Computer
Science Technical Report series as **CMU-CS-26-XXX**, with cross-archival to
arXiv under cs.LO and math.LO.

Scott proves four general finite linear-inequality results (Theorems 1.1--1.4)
and applies them to intransitive indifference (Theorem 2.1), additive utility
for pairs and ordered differences (Theorems 3.1--3.2), and finite subjective
probability (Theorem 4.1).

Standalone package — no dependency on the 1972/1976/1980/1982 domain-theory
formalizations. This repo is submitted to
[Palomar](https://palomar-registry.org/about) on its own (see
`PROVENANCE.md`).

The pin is `leanprover/lean4:v4.35.0-rc2`.

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
whereas this repository first states and proves a stronger modern
Hahn--Banach/Kelley `iff` characterization under an explicit generalized
Kelley condition. Its proof adapts Kelley's 1959 separation method; its exact
statement is not attributed to either Scott or Kelley.

## Compared characterizations in plain language

Every compared theorem is an equivalence. Its left side says that one
real-valued numerical model represents the qualitative data exactly; its right
side gives the conditions under which that model exists.

- **Theorem 1.1.** A linear functional realizes the chosen nonnegative part
  `N` of a finite symmetric vector set exactly when every vector has at least
  one weak sign and cancellation holds. Weighted cancellation says that
  declared-nonnegative vectors with strictly positive real weights cannot sum
  to zero unless every participating vector is neutral—its negative is also
  declared nonnegative.
- **Theorem 1.2.** For finite rational-coordinate vectors, the same
  representation is equivalent to sign completeness and unweighted
  cancellation. Repeating a vector supplies an integer multiplicity, replacing
  the positive real weights of Theorem 1.1.
- **Theorem 1.3.** A linear functional represents a relation on a finite
  rational set exactly when the relation is complete and has relational
  cancellation: if two finite sequences have equal vector sums and every
  left term is related to its right term, then all those comparisons also hold
  in reverse.
- **Theorem 1.4.** The same representation exists exactly when the relation
  extends to the additive closure of the original set as a complete relation
  that preserves comparisons under addition and cancels equal totals.
- **Theorem 2.1.** A finite preference relation has a unit-threshold
  representation `xPy ↔ f(x) ≥ f(y)+1` exactly when it is irreflexive and
  satisfies Scott's two four-alternative axioms.
- **Theorem 3.1.** A relation on mixed pairs is represented exactly by
  `f(x)+f'(x')` iff it is total and satisfies pair-permutation cancellation.
  Independently permute the first and second coordinates of a finite list; if
  every non-distinguished original pair is at least its permuted pair, the
  distinguished comparison must hold in reverse.
- **Theorem 3.2.** A four-place relation is represented exactly by comparing
  utility differences `f(x)-f(y)` iff it is total, satisfies the analogous
  independent-permutation cancellation scheme, and satisfies reversal:
  `D(x,y,z,w)` implies `D(w,z,y,x)`.
- **Theorem 4.1.** A relation on a finite Boolean algebra is represented
  exactly by a normalized, nonnegative, finitely additive probability iff:
  the certain event is weakly above the impossible event but not conversely;
  every event is weakly above the impossible event; every two events are
  comparable; and atom-count cancellation holds. The last condition compares
  two finite event lists in which every atom occurs equally often: all
  non-distinguished comparisons force the distinguished comparison in reverse.
- **Modern infinite characterization.** On an arbitrary Boolean algebra,
  probability representation is equivalent to the first three probability
  conditions above and `GeneralizedKelleyCondition`. Event differences form a
  normed universal event span. The weak-comparison cone is the closed
  dual-polar cone forced nonnegative by all continuous linear functionals that
  are nonnegative on the declared weak comparisons. Strict-comparison vectors
  must lie in this cone and be covered by countably many closed convex layers,
  each avoiding zero and closed upward under addition of weak-cone vectors.
  This is a new, stronger modern `iff` theorem first stated and proved here.
  It adapts Kelley's 1959 countable-cover/Hahn--Banach method; Scott's final
  paragraph contains only an announcement, so the theorem is not attributed
  to him as a published or recoverable statement.

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

## Report and archival files

| File | Role |
|---|---|
| `arxiv.md` | CMU technical-report narrative, theorem inventory, and §4 concordance |
| `scripts/check_concordance.py` | Coverage, quotation, and Lean-name check for §4 cards |
| `scripts/emit_concordance.py` | Regenerates the §4 card body from source spans |
| `arxiv.pdf` | Built CMU report PDF for cross-archival |
| `docs/CMU_TECH_REPORT.md` | Report-number, build, and release checklist |
| `docs/ARXIV_SUBMISSION.md` | arXiv cross-archive metadata |
| `sources/ScottMeasurement1964.pdf` | Primary source PDF (Scott 1964) |
| `Scott1964/` | Sorry-free development |
| `Challenge.lean` | Palomar statement of record |
| `Solution.lean` | Palomar solution module: imports `Scott1964/*` proofs |
| `comparator.json` | Comparator config for the compared theorems and definitions |
| `formalization.yaml` | Palomar / formalization.yaml v0.4 metadata |
| `PROVENANCE.md` | Standalone Palomar submission; relation to siblings |
| `docs/PALOMAR_EDITORIAL_AUDIT.md` | Full vs mechanical preflight; packaging checklist |

## Build

```bash
lake exe cache get
lake build
```

`lake build` typechecks `Scott1964`, `Challenge.lean`, and `Solution.lean`.

**Routine / CI:** mechanical preflight only (pretty-print closure + Palomar-pinned Comparator):

```bash
bash scripts/palomar_preflight.sh --mechanical-only
```

**Before Palomar submission:** full preflight (mechanical + editorial LLM audit):

```bash
bash scripts/palomar_preflight.sh
```

See `docs/PALOMAR_EDITORIAL_AUDIT.md` for packaging checklist and auth.

The report's exhaustive Scott–Lean concordance has a separate coverage and
declaration-reference check:

```bash
python3 scripts/check_concordance.py
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
