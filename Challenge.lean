/-
Copyright (c) 2026 Lars Warren Ericson. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Lars Warren Ericson.
-/

import Mathlib

/-!
# Scott 1964: statement of record

This Mathlib-only module states Scott's eight published theorems 1.1--1.4,
2.1, 3.1, 3.2, and 4.1. It also records a separately labelled modern
reconstruction of the infinite probability result mentioned, but not stated
or proved, in Scott's closing paragraph.

The deliberate `sorry`s are the Palomar challenge holes. `Solution.lean`
re-exports the sorry-free development with matching declarations.
-/

open Set

namespace Scott1964.MeasurementStructures.LinearInequalities

variable {L : Type*} [AddCommGroup L] [Module ℝ L]

def Symmetric (X : Set L) : Prop := ∀ ⦃x⦄, x ∈ X → -x ∈ X

def Realizable (X N : Set L) : Prop :=
  ∃ φ : Module.Dual ℝ L, ∀ x ∈ X, x ∈ N ↔ 0 ≤ φ x

def SignComplete (X N : Set L) : Prop :=
  ∀ ⦃x⦄, x ∈ X → x ∈ N ∨ -x ∈ N

def WeightedSequenceCancellation (X N : Set L) : Prop :=
  ∀ (n : ℕ) (x : Fin (n + 1) → L) (c : Fin (n + 1) → ℝ),
    (∀ i, x i ∈ X) → (∀ i, x i ∈ N) → (∀ i, 0 < c i) →
    ∑ i, c i • x i = 0 → ∀ i, -x i ∈ N

def UnweightedSequenceCancellation (X N : Set L) : Prop :=
  ∀ (n : ℕ) (x : Fin (n + 1) → L),
    (∀ i, x i ∈ X) → (∀ i, x i ∈ N) →
    ∑ i, x i = 0 → ∀ i, -x i ∈ N

def IsRationalVector {S : Type*} (x : S → ℝ) : Prop :=
  ∀ s, ∃ q : ℚ, x s = q

def IsRationalSet {S : Type*} (X : Set (S → ℝ)) : Prop :=
  ∀ ⦃x⦄, x ∈ X → IsRationalVector x

def RelationRealizable (Y : Set L) (R : L → L → Prop) : Prop :=
  ∃ φ : Module.Dual ℝ L, ∀ x ∈ Y, ∀ y ∈ Y, R x y ↔ φ y ≤ φ x

def RelationComplete (Y : Set L) (R : L → L → Prop) : Prop :=
  ∀ ⦃x⦄, x ∈ Y → ∀ ⦃y⦄, y ∈ Y → R x y ∨ R y x

def RelationSequenceCancellation (Y : Set L) (R : L → L → Prop) : Prop :=
  ∀ (n : ℕ) (x y : Fin (n + 1) → L),
    (∀ i, x i ∈ Y) → (∀ i, y i ∈ Y) → (∀ i, R (x i) (y i)) →
    ∑ i, x i = ∑ i, y i → ∀ i, R (y i) (x i)

def additiveClosure (Y : Set L) : Set L :=
  AddSubmonoid.closure Y

structure StrictlyMonotonic (Z : Set L) (R : L → L → Prop) : Prop where
  complete : ∀ ⦃x⦄, x ∈ Z → ∀ ⦃y⦄, y ∈ Z → R x y ∨ R y x
  add : ∀ ⦃x₀ y₀ x₁ y₁⦄, x₀ ∈ Z → y₀ ∈ Z → x₁ ∈ Z → y₁ ∈ Z →
    R x₀ y₀ → R x₁ y₁ → R (x₀ + x₁) (y₀ + y₁)
  cancel : ∀ ⦃x₀ y₀ x₁ y₁⦄, x₀ ∈ Z → y₀ ∈ Z → x₁ ∈ Z → y₁ ∈ Z →
    x₀ + x₁ = y₀ + y₁ → R x₁ y₁ → R y₀ x₀

