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

The repository is an early scaffold. `Challenge.lean` states the paper's three
headline representation theorems:

- `theorem_2_1`, Problem I (intransitive indifference): a binary relation `P`
  on a finite set is realizable as `f x ≥ f y + 1` exactly when it is
  irreflexive and satisfies Scott's two quadruple conditions.
- `theorem_3_2`, Problem II (ordered differences): a quaternary relation `D`
  is realizable by a single utility function exactly when it is complete,
  reversal-closed, and satisfies the infinite bundle of permutation
  conditions.
- `theorem_4_1`, Problem III (subjective probability): a qualitative ordering
  on a finite Boolean algebra is realizable by a probability measure exactly
  when it is nontrivial, nonnegative, complete, and satisfies Scott's
  cancellation condition.

Each is currently a deliberate `sorry`. The Palomar Comparator compares no
declaration until a proof lands under `Scott1964/MeasurementStructures/` and
is reached by `Solution.lean`.

## 2. Theorem inventory

Stated, unproved:

- §2: Theorem 2.1.
- §3: Theorem 3.2.
- §4: Theorem 4.1.

Not yet stated:

- §1: Theorems 1.1 and 1.2, the general and rational realizability criteria
  for a finite symmetric set of vectors; Theorem 1.3, realizability of a
  binary relation on a finite rational subset of `L(S)`; Theorem 1.4, the
  reformulation as extendability to a strictly monotonic relation on the
  additive closure `Y⁺`. These are the engine of every later proof and are
  the natural next milestone.
- §3: Theorem 3.1, realizability by a *pair* of utility functions on `A × A*`.

Out of scope:

- The extension of Theorem 4.1 to infinite Boolean algebras, which Scott
  mentions but does not prove in this paper.

## 3. Formalization notes

Scott's condition (4_B) is stated with the algebraic sum
`x₀ + x₁ + ⋯ + xₙ₋₁` of *characteristic functions*, not the Boolean join.
`Challenge.lean` renders this with the atom-counting reading Scott supplies in
words immediately after the theorem: every atom lies below exactly as many
`xᵢ` as `yᵢ`.

Condition (2_D) is, as Scott notes, an infinite bundle indexed by a length and
a pair of permutations; no finite subfamily suffices. It is formalized as a
universally quantified statement over `n : ℕ` and `Equiv.Perm (Fin (n + 1))`.

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
