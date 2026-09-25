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

The characterizations below all have the same orientation: the left side says
that one real-valued numerical model represents the qualitative relation
exactly; the right side lists the qualitative conditions equivalent to the
existence of that model. In particular:

* Theorems 1.1 and 1.2 characterize a prescribed nonnegative sign pattern by
  sign completeness and weighted or repeated-summand cancellation.
* Theorem 1.3 characterizes a complete relation by equal-sum sequence
  cancellation, and Theorem 1.4 gives the equivalent extension to an additive
  closure with addition and cancellation laws.
* Theorem 2.1 characterizes unit-threshold preference by irreflexivity and two
  four-alternative axioms.
* Theorems 3.1 and 3.2 characterize additive pair utility and ordered utility
  differences by totality, independent-permutation cancellation, and, for
  differences, reversal.
* Theorem 4.1 characterizes finite probability representation by
  nontriviality, bottom-minimality, totality, and atom-count cancellation.
* The final theorem adapts Kelley's 1959 countable-cover/separation method and
  uses Mathlib's modern locally convex separation theory. It is more explicit
  than the bare existence announcement in Scott's last paragraph, and is not
  attributed to Scott as a published or recoverable theorem. Based on the
  literature audit in the report, Section 3.5.10, this characterization
  provides the first explicit, self-contained realization of Scott's
  announced infinite extension in the published literature.

The deliberate `sorry`s are the Palomar challenge holes. `Solution.lean`
re-exports the sorry-free development with matching declarations.
-/

open Set

namespace Scott1964.MeasurementStructures.LinearInequalities

variable {L : Type*} [AddCommGroup L] [Module ℝ L]

def Symmetric (X : Set L) : Prop := ∀ ⦃x⦄, x ∈ X → -x ∈ X

/-- A sign assignment `N ⊆ X` is realizable when one linear functional is
nonnegative exactly on the vectors declared to lie in `N`. -/
def Realizable (X N : Set L) : Prop :=
  ∃ φ : Module.Dual ℝ L, ∀ x ∈ X, x ∈ N ↔ 0 ≤ φ x

/-- Every vector in the symmetric test set has at least one declared weak sign:
the vector itself or its negative lies in `N`. -/
def SignComplete (X N : Set L) : Prop :=
  ∀ ⦃x⦄, x ∈ X → x ∈ N ∨ -x ∈ N

/-- Weighted cancellation says that if declared-nonnegative vectors with
strictly positive real weights sum to zero, then every summand is neutral:
its negative is declared nonnegative too. -/
def WeightedSequenceCancellation (X N : Set L) : Prop :=
  ∀ (n : ℕ) (x : Fin (n + 1) → L) (c : Fin (n + 1) → ℝ),
    (∀ i, x i ∈ X) → (∀ i, x i ∈ N) → (∀ i, 0 < c i) →
    ∑ i, c i • x i = 0 → ∀ i, -x i ∈ N

/-- Unweighted cancellation is the same zero-sum test with unit coefficients;
repetition of a vector supplies positive integer multiplicity. -/
def UnweightedSequenceCancellation (X N : Set L) : Prop :=
  ∀ (n : ℕ) (x : Fin (n + 1) → L),
    (∀ i, x i ∈ X) → (∀ i, x i ∈ N) →
    ∑ i, x i = 0 → ∀ i, -x i ∈ N

def IsRationalVector {S : Type*} (x : S → ℝ) : Prop :=
  ∀ s, ∃ q : ℚ, x s = q

def IsRationalSet {S : Type*} (X : Set (S → ℝ)) : Prop :=
  ∀ ⦃x⦄, x ∈ X → IsRationalVector x

/-- A relation is realizable when one linear functional represents it exactly
as weak numerical comparison on `Y`. -/
def RelationRealizable (Y : Set L) (R : L → L → Prop) : Prop :=
  ∃ φ : Module.Dual ℝ L, ∀ x ∈ Y, ∀ y ∈ Y, R x y ↔ φ y ≤ φ x

