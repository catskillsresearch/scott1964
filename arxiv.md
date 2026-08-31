# A Lean 4 Development of Scott's Measurement Structures and Linear Inequalities (1964)

**Author.** Lars Warren Ericson (Catskills Research Company).
**Source paper.** Dana S. Scott, *Measurement Structures and Linear
Inequalities*, Journal of Mathematical Psychology 1 (1964), 233–247.
**Repository.** https://github.com/catskillsresearch/scott1964

---

## Abstract

This note records a Lean 4 / mathlib formalization of Dana Scott's 1964 paper
*Measurement Structures and Linear Inequalities*. Scott takes the general
criterion for solvability of a finite system of linear inequalities and
applies it, uniformly, to three finite representation problems from
measurement theory: intransitive indifference, ordered differences, and
subjective probability. In each case he obtains necessary and sufficient
conditions for the existence of a real-valued utility or measure. The
development is packaged for
[Palomar](https://palomar-registry.org/about) with a Challenge / Solution pair
and `formalization.yaml` metadata. Dana Scott was not contacted and did not
participate in, review, or endorse this formalization.

<!-- AI_MODEL_TOOL_BULLETS -->
<!-- /AI_MODEL_TOOL_BULLETS -->

## 1. Scope

The repository formalizes all eight numbered theorems in Scott's paper:

- `scott_theorem_1_1`--`scott_theorem_1_4`, the finite
  linear-inequality engine and its relational reformulations;

- `theorem_2_1`, Problem I (intransitive indifference): a binary relation `P`
  on a finite set is realizable as `f x ≥ f y + 1` exactly when it is
  irreflexive and satisfies Scott's two quadruple conditions.
- `theorem_3_2`, Problem II (ordered differences): a quaternary relation `D`
  is realizable by a single utility function exactly when it is complete,
  reversal-closed, and satisfies the infinite bundle of permutation
  conditions.
- `theorem_3_1`, the preceding additive representation theorem for a relation
  on pairs using two utility functions.
- `theorem_4_1`, Problem III (subjective probability): a qualitative ordering
  on a finite Boolean algebra is realizable by a probability measure exactly
  when it is nontrivial, nonnegative, complete, and satisfies Scott's
  cancellation condition.

The sorry-free proofs live under `Scott1964/MeasurementStructures/` and are
re-exported by `Solution.lean`. Deliberate proof holes occur only in the
Mathlib-only `Challenge.lean`.

## 2. Theorem inventory

Formalized and proved:

- §1: Theorems 1.1, 1.2, 1.3, and 1.4.
- §2: Theorem 2.1.
- §3: Theorems 3.1 and 3.2.
- §4: Theorem 4.1, for finite Boolean algebras.

The development additionally contains a finite
Kraft--Pratt--Seidenberg counterexample and
`Probability.Infinite.reconstructed_infinite_theorem_4_1`. The latter is a
modern theorem under the explicit `GeneralizedKelleyCondition`; it is not
claimed to be the unpublished theorem Scott announced in the paper.

Further formalized results and examples:

- `finite_local_real_embedding` makes Scott's ordered-group observation
  precise: a finite subset of a linearly ordered abelian group has an
  order-reflecting real model preserving each addition equation visible
  inside that subset.
- `lexPreference_strictlyMonotonic` and
  `no_global_real_additive_lex_realization` exhibit the complementary
  obstruction. Lexicographic `ℤ × ℤ` is strictly monotonic on the additive
  closure of two generators, but no additive map to `ℝ` represents the
  relation globally.
- `scott_p15_signed_charge` proves Scott's p. 15 claim that completeness and
  cancellation characterize representation by a finitely additive signed
  charge; `scott_p15_signed_charge_vector` gives its literal vector form.
- `kpsGe_deFinettiAxioms`, `not_realizableProbability_kpsGe`, and
  `deFinetti_axioms_insufficient` integrate the KPS five-atom order into the
  shared probability API: it satisfies the bundled five de Finetti axioms
  while admitting no realizing probability.

## 3. Formalization notes

Scott's condition (4_B) is stated with the algebraic sum
`x₀ + x₁ + ⋯ + xₙ₋₁` of *characteristic functions*, not the Boolean join.
The primary `theorem_4_1` uses the equivalent atom-counting reading Scott
supplies in words immediately after the theorem: every atom lies below exactly
as many `xᵢ` as `yᵢ`. `ProbVectorCancellation` and
`theorem_4_1_vector` additionally formalize the literal equality of sums of
atom vectors, with `probVectorCancellation_iff_probCancellation` proving the
equivalence.

Condition (2_D) is, as Scott notes, an infinite bundle indexed by a length and
a pair of permutations; no finite subfamily suffices. It is formalized as a
universally quantified statement over `n : ℕ` and `Equiv.Perm (Fin (n + 1))`.

The finite probability structure includes nonnegativity as part of
`IsProbability`, in addition to normalization and finite additivity. The
proofs introduce no project axioms and use only Mathlib's standard
`propext`, `Quot.sound`, and `Classical.choice`.

Theorem 2.1 currently uses the direct finite Scott--Suppes construction:
substitutability classes are ordered and represented by a finite staircase.
The local cycle reductions from Scott's 1964 proof are nevertheless
formalized in `Preference/Cycle.lean` (transitivity from `(2_P)` and the
three cycle-shortening patterns). There is currently no completed
`Preference/LinearProof.lean` replacing the direct proof.

For probability, `IsSignedCharge` intentionally drops normalization and
nonnegativity. This separates Scott's p. 15 signed-measure statement from
Theorem 4.1, whose conclusion remains a normalized nonnegative probability.
Likewise, `DeFinettiAxioms` records de Finetti's literal weak nontriviality
condition `¬ R ⊥ ⊤`, not Scott's stronger conjunction
`R ⊤ ⊥ ∧ ¬ R ⊥ ⊤`.

## 4. Source materials

- PDF: [`sources/ScottMeasurement1964.pdf`](sources/ScottMeasurement1964.pdf)
- Working vision transcription (once generated):
  [`sources/ScottMeasurement1964_vision.md`](sources/ScottMeasurement1964_vision.md)

See `NOTICE` and `sources/README.md` for copyright carve-outs.

## 5. Build

```bash
lake exe cache get
lake build
bash scripts/palomar_preflight.sh
```

## 6. Palomar packaging

| File | Role |
|---|---|
| `Challenge.lean` | Statement of record (Mathlib only; deliberate `sorry`) |
| `Solution.lean` | Imports sorry-free `Scott1964/*` |
| `comparator.json` | Compared theorem and definition names |
| `formalization.yaml` | formalization.yaml v0.4 |

---

<!-- AI_MODEL_REFERENCES -->
<!-- /AI_MODEL_REFERENCES -->