def ExtendsOn (Y Z : Set L) (R Rplus : L → L → Prop) : Prop :=
  Y ⊆ Z ∧ ∀ ⦃x⦄, x ∈ Y → ∀ ⦃y⦄, y ∈ Y → (Rplus x y ↔ R x y)

end Scott1964.MeasurementStructures.LinearInequalities

namespace Scott1964.MeasurementStructures.LinearInequalities

variable {L : Type*} [NormedAddCommGroup L] [NormedSpace ℝ L]
  [FiniteDimensional ℝ L]

theorem scott_theorem_1_1 {X N : Set L} (hX : X.Finite) (hsym : Symmetric X) :
    Realizable X N ↔ SignComplete X N ∧ WeightedSequenceCancellation X N := by
  sorry

theorem scott_theorem_1_2 {S : Type*} [Fintype S] {X N : Set (S → ℝ)}
    (hX : X.Finite) (hrat : IsRationalSet X) (hsym : Symmetric X) :
    Realizable X N ↔ SignComplete X N ∧ UnweightedSequenceCancellation X N := by
  sorry

theorem scott_theorem_1_3 {S : Type*} [Fintype S]
    {Y : Set (S → ℝ)} {R : (S → ℝ) → (S → ℝ) → Prop}
    (hY : Y.Finite) (hYrat : IsRationalSet Y) :
    RelationRealizable Y R ↔
      RelationComplete Y R ∧ RelationSequenceCancellation Y R := by
  sorry

theorem scott_theorem_1_4 {S : Type*} [Fintype S]
    {Y : Set (S → ℝ)} {R : (S → ℝ) → (S → ℝ) → Prop}
    (hY : Y.Finite) (hYrat : IsRationalSet Y) :
    RelationRealizable Y R ↔
      ∃ Rplus : (S → ℝ) → (S → ℝ) → Prop,
        ExtendsOn Y (additiveClosure Y) R Rplus ∧
        StrictlyMonotonic (additiveClosure Y) Rplus := by
  sorry

end Scott1964.MeasurementStructures.LinearInequalities

namespace Scott1964.MeasurementStructures

open scoped Classical

def RealizablePreference {A : Type u} (P : A → A → Prop) : Prop :=
  ∃ f : A → ℝ, ∀ x y, P x y ↔ f x ≥ f y + 1