/-- Every two members of `Y` are comparable by `R`. -/
def RelationComplete (Y : Set L) (R : L → L → Prop) : Prop :=
  ∀ ⦃x⦄, x ∈ Y → ∀ ⦃y⦄, y ∈ Y → R x y ∨ R y x

/-- Relational cancellation says that termwise comparisons between two finite
sequences with equal vector sums must all be ties: every comparison also holds
in reverse. -/
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

theorem fin_succ_pos (n : ℕ) : 0 < n + 1 :=
  Nat.succ_pos n

def finHead (n : ℕ) : Fin (n + 1) :=
  ⟨0, fin_succ_pos n⟩

theorem finHead_eq_zero (n : ℕ) : finHead n = 0 :=
  Fin.ext rfl

/-- A preference relation is realizable when one score function represents it
exactly as a gap of at least one unit. -/
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

/-- A mixed-pair relation is realizable when two utility functions represent
it exactly by comparing their additive scores. -/
def RealizableUtilityPair {A : Type u} {A' : Type v}
    (V : A → A' → A → A' → Prop) : Prop :=
  ∃ f : A → ℝ, ∃ f' : A' → ℝ,
    ∀ x x' y y', V x x' y y' ↔ f x + f' x' ≥ f y + f' y'

/-- Every two mixed pairs are comparable. -/
def PairTotal {A : Type u} {A' : Type v}
    (V : A → A' → A → A' → Prop) : Prop :=
  ∀ x x' y y', V x x' y y' ∨ V y y' x x'

/-- Pair-permutation cancellation independently permutes the first and second
coordinates of a finite list of pairs. If every comparison except the
distinguished one goes from the original pair to its permuted pair, the
remaining comparison must go in the reverse direction. -/
def PairPermutation {A : Type u} {A' : Type v}
    (V : A → A' → A → A' → Prop) : Prop :=
  ∀ (n : ℕ) (x : Fin (n + 1) → A) (x' : Fin (n + 1) → A')
    (π σ : Equiv.Perm (Fin (n + 1))),
    (∀ i, i ≠ finHead n → V (x i) (x' i) (x (π i)) (x' (σ i))) →
      V (x (π (finHead n))) (x' (σ (finHead n))) (x (finHead n)) (x' (finHead n))

theorem theorem_3_1 {A : Type u} {A' : Type v}
    [Fintype A] [Nonempty A] [Fintype A'] [Nonempty A']
    (V : A → A' → A → A' → Prop) :
    RealizableUtilityPair V ↔ PairTotal V ∧ PairPermutation V := by
  sorry

/-- A difference relation is realizable when one utility function represents
it exactly by comparing `f x - f y` with `f z - f w`. -/
def RealizableDifference {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∃ f : A → ℝ, ∀ x y z w, D x y z w ↔ f x - f y ≥ f z - f w

def DiffTotal {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ x y z w, D x y z w ∨ D z w x y

/-- Difference-permutation cancellation applies the same distinguished-term
rule after independently permuting the left and right entries of a finite
list of ordered pairs. -/
def DiffPermutation {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ (n : ℕ) (x y : Fin (n + 1) → A) (π σ : Equiv.Perm (Fin (n + 1))),
    (∀ i, i ≠ finHead n → D (x i) (y i) (x (π i)) (y (σ i))) →
      D (x (π (finHead n))) (y (σ (finHead n))) (x (finHead n)) (y (finHead n))

/-- Reversal says that if the difference from `y` to `x` is at least that from
`w` to `z`, then the oppositely oriented second difference is at least the
oppositely oriented first one. -/
def DiffReversal {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ x y z w, D x y z w → D w z y x

theorem theorem_3_2 {A : Type u} [Fintype A] [Nonempty A]
    (D : A → A → A → A → Prop) :
    RealizableDifference D ↔ DiffTotal D ∧ DiffPermutation D ∧ DiffReversal D := by
  sorry

/-- A finite-additive probability is zero at bottom, one at top, additive on
disjoint joins, and nonnegative on every event. -/
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
  have hd : Disjoint x xᶜ := disjoint_compl_right
  have h := hμ.additive x xᶜ hd
  rw [sup_compl_eq_top, hμ.top] at h
  linarith

theorem IsProbability.mono_of_nonnegative {B : Type u} [BooleanAlgebra B]
    {μ : B → ℝ} (hμ : IsProbability μ) (hn : IsNonnegative μ)
    ⦃x y : B⦄ (hxy : x ≤ y) : μ x ≤ μ y := by
  have hd : Disjoint x (y \ x) := by
    rw [disjoint_iff_inf_le]
    simp
  have hy : x ⊔ (y \ x) = y := by
    exact sup_sdiff_cancel_right hxy
  rw [← hy, hμ.additive _ _ hd]
  exact le_add_of_nonneg_right (hn _)

theorem IsProbability.mono {B : Type u} [BooleanAlgebra B]
    {μ : B → ℝ} (hμ : IsProbability μ) ⦃x y : B⦄ (hxy : x ≤ y) :
    μ x ≤ μ y :=
  hμ.mono_of_nonnegative hμ.nonnegative hxy

theorem IsProbability.le_one_of_nonnegative {B : Type u} [BooleanAlgebra B]
    {μ : B → ℝ} (hμ : IsProbability μ) (hn : IsNonnegative μ) (x : B) :
    μ x ≤ 1 := by
  simpa [hμ.top] using hμ.mono_of_nonnegative hn (show x ≤ (⊤ : B) from le_top)

theorem IsProbability.le_one {B : Type u} [BooleanAlgebra B]
    {μ : B → ℝ} (hμ : IsProbability μ) (x : B) : μ x ≤ 1 :=
  hμ.le_one_of_nonnegative hμ.nonnegative x

/-- A qualitative event relation is realizable when one finitely additive
probability represents it exactly by numerical comparison. -/
def RealizableProbability {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∃ μ : B → ℝ, IsProbability μ ∧ ∀ x y, R x y ↔ μ x ≥ μ y

def StrictlyPreferred {B : Type u} (R : B → B → Prop) (x y : B) : Prop :=
  ¬R y x

/-- The certain event is weakly above the impossible event, but not conversely. -/
def ProbNontrivial {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  R ⊤ ⊥ ∧ ¬R ⊥ ⊤

/-- Every event is weakly above the impossible event. -/
def ProbNonneg {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∀ x, R x ⊥

/-- Every two events are comparable. -/
def ProbTotal {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∀ x y, R x y ∨ R y x

/-- Finite probability cancellation compares two event lists in which each
atom occurs equally often. If all non-distinguished comparisons go from the
left list to the right, the distinguished comparison must reverse. -/
def ProbCancellation {B : Type u} [BooleanAlgebra B] [Fintype B]
    (R : B → B → Prop) : Prop :=
  ∀ (n : ℕ) (x y : Fin (n + 1) → B),
    (∀ a : B, IsAtom a →
        (∑ i, if a ≤ x i then 1 else 0) =
          (∑ i, if a ≤ y i then 1 else 0 : ℕ)) →
      (∀ i, i ≠ finHead n → R (x i) (y i)) → R (y (finHead n)) (x (finHead n))

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

noncomputable instance instBoundedAddReal : BoundedAdd ℝ := inferInstance

def ProbabilityPoint :=
  {μ : B → ℝ // IsFinitelyAdditiveProbability μ}

instance instTopologicalSpaceProbabilityPoint : TopologicalSpace (ProbabilityPoint B) := ⊥

theorem probabilityPoint_discrete_eq_bot :
    instTopologicalSpaceProbabilityPoint B = ⊥ :=
  rfl

instance instDiscreteTopologyProbabilityPoint : DiscreteTopology (ProbabilityPoint B) where
  eq_bot := probabilityPoint_discrete_eq_bot B

noncomputable instance instAddCommMonoidProbabilityBCF :
    AddCommMonoid (ProbabilityPoint B →ᵇ ℝ) := inferInstance

noncomputable instance instModuleProbabilityBCF :
    Module ℝ (ProbabilityPoint B →ᵇ ℝ) := inferInstance

noncomputable instance instAddCommGroupProbabilityBCF :
    AddCommGroup (ProbabilityPoint B →ᵇ ℝ) := inferInstance

theorem probabilityPoint_nonnegative (p : ProbabilityPoint B) (a : B) :
    0 ≤ p.1 a :=
  p.2.nonnegative a

theorem probabilityPoint_le_one (p : ProbabilityPoint B) (a : B) :
    p.1 a ≤ 1 :=
  p.2.le_one a

theorem eventVector_dist_le_one (a : B) (p q : ProbabilityPoint B) :
    dist (p.1 a) (q.1 a) ≤ 1 := by
  rw [Real.dist_eq, abs_sub_le_iff]
  constructor <;>
    linarith [probabilityPoint_nonnegative B p a,
      probabilityPoint_nonnegative B q a,
      probabilityPoint_le_one B p a,
      probabilityPoint_le_one B q a]

def eventVector (a : B) : ProbabilityPoint B →ᵇ ℝ :=
  BoundedContinuousFunction.mkOfDiscrete (fun p => p.1 a) 1
    (eventVector_dist_le_one B a)

def EventSpan : Submodule ℝ (ProbabilityPoint B →ᵇ ℝ) :=
  Submodule.span ℝ (Set.range (eventVector B))

noncomputable instance instNormedAddCommGroupEventSpan :
    NormedAddCommGroup (EventSpan B) := inferInstance

noncomputable instance instNormedSpaceEventSpan :
    NormedSpace ℝ (EventSpan B) := inferInstance

noncomputable instance instLocallyConvexSpaceEventSpan :
    LocallyConvexSpace ℝ (EventSpan B) := inferInstance

def event (a : B) : EventSpan B :=
  ⟨eventVector B a, Submodule.subset_span (Set.mem_range_self a)⟩

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [LocallyConvexSpace ℝ E]

def ConeUpperSet (C : ProperCone ℝ E) (K : Set E) : Prop :=
  ∀ ⦃x c⦄, x ∈ K → c ∈ C → x + c ∈ K

/-- A Kelley cover places the strict-comparison set inside the weak cone and
covers it by countably many closed convex sets. Every layer avoids zero and is
upper-closed under addition of vectors from the weak cone. -/
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

/-- The weak-comparison cone is the intersection of all continuous-dual closed
half-spaces that contain every declared weak-comparison vector. Equivalently,
a vector is in the cone when every continuous linear functional nonnegative
on all declared weak comparisons is also nonnegative on that vector. -/
def weakComparisonCone (R : B → B → Prop) : ProperCone ℝ (EventSpan B) :=
  ⨅ (L : StrongDual ℝ (EventSpan B))
    (_hL : ∀ x y, R x y → 0 ≤ L (comparisonVector B x y)),
      (ProperCone.positive ℝ ℝ).comap L

/-- The strict set consists of `event x - event y` whenever the reverse weak
comparison `R y x` fails. -/
def strictComparisonSet (R : B → B → Prop) : Set (EventSpan B) :=
  {v | ∃ x y, StrictlyPreferred R x y ∧ v = comparisonVector B x y}

/-- The generalized Kelley condition requires a countable Kelley cover of the
strict-comparison vectors above the closed weak-comparison cone. -/
def GeneralizedKelleyCondition (R : B → B → Prop) : Prop :=
  Nonempty (KelleyCover (weakComparisonCone R) (strictComparisonSet R))

theorem reconstructed_infinite_theorem_4_1 (R : B → B → Prop) :
    RealizableProbability R ↔
      ProbNontrivial R ∧ ProbNonneg R ∧ ProbTotal R ∧
        GeneralizedKelleyCondition R := by
  sorry

end

end Scott1964.MeasurementStructures.Probability.Infinite
