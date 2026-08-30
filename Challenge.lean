import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Order.Atoms
import Mathlib.Data.Real.Basic

/-
Copyright (c) 2026  Lars Warren Ericson.  All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Lars Warren Ericson.
-/

/-!
# Scott 1964, the three measurement-representation theorems

Scott's paper applies the general solvability criterion for finite systems of
linear inequalities (§1) to three representation problems:

* Problem I, intransitive indifference — Theorem 2.1;
* Problem II, ordered differences — Theorem 3.2;
* Problem III, subjective probability — Theorem 4.1.

This file imports only Mathlib and states those three results with deliberate
`sorry`s. The sorry-free proofs are to live in
`Scott1964/MeasurementStructures/` and are compared via `Solution.lean`.

The statement of record is not yet fixed: `comparator.json` compares no
declaration until the corresponding proof lands in the Solution import graph.
See `PROVENANCE.md` and `arxiv.md`.
-/

namespace Scott1964.MeasurementStructures

open scoped Classical

/-! ## Problem I — intransitive indifference -/

/-- `P` is realizable when some utility `f` makes strict preference the
statement `f x ≥ f y + 1`. -/
def RealizablePreference {A : Type u} (P : A → A → Prop) : Prop :=
  ∃ f : A → ℝ, ∀ x y, P x y ↔ f x ≥ f y + 1

/-- Scott 1964, condition (1_P): irreflexivity. -/
def PrefIrrefl {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x, ¬ P x x

/-- Scott 1964, condition (2_P). -/
def PrefQuadA {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x y z w, P x y → P z w → P x w ∨ P z y

/-- Scott 1964, condition (3_P). -/
def PrefQuadB {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x y z w, P x y → P z x → P w y ∨ P z w

/-- **Scott 1964, Theorem 2.1 (intransitive indifference).** -/
theorem theorem_2_1 {A : Type u} [Fintype A] [Nonempty A] (P : A → A → Prop) :
    RealizablePreference P ↔ PrefIrrefl P ∧ PrefQuadA P ∧ PrefQuadB P := by
  sorry

/-! ## Problem II — ordered differences -/

/-- `D` is realizable when a single utility `f` makes `xy D zw` the statement
`f x - f y ≥ f z - f w`. -/
def RealizableDifference {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∃ f : A → ℝ, ∀ x y z w, D x y z w ↔ f x - f y ≥ f z - f w

/-- Scott 1964, condition (1_D): completeness. -/
def DiffTotal {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ x y z w, D x y z w ∨ D z w x y

/-- Scott 1964, condition (2_D): the infinite bundle of permutation
conditions, one for each length and each pair of permutations. -/
def DiffPermutation {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ (n : ℕ) (x y : Fin (n + 1) → A) (π σ : Equiv.Perm (Fin (n + 1))),
    (∀ i, i ≠ 0 → D (x i) (y i) (x (π i)) (y (σ i))) →
      D (x (π 0)) (y (σ 0)) (x 0) (y 0)

/-- Scott 1964, condition (3_D): reversal. -/
def DiffReversal {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ x y z w, D x y z w → D w z y x

/-- **Scott 1964, Theorem 3.2 (ordered differences).** -/
theorem theorem_3_2 {A : Type u} [Fintype A] [Nonempty A]
    (D : A → A → A → A → Prop) :
    RealizableDifference D ↔ DiffTotal D ∧ DiffPermutation D ∧ DiffReversal D := by
  sorry

/-! ## Problem III — subjective probability -/

/-- A finitely additive probability measure on a Boolean algebra. -/
structure IsProbability {B : Type u} [BooleanAlgebra B] (μ : B → ℝ) : Prop where
  bot : μ ⊥ = 0
  top : μ ⊤ = 1
  additive : ∀ x y, Disjoint x y → μ (x ⊔ y) = μ x + μ y

/-- `R` is realizable when some probability measure orders `B` the same way. -/
def RealizableProbability {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) :
    Prop :=
  ∃ μ : B → ℝ, IsProbability μ ∧ ∀ x y, R x y ↔ μ x ≥ μ y

/-- Scott 1964, condition (1_B): nontriviality. -/
def ProbNontrivial {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  R ⊤ ⊥ ∧ ¬ R ⊥ ⊤

/-- Scott 1964, condition (2_B): every event is at least null. -/
def ProbNonneg {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∀ x, R x ⊥

/-- Scott 1964, condition (3_B): comparability. -/
def ProbTotal {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∀ x y, R x y ∨ R y x

/-- Scott 1964, condition (4_B). The hypothesis is the *algebraic* identity
`x₀ + ⋯ + xₙ₋₁ = y₀ + ⋯ + yₙ₋₁` on characteristic functions, i.e. every atom
lies below exactly as many `xᵢ` as `yᵢ`. -/
def ProbCancellation {B : Type u} [BooleanAlgebra B] [Fintype B]
    (R : B → B → Prop) : Prop :=
  ∀ (n : ℕ) (x y : Fin (n + 1) → B),
    (∀ a : B, IsAtom a →
        (∑ i, if a ≤ x i then 1 else 0) = (∑ i, if a ≤ y i then 1 else 0 : ℕ)) →
      (∀ i, i ≠ 0 → R (x i) (y i)) → R (y 0) (x 0)

/-- **Scott 1964, Theorem 4.1 (subjective probability).** -/
theorem theorem_4_1 {B : Type u} [BooleanAlgebra B] [Fintype B]
    (R : B → B → Prop) :
    RealizableProbability R ↔
      ProbNontrivial R ∧ ProbNonneg R ∧ ProbTotal R ∧ ProbCancellation R := by
  sorry

end Scott1964.MeasurementStructures