def PrefIrrefl {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x, ¬P x x

def PrefQuadA {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x y z w, P x y → P z w → P x w ∨ P z y

def PrefQuadB {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x y z w, P x y → P z x → P w y ∨ P z w

theorem theorem_2_1 {A : Type u} [Fintype A] [Nonempty A] (P : A → A → Prop) :
    RealizablePreference P ↔ PrefIrrefl P ∧ PrefQuadA P ∧ PrefQuadB P := by
  sorry

def RealizableUtilityPair {A : Type u} {A' : Type v}
    (V : A → A' → A → A' → Prop) : Prop :=
  ∃ f : A → ℝ, ∃ f' : A' → ℝ,
    ∀ x x' y y', V x x' y y' ↔ f x + f' x' ≥ f y + f' y'

def PairTotal {A : Type u} {A' : Type v}
    (V : A → A' → A → A' → Prop) : Prop :=
  ∀ x x' y y', V x x' y y' ∨ V y y' x x'

def PairPermutation {A : Type u} {A' : Type v}
    (V : A → A' → A → A' → Prop) : Prop :=
  ∀ (n : ℕ) (x : Fin (n + 1) → A) (x' : Fin (n + 1) → A')
    (π σ : Equiv.Perm (Fin (n + 1))),
    (∀ i, i ≠ 0 → V (x i) (x' i) (x (π i)) (x' (σ i))) →
      V (x (π 0)) (x' (σ 0)) (x 0) (x' 0)

theorem theorem_3_1 {A : Type u} {A' : Type v}
    [Fintype A] [Nonempty A] [Fintype A'] [Nonempty A']
    (V : A → A' → A → A' → Prop) :
    RealizableUtilityPair V ↔ PairTotal V ∧ PairPermutation V := by
  sorry

def RealizableDifference {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∃ f : A → ℝ, ∀ x y z w, D x y z w ↔ f x - f y ≥ f z - f w

def DiffTotal {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ x y z w, D x y z w ∨ D z w x y

def DiffPermutation {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ (n : ℕ) (x y : Fin (n + 1) → A) (π σ : Equiv.Perm (Fin (n + 1))),
    (∀ i, i ≠ 0 → D (x i) (y i) (x (π i)) (y (σ i))) →
      D (x (π 0)) (y (σ 0)) (x 0) (y 0)

def DiffReversal {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ x y z w, D x y z w → D w z y x

theorem theorem_3_2 {A : Type u} [Fintype A] [Nonempty A]
    (D : A → A → A → A → Prop) :
    RealizableDifference D ↔ DiffTotal D ∧ DiffPermutation D ∧ DiffReversal D := by
  sorry

structure IsProbability {B : Type u} [BooleanAlgebra B] (μ : B → ℝ) : Prop where
  bot : μ ⊥ = 0
  top : μ ⊤ = 1
  additive : ∀ x y, Disjoint x y → μ (x ⊔ y) = μ x + μ y
  nonnegative : ∀ x, 0 ≤ μ x

def IsNonnegative {B : Type u} [BooleanAlgebra B] (μ : B → ℝ) : Prop :=
  ∀ x, 0 ≤ μ x

def IsFinitelyAdditiveProbability {B : Type u} [BooleanAlgebra B] (μ : B → ℝ) : Prop :=
  IsProbability μ

theorem IsProbability.compl {B : Type u} [BooleanAlgebra B] {μ : B → ℝ}
    (hμ : IsProbability μ) (x : B) : μ xᶜ = 1 - μ x := by
  sorry

theorem IsProbability.mono_of_nonnegative {B : Type u} [BooleanAlgebra B]
    {μ : B → ℝ} (hμ : IsProbability μ) (hn : IsNonnegative μ)
    ⦃x y : B⦄ (hxy : x ≤ y) : μ x ≤ μ y := by
  sorry

theorem IsProbability.mono {B : Type u} [BooleanAlgebra B]
    {μ : B → ℝ} (hμ : IsProbability μ) ⦃x y : B⦄ (hxy : x ≤ y) :
    μ x ≤ μ y := by
  sorry

theorem IsProbability.le_one_of_nonnegative {B : Type u} [BooleanAlgebra B]
    {μ : B → ℝ} (hμ : IsProbability μ) (hn : IsNonnegative μ) (x : B) :
    μ x ≤ 1 := by
  sorry

theorem IsProbability.le_one {B : Type u} [BooleanAlgebra B]
    {μ : B → ℝ} (hμ : IsProbability μ) (x : B) : μ x ≤ 1 := by
  sorry

def RealizableProbability {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∃ μ : B → ℝ, IsProbability μ ∧ ∀ x y, R x y ↔ μ x ≥ μ y

def StrictlyPreferred {B : Type u} (R : B → B → Prop) (x y : B) : Prop :=
  ¬R y x

def ProbNontrivial {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  R ⊤ ⊥ ∧ ¬R ⊥ ⊤

def ProbNonneg {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∀ x, R x ⊥

def ProbTotal {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∀ x y, R x y ∨ R y x

def ProbCancellation {B : Type u} [BooleanAlgebra B] [Fintype B]
    (R : B → B → Prop) : Prop :=
  ∀ (n : ℕ) (x y : Fin (n + 1) → B),
    (∀ a : B, IsAtom a →
        (∑ i, if a ≤ x i then 1 else 0) =
          (∑ i, if a ≤ y i then 1 else 0 : ℕ)) →
      (∀ i, i ≠ 0 → R (x i) (y i)) → R (y 0) (x 0)

theorem theorem_4_1 {B : Type u} [BooleanAlgebra B] [Fintype B]
    (R : B → B → Prop) :
    RealizableProbability R ↔
      ProbNontrivial R ∧ ProbNonneg R ∧ ProbTotal R ∧ ProbCancellation R := by
  sorry

end Scott1964.MeasurementStructures

namespace Scott1964.MeasurementStructures.Probability.Infinite

open scoped BoundedContinuousFunction
open Set

noncomputable section

universe u

variable (B : Type u) [BooleanAlgebra B]

def ProbabilityPoint :=
  {μ : B → ℝ // IsFinitelyAdditiveProbability μ}

instance : TopologicalSpace (ProbabilityPoint B) := ⊥

instance : DiscreteTopology (ProbabilityPoint B) := ⟨rfl⟩

theorem probabilityPoint_nonnegative (p : ProbabilityPoint B) (a : B) :
    0 ≤ p.1 a :=
  p.2.nonnegative a

theorem probabilityPoint_le_one (p : ProbabilityPoint B) (a : B) :
    p.1 a ≤ 1 :=
  p.2.le_one a

def eventVector (a : B) : ProbabilityPoint B →ᵇ ℝ :=
  BoundedContinuousFunction.mkOfDiscrete (fun p => p.1 a) 1 (by
    intro p q
    rw [Real.dist_eq]
    rw [abs_sub_le_iff]
    constructor <;>
      linarith [probabilityPoint_nonnegative B p a,
        probabilityPoint_nonnegative B q a,
        probabilityPoint_le_one B p a,
        probabilityPoint_le_one B q a])

def EventSpan : Submodule ℝ (ProbabilityPoint B →ᵇ ℝ) :=
  Submodule.span ℝ (Set.range (eventVector B))

def event (a : B) : EventSpan B :=
  ⟨eventVector B a, Submodule.subset_span (Set.mem_range_self a)⟩

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [LocallyConvexSpace ℝ E]

def ConeUpperSet (C : ProperCone ℝ E) (K : Set E) : Prop :=
  ∀ ⦃x c⦄, x ∈ K → c ∈ C → x + c ∈ K

structure KelleyCover (C : ProperCone ℝ E) (S : Set E) where
  layer : ℕ → Set E
  strictInCone : S ⊆ C
  covers : S ⊆ ⋃ n, layer n
  convex : ∀ n, Convex ℝ (layer n)
  closed : ∀ n, IsClosed (layer n)
  avoidsZero : ∀ n, (0 : E) ∉ layer n
  upper : ∀ n, ConeUpperSet C (layer n)

variable {B : Type u} [BooleanAlgebra B]

def comparisonVector (B : Type u) [BooleanAlgebra B] (x y : B) : EventSpan B :=
  event B x - event B y

def weakComparisonCone (R : B → B → Prop) : ProperCone ℝ (EventSpan B) :=
  ⨅ (L : StrongDual ℝ (EventSpan B))
    (_hL : ∀ x y, R x y → 0 ≤ L (comparisonVector B x y)),
      (ProperCone.positive ℝ ℝ).comap L

def strictComparisonSet (R : B → B → Prop) : Set (EventSpan B) :=
  {v | ∃ x y, StrictlyPreferred R x y ∧ v = comparisonVector B x y}

def GeneralizedKelleyCondition (R : B → B → Prop) : Prop :=
  Nonempty (KelleyCover (weakComparisonCone R) (strictComparisonSet R))

theorem reconstructed_infinite_theorem_4_1 (R : B → B → Prop) :
    RealizableProbability R ↔
      ProbNontrivial R ∧ ProbNonneg R ∧ ProbTotal R ∧
        GeneralizedKelleyCondition R := by
  sorry

end

end Scott1964.MeasurementStructures.Probability.Infinite
