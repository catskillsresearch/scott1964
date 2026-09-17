#!/usr/bin/env python3
"""Emit source-faithful concordance cards into ``arxiv.md``.

Card metadata and reconstructions live here so that Scott quotations can be
copied from ``sources/ScottMeasurement1964_vision.md`` without drift.  The
published source of the cards is the marked region in ``arxiv.md``.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARXIV = ROOT / "arxiv.md"
SOURCE = ROOT / "sources" / "ScottMeasurement1964_vision.md"
BEGIN = "<!-- CONCORDANCE_BODY -->"
END = "<!-- /CONCORDANCE_BODY -->"


@dataclass(frozen=True)
class Card:
    card_id: str
    start: int
    end: int
    lean: str
    title: str
    lean_panel: str
    reconstruction: str


def quote_source(lines: list[str], start: int, end: int) -> str:
    quoted: list[str] = []
    for line in lines[start - 1 : end]:
        quoted.append("> " + line if line else ">")
    return "\n".join(quoted)


def emit_card(card: Card, lines: list[str]) -> str:
    return (
        f"<!-- scott-concordance: card={card.card_id} "
        f"source-lines={card.start}-{card.end} lean={card.lean} -->\n\n"
        f"**{card.title}.**\n\n"
        f"**Scott 1964 (verbatim).**\n\n"
        f"{quote_source(lines, card.start, card.end)}\n\n"
        f"**Lean 4 correspondence (exact source).**\n\n"
        f"{card.lean_panel.strip()}\n\n"
        f"**Mathematical reconstruction from Lean.**\n\n"
        f"{card.reconstruction.strip()}\n\n"
        f"<!-- /scott-concordance -->\n"
    )


def none_panel(nearest: str | None = None) -> str:
    if nearest:
        return (
            "No direct Lean counterpart. The nearest genuine formal object is "
            f"{nearest}."
        )
    return "No direct Lean counterpart."


NONE_RECON = (
    "This passage is historical, motivational, or bibliographic. There is no "
    "Lean definition or proof to reconstruct. The formal development begins "
    "only where a mathematical object, axiom, or theorem is isolated below."
)


def cards() -> list[Card]:
    return [
        *front_cards(),
        *section_i_cards(),
        *section_ii_cards(),
        *section_iii_cards(),
        *section_iv_cards(),
        *reference_cards(),
    ]


def front_cards() -> list[Card]:
    return [
        Card(
            "C-F01",
            7,
            10,
            "none",
            "Editorial transcription header",
            none_panel(),
            "The vision transcription begins with an editorial heading and a "
            "page marker. These are navigation aids for the formalization, not "
            "part of Scott's article, and they do not determine any Lean object.",
        ),
        Card(
            "C-F02",
            11,
            19,
            "none",
            "Journal heading, title, and author",
            none_panel(),
            "The published title identifies the paper formalized by the "
            "`Scott1964.MeasurementStructures` library. Lean records theorems "
            "and constructions, not the journal masthead.",
        ),
        Card(
            "C-F03",
            20,
            21,
            "none",
            "Scott's opening abstract",
            none_panel(
                "`Realizable`, `RealizablePreference`, `RealizableDifference`, "
                "and `RealizableProbability`"
            ),
            NONE_RECON
            + " The three examples announced here become Theorems 2.1, 3.1--3.2, "
            "and 4.1; the common solvability criterion becomes Theorems 1.1--1.4.",
        ),
        Card(
            "C-F04",
            22,
            23,
            "none",
            "Measurement as numerical assignment",
            none_panel(),
            NONE_RECON,
        ),
        Card(
            "C-F05",
            24,
            31,
            "RealizablePreference",
            "Problem I: intransitive indifference",
            """The numerical representation is exactly `RealizablePreference`.

```lean
def RealizablePreference {A : Type u} (P : A → A → Prop) : Prop :=
  ∃ f : A → ℝ, ∀ x y, P x y ↔ f x ≥ f y + 1
```""",
            "Scott asks when a finite strict relation $P$ is the unit-threshold "
            "cut of a real assignment. Lean packages that existence statement "
            "and nothing more: no axioms yet, and no construction of $f$. The "
            "constant $1$ is conventional; a later lemma rescales any positive "
            "threshold to this unit. The solution is `theorem_2_1`.",
        ),
        Card(
            "C-F06",
            32,
            39,
            "RealizableDifference",
            "Problem II: ordered differences",
            """```lean
def RealizableDifference {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∃ f : A → ℝ, ∀ x y z w, D x y z w ↔ f x - f y ≥ f z - f w
```""",
            "The quaternary comparison is a comparison of increments of one "
            "utility. Lean keeps Scott's four-argument order and the same "
            "difference inequality. The reduction through a pair of utilities "
            "appears only when Theorem 3.2 is proved.",
        ),
        Card(
            "C-F07",
            40,
            47,
            "RealizableProbability,IsProbability",
            "Problem III: subjective probability",
            """```lean
def RealizableProbability {B : Type u} [BooleanAlgebra B] (R : B → B → Prop) : Prop :=
  ∃ μ : B → ℝ, IsProbability μ ∧ ∀ x y, R x y ↔ μ x ≥ μ y
```""",
            "A qualitative comparison of events is realized when some finitely "
            "additive, nonnegative, normalized set function reproduces it. "
            "`IsProbability` forces $\\mu(\\bot)=0$, $\\mu(\\top)=1$, additivity "
            "on disjoint events, and nonnegativity. Scott's Boolean algebra is "
            "an abstract finite `BooleanAlgebra`, not a hardcoded powerset.",
        ),
        Card(
            "C-F08",
            48,
            53,
            "theorem_2_1,PrefIrrefl",
            "History and motivation for Problem I",
            none_panel("`theorem_2_1` and the Scott--Suppes staircase in `Preference/Direct.lean`"),
            "Lean does not formalize Luce's 1956 partial solution or the "
            "prose claim that indifference is often intransitive. What it does "
            "record is the completed representation theorem and the observation "
            "that a realizing $f$ forces irreflexivity. The printed 1964 cycle "
            "argument is only partly formalized; the checked converse uses the "
            "1958 staircase construction rather than Section I cancellation.",
        ),
        Card(
            "C-F09",
            54,
            55,
            "deFinetti_axioms_insufficient,theorem_4_1",
            "Problem III and the Kraft--Pratt--Seidenberg paper",
            """Scott's re-derivation is `theorem_4_1`. The 1959 insufficiency
result is the integrated counterexample

```lean
theorem deFinetti_axioms_insufficient :
    DeFinettiAxioms KPSGe ∧ ¬RealizableProbability KPSGe
```""",
            "The formal library separates two claims that Scott mentions together. "
            "Theorem 4.1 is the correct finite criterion, obtained from Theorem "
            "1.3 on atom vectors. The KPS order shows that de Finetti's five "
            "older axioms do not imply that criterion. There is no separate Lean "
            "theorem named “KPS Theorem 2”; Scott's strengthening is the object "
            "that was formalized.",
        ),
        Card(
            "C-F10",
            56,
            57,
            "theorem_3_1,theorem_4_1",
            "Priority remark on Problem II",
            none_panel("`theorem_3_1` and `theorem_4_1`"),
            "Adams's unpublished report is not formalized. Lean proves the "
            "theorems Scott states, not the historical priority claim. The "
            "methodological promise—that the general inequality criterion "
            "discovers the axioms—is realized for Theorems 3.1 and 4.1, which "
            "do route through Theorem 1.3, and is not yet realized for Theorem 2.1.",
        ),
    ]


def section_i_cards() -> list[Card]:
    return [
        Card(
            "C-I01",
            58,
            63,
            "Symmetric,Realizable",
            "Symmetric sets and realizable sign patterns",
            """```lean
def Symmetric (X : Set L) : Prop := ∀ ⦃x⦄, x ∈ X → -x ∈ X

def Realizable (X N : Set L) : Prop :=
  ∃ φ : Module.Dual ℝ L, ∀ x ∈ X, x ∈ N ↔ 0 ≤ φ x
```""",
            "Scott works in a finite-dimensional real vector space; Lean uses "
            "a module $L$ over $\\mathbb{R}$, later specialized to a "
            "finite-dimensional normed space when separation is invoked. "
            "Symmetry is closure under negation. Realizability is the existence "
            "of one linear functional whose nonnegative half-space cuts $X$ "
            "exactly along $N$. The zero functional realizes the case $N=X$, "
            "which Lean does not isolate as a named lemma.",
        ),
        Card(
            "C-I02",
            64,
            67,
            "strictPositive,indifferent,SignComplete",
            "Sign notation and the half-space remark",
            """```lean
def strictPositive (X N : Set L) : Set L :=
  {x | x ∈ X ∧ x ∈ N ∧ -x ∉ N}

def indifferent (X N : Set L) : Set L :=
  {x | x ∈ X ∧ x ∈ N ∧ -x ∈ N}

def SignComplete (X N : Set L) : Prop :=
  ∀ ⦃x⦄, x ∈ X → x ∈ N ∨ -x ∈ N
```""",
            "Scott's suggestive notation $x\\ge 0$ is membership in $N$. The "
            "strict vectors are those with only one weak sign; the indifferent "
            "vectors carry both. Sign completeness is condition (1). The "
            "half-space paragraph is exposition: `Realizable` already permits "
            "a trivial functional, and the later separation lemma produces a "
            "functional that is strictly positive on the strict set and zero "
            "on the indifferent span.",
        ),
        Card(
            "C-I03",
            68,
            75,
            "scott_theorem_1_1,SignComplete,WeightedSequenceCancellation",
            "Theorem 1.1",
            """```lean
theorem scott_theorem_1_1 {X N : Set L}
    (hX : X.Finite) (hsym : Symmetric X) :
    Realizable X N ↔
      SignComplete X N ∧ WeightedSequenceCancellation X N
```""",
            "Condition (2) is a positive-weight dependence among members of "
            "$N$ that sums to zero. Lean concludes that every summand is "
            "indifferent, which is stronger than Scott's displayed $x_0\\le 0$ "
            "but is the form used in the convex-hull contradiction. Sequences "
            "are indexed by `Fin (n+1)` so the distinguished term always exists. "
            "The geometric shadow of (2) is `WeightedCancellation`: the convex "
            "hull of strict vectors misses the span of indifferent vectors.",
        ),
        Card(
            "C-I04",
            76,
            77,
            "Realizable.weightedSequenceCancellation",
            "Necessity in Theorem 1.1",
            """```lean
theorem Realizable.weightedSequenceCancellation {X N : Set L}
    (h : Realizable X N) (hsym : Symmetric X) :
    WeightedSequenceCancellation X N
```""",
            "If $\\varphi$ realizes $N$, a positive combination of members of "
            "$N$ is sent to a nonnegative number. When that combination is the "
            "zero vector, each summand must have $\\varphi$-value zero and "
            "therefore, by realization, must also lie in $-N$. Sign completeness "
            "is the same dichotomy applied to a single vector: $\\varphi(x)$ is "
            "either nonnegative or its negative is.",
        ),
        Card(
            "C-I05",
            78,
            85,
            "weightedCancellation_of_sequence,finite_strict_separation,scott_theorem_1_1",
            "Sufficiency: cones, polyhedra, and separation",
            """Scott's $P$ and $Q$ become the convex hull of the strict set and
the span of the indifferent set. The checked separation lemma is Mathlib's
compact-closed Hahn--Banach theorem, specialized to a finite hull:

```lean
theorem finite_strict_separation {A B : Set L} (hA : A.Finite) :
    Disjoint (convexHull ℝ A) (Submodule.span ℝ B : Set L) ↔
      ∃ φ : Module.Dual ℝ L,
        (∀ x ∈ A, 0 < φ x) ∧ ∀ x ∈ B, φ x = 0
```""",
            "The printed argument cites Kuhn--Tucker. Lean does not cite that "
            "page; it invokes `geometric_hahn_banach_compact_closed` on the "
            "compact convex hull of a finite strict set and the closed "
            "finite-dimensional span of the indifferent set. The resulting "
            "continuous functional is flipped in sign so that it is strictly "
            "positive on every strict vector and identically zero on the "
            "indifferent subspace. Sign completeness then upgrades this "
            "geometric separator to a realizing functional for $N$.",
        ),
        Card(
            "C-I06",
            86,
            97,
            "weightedCancellation_of_sequence",
            "The intersection contradiction in Theorem 1.1",
            """The rewrite of a hypothetical point of $P\\cap Q$ as one positive
dependence is `weightedCancellation_of_sequence` in
`LinearInequalities/ScottTheorems.lean`.""",
            "Suppose a vector lies in both the convex hull of strict vectors "
            "and the linear span of indifferent vectors. Expanding both "
            "expressions and using symmetry to flip the sign of any negative "
            "indifferent coefficient produces one strictly positive finite "
            "combination equal to zero. Sequence cancellation would force a "
            "strict vector to be indifferent, which it is not. Therefore the "
            "two sets are disjoint, and the separation lemma applies. Lean "
            "does not keep Scott's barycentric normalization $\\sum\\lambda_i=1$ "
            "as a separate hypothesis; convex-hull membership already supplies "
            "it, and vanishing weights are discarded before the sequence is "
            "formed.",
        ),
        Card(
            "C-I07",
            98,
            107,
            "IsRationalVector,IsRationalSet,UnweightedSequenceCancellation,scott_theorem_1_2",
            "Rational coordinates and Theorem 1.2",
            """```lean
def IsRationalVector {S : Type*} (x : S → ℝ) : Prop :=
  ∀ s, ∃ q : ℚ, x s = q

theorem scott_theorem_1_2 {S : Type*} [Fintype S] {X N : Set (S → ℝ)}
    (hX : X.Finite) (hrat : IsRationalSet X) (hsym : Symmetric X) :
    Realizable X N ↔ SignComplete X N ∧ UnweightedSequenceCancellation X N
```""",
            "Scott's $L(S)$ is the function space $S\\to\\mathbb{R}$ with $S$ "
            "finite. Rationality is coordinatewise. Condition (4) is the same "
            "cancellation with every coefficient equal to $1$; repetitions "
            "stand in for integer multiplicities. The theorem is the "
            "combinatorial special case of Theorem 1.1 once positive real "
            "weights can be replaced by unweighted repetitions.",
        ),
        Card(
            "C-I08",
            108,
            109,
            "exists_pos_rational_relation,UnweightedSequenceCancellation.rationalWeighted,UnweightedSequenceCancellation.natWeighted",
            "Proof of Theorem 1.2",
            """The rationalization pipeline is isolated in
`LinearInequalities/Rationalization.lean`: a positive real dependence among
rational vectors is replaced by a positive rational dependence, denominators
are cleared, and each vector is repeated according to its natural
multiplicity.""",
            "A homogeneous linear relation with rational coordinates and "
            "positive real coefficients admits a positive rational solution. "
            "Clearing a common denominator yields a positive natural-weight "
            "relation. Repeating each vector that many times produces an "
            "unweighted sequence summing to zero, to which (4) applies. Thus "
            "unweighted cancellation implies weighted cancellation on rational "
            "sets, and Theorem 1.1 supplies the functional. The converse is "
            "immediate: drop the weights.",
        ),
        Card(
            "C-I09",
            110,
            113,
            "RelationRealizable,RelationComplete",
            "Realizable relations",
            """```lean
def RelationRealizable (Y : Set L) (R : L → L → Prop) : Prop :=
  ∃ φ : Module.Dual ℝ L, ∀ x ∈ Y, ∀ y ∈ Y, R x y ↔ φ y ≤ φ x
```""",
            "A binary comparison on a set of vectors is realized by comparing "
            "the values of one linear functional. Lean orients $R\\,x\\,y$ as "
            "$\\varphi(y)\\le\\varphi(x)$, matching Scott's $x\\succsim y$ iff "
            "$\\varphi(x)\\ge\\varphi(y)$. Completeness is condition (5).",
        ),
        Card(
            "C-I10",
            114,
            125,
            "scott_theorem_1_3,RelationSequenceCancellation",
            "Theorem 1.3",
            """```lean
theorem scott_theorem_1_3 {S : Type*} [Fintype S]
    {Y : Set (S → ℝ)} {R : (S → ℝ) → (S → ℝ) → Prop}
    (hY : Y.Finite) (hYrat : IsRationalSet Y) :
    RelationRealizable Y R ↔
      RelationComplete Y R ∧ RelationSequenceCancellation Y R
```""",
            "The difference set $X=Y-Y$ is finite, rational, and symmetric. "
            "Declaring $x-y\\ge 0$ when $R\\,x\\,y$ is well-defined because "
            "paired equal-sums cancellation identifies differences that "
            "represent the same vector. Completeness of $R$ becomes sign "
            "completeness of that sign pattern, and (6) becomes unweighted "
            "cancellation. Theorem 1.2 returns a functional on differences, "
            "hence a realization of $R$. Lean also records a geometric "
            "variant `scott_theorem_1_3_geometric` that never appears in the "
            "paper: disjointness of the convex hull of strict differences from "
            "the span of indifferent differences.",
        ),
        Card(
            "C-I11",
            126,
            127,
            "scott_theorem_1_3,rational_difference_set,RelationRealizable.sequenceCancellation",
            "Proof of Theorem 1.3",
            "The body of `scott_theorem_1_3` constructs the difference set, "
            "transports (5)--(6) to Theorem 1.2, and uses a two-element "
            "cancellation to recover the original relation from the functional.",
            "Necessity of (6) is evaluation of a realizing functional on equal "
            "sums. Sufficiency must also check that the sign assigned to a "
            "difference does not depend on the pair that represents it. If "
            "$x-y=x'-y'$ then the two-term sequence $(x,y')$ versus $(y,x')$ "
            "has equal sums, so (6) identifies $R\\,x\\,y$ with $R\\,x'\\,y'$. "
            "After Theorem 1.2 produces $\\varphi$, a second two-point "
            "cancellation ensures that $\\varphi(x)\\ge\\varphi(y)$ implies "
            "the original $R$, not merely some relation with the same "
            "nonnegative cone of differences.",
        ),
        Card(
            "C-I12",
            128,
            139,
            "StrictlyMonotonic,additiveClosure,ExtendsOn",
            "Strictly monotonic relations and additive closure",
            """```lean
structure StrictlyMonotonic (Z : Set L) (R : L → L → Prop) : Prop where
  complete : ∀ ⦃x⦄, x ∈ Z → ∀ ⦃y⦄, y ∈ Z → R x y ∨ R y x
  add : ∀ ⦃x₀ y₀ x₁ y₁⦄, x₀ ∈ Z → y₀ ∈ Z → x₁ ∈ Z → y₁ ∈ Z →
    R x₀ y₀ → R x₁ y₁ → R (x₀ + x₁) (y₀ + y₁)
  cancel : ∀ ⦃x₀ y₀ x₁ y₁⦄, x₀ ∈ Z → y₀ ∈ Z → x₁ ∈ Z → y₁ ∈ Z →
    x₀ + x₁ = y₀ + y₁ → R x₁ y₁ → R y₀ x₀

def additiveClosure (Y : Set L) : Set L :=
  AddSubmonoid.closure Y
```""",
            "Scott's $Y^+$ is the additive monoid generated by $Y$, including "
            "the empty sum. The three axioms are totality, preservation of "
            "addition, and cancellation of a summand. `ExtendsOn` says the "
            "enlarged relation agrees with the original on $Y$. These are the "
            "ingredients of Theorem 1.4, not an independent representation "
            "theorem on the whole closure.",
        ),
        Card(
            "C-I13",
            140,
            149,
            "scott_theorem_1_4,scott_theorem_1_4_forward,StrictlyMonotonic.relationSequenceCancellation",
            "Theorem 1.4",
            """```lean
theorem scott_theorem_1_4 {S : Type*} [Fintype S]
    {Y : Set (S → ℝ)} {R : (S → ℝ) → (S → ℝ) → Prop}
    (hY : Y.Finite) (hYrat : IsRationalSet Y) :
    RelationRealizable Y R ↔
      ∃ Rplus,
        ExtendsOn Y (additiveClosure Y) R Rplus ∧
        StrictlyMonotonic (additiveClosure Y) Rplus
```""",
            "A realizing functional extends immediately by the same comparison "
            "of values, and linearity gives the three monotonicity axioms. "
            "Conversely, an extension that is strictly monotonic on $Y^+$ "
            "implies (6): add the comparisons other than the distinguished "
            "pair, then cancel the resulting equal totals. Theorem 1.3 "
            "finishes the argument. Scott's warning is exact in Lean as well: "
            "the theorem realizes the restriction to finite $Y$, not the "
            "relation on the whole closure.",
        ),
        Card(
            "C-I14",
            150,
            154,
            "lexPreference,lexPreference_strictlyMonotonic,no_global_real_additive_lex_realization",
            "The non-Archimedean warning",
            """Lean illustrates the same obstruction with the lexicographic
group $\\mathbb{Z}\\times\\mathbb{Z}$ rather than Scott's displayed
subset of $E^2$:

```lean
theorem no_global_real_additive_lex_realization :
    ¬ ∃ φ : LexIntPair → ℝ,
        (∀ x y, lexPreference x y ↔ φ y ≤ φ x) ∧
          ∀ x y, φ (x + y) = φ x + φ y
```""",
            "Scott's example is a lexicographic order on the additive monoid "
            "generated by two basis vectors. Lean uses the lexicographic "
            "product of two copies of $\\mathbb{Z}$. The order is strictly "
            "monotonic on the monoid generated by $(1,0)$ and $(0,1)$, yet any "
            "additive real representation would force one positive generator "
            "to dominate arbitrarily many copies of the other. The printed "
            "coordinatewise recipe and the Lean lexicographic group are the "
            "same phenomenon, not a line-for-line transcription of the $E^2$ "
            "display.",
        ),
        Card(
            "C16",
            155,
            165,
            "none",
            "Editorial OCR reconciliation notes",
            none_panel(),
            "This table is an editorial record of discrepancies among OCR "
            "passes. It is not part of Scott's paper and contributes no Lean "
            "object. The checker treats the card as coverage only and does "
            "not compare its quotation to the source lines.",
        ),
        Card(
            "C-I15",
            166,
            177,
            "finite_local_real_embedding",
            "Finite subsets of ordered abelian groups",
            """```lean
theorem finite_local_real_embedding (S : Set G) (hS : S.Finite) :
    ∃ f : S → ℝ,
      (∀ x y : S, x ≤ y ↔ f x ≤ f y) ∧
      (∀ x y z : S, (x : G) + y = z → f x + f y = f z)
```""",
            "Characteristic functions of singleton elements of a finite subset "
            "$S$ become rational test vectors. Finite addition equations "
            "visible inside $S$ become further test vectors. The coordinatewise "
            "comparison of those vectors is strictly monotonic on their "
            "additive closure, so Theorem 1.4 supplies a functional. "
            "Evaluating that functional on basis vectors yields a real map "
            "that reflects the ambient order on $S$ and preserves every "
            "equation $x+y=z$ whose three terms lie in $S$. Lean therefore "
            "proves a slightly stronger local embedding than the prose "
            "sentence “preserves the addition and order relations within "
            "the finite set $S$,” but it does not state a separately named "
            "theorem that every ordered abelian group embeds globally in "
            "$\\mathbb{R}$.",
        ),
        Card(
            "C-I16",
            178,
            179,
            "none",
            "Bridge to the three measurement problems",
            none_panel("`theorem_3_1` and `theorem_4_1`, which apply Theorem 1.3"),
            "The sentence is a methodological promise. In the formal library "
            "it is true of the pair and probability developments and not yet "
            "true of Theorem 2.1, whose completed converse uses the "
            "Scott--Suppes staircase instead of an incidence-vector instance "
            "of Theorem 1.2.",
        ),
    ]


def section_ii_cards() -> list[Card]:
    return [
        Card(
            "C-II01",
            180,
            186,
            "RealizablePreference,PrefIrrefl",
            "Section II setup",
            """```lean
def PrefIrrefl {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x, ¬P x x
```""",
            "Realizability is again the unit-threshold representation. A "
            "realizing $f$ is automatically irreflexive, so Scott assumes "
            "`PrefIrrefl` as axiom $(1_P)$. Lean keeps that axiom on the "
            "right-hand side of `theorem_2_1` rather than as a standing "
            "typeclass on $P$.",
        ),
        Card(
            "C-II02",
            187,
            201,
            "none",
            "The auxiliary vector $e$ and the set $X$",
            none_panel(
                "`RealizablePreference` and the unused local moves in "
                "`Preference/Cycle.lean`. There is no incidence-vector "
                "encoding of Section II"
            ),
            "Scott embeds $A\\cup\\{e\\}$ as a basis and realizes the sign "
            "pattern of the vectors $x-y-e$ and $y+e-x$ by Theorem 1.2. That "
            "construction is not in the library. The checked proof of "
            "Theorem 2.1 never builds $X$, never mentions $e$, and never "
            "calls `scott_theorem_1_2`. This is the principal missing "
            "formal counterpart in Section II.",
        ),
        Card(
            "C-II03",
            202,
            206,
            "RealizablePreference.necessary",
            "Normalization $\\varphi(e)=1$ and necessity of the axioms",
            """Necessity of $(1_P)$--$(3_P)$ is proved directly from $f$, not
from a functional on $X$:

```lean
theorem RealizablePreference.necessary {A : Type u} {P : A → A → Prop}
    (hP : RealizablePreference P) :
    PrefIrrefl P ∧ PrefQuadA P ∧ PrefQuadB P
```""",
            "If a unit-threshold $f$ exists, irreflexivity and the two "
            "quadruple implications are linear arithmetic. Scott obtains the "
            "same necessities after normalizing $\\varphi(e)=1$. Lean skips "
            "that normalization because it never constructs $\\varphi$. The "
            "conclusions coincide; the routes do not.",
        ),
        Card(
            "C-II04",
            207,
            221,
            "none",
            "Cancellation sequences and independence of $e$",
            none_panel(),
            "The printed argument shows that a putative zero-sum of the "
            "incidence vectors forces equally many primed and unprimed terms "
            "because $e$ is independent of $A$. There is no Lean lemma for "
            "this count, because the incidence vectors themselves are absent.",
        ),
        Card(
            "C-II05",
            222,
            234,
            "none",
            "Permutation of the two arrays",
            none_panel(),
            "Independence of the basis $A$ yields only that the upper and "
            "lower arrays are permutations of one another. Lean has this "
            "style of argument for pairs (`pairVector_sum_eq_permutations`) "
            "but not for the Section II encoding. The subsequent “tour "
            "through the permutation” is therefore also unformalized as a "
            "global cycle decomposition.",
        ),
        Card(
            "C-II06",
            235,
            244,
            "preference_transitive_of_quadA",
            "Case 1: an unprimed $P$-cycle",
            """```lean
theorem preference_transitive_of_quadA {A : Type u} {P : A → A → Prop}
    (hirr : ∀ x, ¬ P x x)
    (hquad : ∀ x y z w, P x y → P z w → P x w ∨ P z y) :
    Transitive P
```""",
            "Scott rules out a pure $P$-cycle by transitivity plus "
            "irreflexivity. Lean proves transitivity from the quadruple "
            "axiom $(2_P)$ by substituting $y$ for $z$, which is exactly "
            "Scott's later parenthetical. It does not construct the cycle "
            "from a permutation of arrays, and the lemma is not imported by "
            "`theorem_2_1`.",
        ),
        Card(
            "C-II07",
            245,
            270,
            "preference_shorten_ppq,preference_shorten_qpp,PrefQuadB",
            "Case 2: adjacent $P$'s and condition $(3_P)$",
            """```lean
def PrefQuadB {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x y z w, P x y → P z x → P w y ∨ P z w

theorem preference_shorten_ppq {A : Type u} {P : A → A → Prop}
    (hquad : ∀ x y z w, P x y → P z x → P w y ∨ P z w)
    {z x y w : A} (hzx : P z x) (hxy : P x y) (hyw : ¬ P w y) :
    P z w
```""",
            "The local configurations $zPxPyQw$ and $wQzPxPy$ are the two "
            "adjacent-$P$ shortenings. Given $(3_P)$, each configuration "
            "collapses to a shorter cycle with equally many $P$'s and $Q$'s. "
            "Lean records both local inferences and stops there. It does not "
            "assemble them into a descent on a global mixed cycle, which is "
            "why they cannot yet replace the staircase proof.",
        ),
        Card(
            "C-II08",
            271,
            287,
            "preference_shorten_pqp,PrefQuadA",
            "Alternating cycles and condition $(2_P)$",
            """```lean
def PrefQuadA {A : Type u} (P : A → A → Prop) : Prop :=
  ∀ x y z w, P x y → P z w → P x w ∨ P z y

theorem preference_shorten_pqp {A : Type u} {P : A → A → Prop}
    (hquad : ∀ x y z w, P x y → P z w → P x w ∨ P z y)
    {x y z w : A} (hxy : P x y) (hyz : ¬ P z y) (hzw : P z w) :
    P x w
```""",
            "Once adjacent $P$'s are removed, a balanced cycle is alternating "
            "and contains the pattern $xPyQzPw$. Condition $(2_P)$ shortens "
            "that pattern. Repeated shortening would reach $xPx$, contradicting "
            "irreflexivity. Lean has the local move and the observation that "
            "$(2_P)$ implies transitivity. The global descent remains a gap.",
        ),
        Card(
            "C-II09",
            288,
            297,
            "theorem_2_1,finite_staircase_representation,ScottWeakOrder",
            "Theorem 2.1",
            """```lean
theorem theorem_2_1 {A : Type u} [Fintype A] [Nonempty A]
    (P : A → A → Prop) :
    RealizablePreference P ↔
      PrefIrrefl P ∧ PrefQuadA P ∧ PrefQuadB P
```

The converse is not Scott's cycle argument. It uses `ScottWeakOrder`,
antisymmetrization, and `finite_staircase_representation`.""",
            "The statement is faithful. Necessity is the linear-arithmetic "
            "lemmas already cited. Sufficiency compares alternatives by their "
            "strict-preference profiles: $x$ is weakly below $y$ when every "
            "predecessor of $x$ is a predecessor of $y$ and every successor of "
            "$y$ is a successor of $x$. The two quadruple axioms make this "
            "relation a total preorder. Antisymmetrization quotients by "
            "identical profiles. On the finite quotient the lower sections are "
            "nested, and a recursively constructed staircase assigns real "
            "values with a unit gap, which pulls back to $A$. This is the "
            "Scott--Suppes construction, not a formalization of pages 7--9.",
        ),
        Card(
            "C-II10",
            298,
            307,
            "StrictlyRealizablePreference,RealizablePreference.strict_of_finite,realizablePreference_threshold_iff",
            "Strict margins and Scott's methodological remark",
            """```lean
def StrictlyRealizablePreference {A : Type u} (P : A → A → Prop) : Prop :=
  ∃ f : A → ℝ, ∀ x y, P x y ↔ f x > f y + 1

theorem RealizablePreference.strict_of_finite
    {A : Type u} [Fintype A] [Nonempty A] {P : A → A → Prop}
    (hP : RealizablePreference P) : StrictlyRealizablePreference P
```""",
            "On a finite set a realizing assignment can be perturbed so that "
            "the unit threshold is never attained. Lean proves that the weak "
            "and strict unit-threshold representations are equivalent for "
            "finite $A$, and that any positive threshold is equivalent to $1$ "
            "after rescaling. Scott's closing remark that the proof is "
            "unattractive but mechanical is commentary; the formal converse "
            "is attractive for a different reason, and it is not the "
            "mechanical Section I analysis he describes.",
        ),
    ]


def section_iii_cards() -> list[Card]:
    return [
        Card(
            "C-III01",
            308,
            317,
            "RealizableUtilityPair",
            "Additive utilities for pairs",
            """```lean
def RealizableUtilityPair {A : Type u} {A' : Type v}
    (V : A → A' → A → A' → Prop) : Prop :=
  ∃ f : A → ℝ, ∃ f' : A' → ℝ,
    ∀ x x' y y', V x x' y y' ↔ f x + f' x' ≥ f y + f' y'
```""",
            "A comparison of commodity bundles is additive across the two "
            "factors. Lean uses a four-argument predicate rather than a "
            "relation on a cartesian product, which is the same data. The "
            "philosophy that “the whole is the sum of its parts” is the "
            "meaning of the displayed inequality, not an extra axiom.",
        ),
        Card(
            "C-III02",
            318,
            325,
            "pairVector",
            "Incidence vectors of pairs",
            """```lean
noncomputable def pairVector {A : Type u} {A' : Type v} (x : A) (x' : A') :
    Sum A A' → ℝ :=
  Pi.single (Sum.inl x) 1 + Pi.single (Sum.inr x') 1
```""",
            "Scott's $S=A\\cup A^*$ and $Y=\\{x+x^*\\}$ become functions on "
            "`Sum A A'`. Disjointness of the two summands is built into the "
            "coproduct, so the later remark that disjointness is only a "
            "technical device is already reflected in the types: Theorem 3.1 "
            "never assumes `Disjoint` of the original sets. The relation on "
            "$Y$ is $V$ transported along `pairVector`.",
        ),
        Card(
            "C-III03",
            326,
            348,
            "PairTotal,PairPermutation,pairVector_sum_eq_permutations,finHead",
            "Totality, equal sums, and the two permutations",
            """```lean
def PairPermutation {A : Type u} {A' : Type v}
    (V : A → A' → A → A' → Prop) : Prop :=
  ∀ (n : ℕ) (x : Fin (n + 1) → A) (x' : Fin (n + 1) → A')
    (π σ : Equiv.Perm (Fin (n + 1))),
    (∀ i, i ≠ finHead n → V (x i) (x' i) (x (π i)) (x' (σ i))) →
      V (x (π (finHead n))) (x' (σ (finHead n)))
        (x (finHead n)) (x' (finHead n))
```""",
            "Independence of the two families of coordinates splits an equality "
            "of pair-vector sums into two multiplicity identities. "
            "`pairVector_sum_eq_permutations` upgrades those identities to "
            "permutations $\\pi$ and $\\sigma$. Condition $(2_V)$ is the "
            "resulting cancellation, with Scott's distinguished index $0$ "
            "rendered as `finHead n` and the hypothesis taken only for the "
            "other indices, as he allows parenthetically.",
        ),
        Card(
            "C-III04",
            349,
            359,
            "theorem_3_1,LinearInequalities.scott_theorem_1_3",
            "Theorem 3.1",
            """```lean
theorem theorem_3_1 {A : Type u} {A' : Type v}
    [Fintype A] [Nonempty A] [Fintype A'] [Nonempty A']
    (V : A → A' → A → A' → Prop) :
    RealizableUtilityPair V ↔ PairTotal V ∧ PairPermutation V
```""",
            "Necessity is evaluation of $f+f'$. Sufficiency transports $V$ to "
            "the finite rational range of `pairVector`, turns totality into "
            "`RelationComplete` and the permutation axiom into "
            "`RelationSequenceCancellation`, and applies Theorem 1.3. The "
            "resulting functional, restricted to the two kinds of singleton "
            "spikes, is the pair of utilities. This is the printed route.",
        ),
        Card(
            "C-III05",
            360,
            365,
            "PairPermutation.transitive",
            "$(2_V)$ implies transitivity",
            """```lean
theorem PairPermutation.transitive {A : Type u} {A' : Type v}
    {V : A → A' → A → A' → Prop} (hV : PairPermutation V) :
    ∀ p q r : A × A',
      V p.1 p.2 q.1 q.2 → V q.1 q.2 r.1 r.2 → V p.1 p.2 r.1 r.2
```""",
            "Scott's three-cycle of indices with $\\pi=\\sigma$ the cycle "
            "$(0\\,1\\,2)$ is copied exactly, using the length-$3$ instance "
            "of `PairPermutation`. The calculation is a check that the "
            "infinite scheme already contains ordinary transitivity.",
        ),
        Card(
            "C-III06",
            366,
            381,
            "RealizableDifference,RealizableDifference.utilityPair",
            "Ordered differences and the pair of utilities $g,h$",
            """```lean
theorem RealizableDifference.utilityPair {A : Type u}
    {D : A → A → A → A → Prop} (hD : RealizableDifference D) :
    RealizableUtilityPair D
```""",
            "Scott defines an auxiliary $V$ by swapping slots, $xw\\,V\\,zy$ "
            "iff $xy\\,D\\,zw$, then invokes Theorem 3.1 to obtain $g$ and "
            "$h$ with $g(x)-h(y)$ representing $D$. Lean never names that "
            "$V$. It treats $D$ itself as a pair relation and represents it "
            "by $g(x)+q(y)$, i.e. $g(x)-h(y)$ with $q=-h$. The algebra is "
            "the same; the intermediate relabeling is not a definition in "
            "the library.",
        ),
        Card(
            "C-III07",
            382,
            417,
            "DiffReversal,difference_of_pair_and_reversal",
            "Reversal and the sum of the two scales",
            """```lean
def DiffReversal {A : Type u} (D : A → A → A → A → Prop) : Prop :=
  ∀ x y z w, D x y z w → D w z y x

theorem difference_of_pair_and_reversal {A : Type u}
    {D : A → A → A → A → Prop} (hp : RealizableUtilityPair D)
    (hr : DiffReversal D) : RealizableDifference D
```""",
            "Reversal is the commutativity $xy\\,D\\,zw\\Rightarrow wz\\,D\\,yx$. "
            "From a pair representation $g,q$ one obtains both "
            "$g(x)+q(y)\\ge g(z)+q(w)$ and the reversed inequality. Adding "
            "them produces the single difference $f(x)-f(y)$ with "
            "$f=g-q$. The converse direction is the same addition on the "
            "strictly opposite inequalities. This is Scott's $f=g+h$ after "
            "the sign convention $q=-h$.",
        ),
        Card(
            "C-III08",
            418,
            429,
            "theorem_3_2,DiffTotal,DiffPermutation",
            "Theorem 3.2",
            """```lean
theorem theorem_3_2 {A : Type u} [Fintype A] [Nonempty A]
    (D : A → A → A → A → Prop) :
    RealizableDifference D ↔
      DiffTotal D ∧ DiffPermutation D ∧ DiffReversal D
```""",
            "The three axioms are totality, the same permutation scheme as "
            "$(2_V)$, and reversal. Sufficiency applies Theorem 3.1 to $D$ "
            "as a pair relation and then `difference_of_pair_and_reversal`. "
            "Lean therefore follows Scott's architecture: one-utility "
            "differences are two-utility pairs plus commutativity.",
        ),
        Card(
            "C-III09",
            430,
            431,
            "DiffPermutation",
            "The infinite bundle $(2_D)$",
            none_panel("`DiffPermutation`, which quantifies over every `n` and both permutations"),
            "Scott remarks that no finite truncation of the permutation "
            "scheme is sufficient, citing Scott--Suppes 1958. Lean does not "
            "prove that non-finite-axiomatizability result. It does keep "
            "$(2_D)$ as a genuine infinite scheme: the universal quantifiers "
            "over `n`, $\\pi$, and $\\sigma$ are essential to the definition.",
        ),
    ]


def section_iv_cards() -> list[Card]:
    return [
        Card(
            "C-IV01",
            432,
            439,
            "RealizableProbability",
            "Section IV: qualitative probability",
            "The existence question is again `RealizableProbability`.",
            "A finite Boolean algebra of events carries a binary comparison "
            "intended as subjective probability. Realization means a genuine "
            "finitely additive probability, not a signed charge. The infinite "
            "case is postponed to the last paragraph and is not a numbered "
            "theorem of the paper.",
        ),
        Card(
            "C-IV02",
            440,
            455,
            "DeFinettiAxioms,ProbTransitive,ProbDisjointUnionInvariant,ProbTotal",
            "de Finetti's five axioms",
            """```lean
structure DeFinettiAxioms {B : Type u} [BooleanAlgebra B]
    (R : B → B → Prop) : Prop where
  nontrivial : ¬R ⊥ ⊤
  bottom : ∀ x, R x ⊥
  total : ProbTotal R
  transitive : ProbTransitive R
  disjointUnionInvariant : ProbDisjointUnionInvariant R
```""",
            "Lean bundles the five axioms Scott attributes to de Finetti. "
            "Condition (i) is the weak nontriviality $\\neg\\bot\\succsim\\top$, "
            "not Scott's later $(1_B)$ which also demands $\\top\\succsim\\bot$. "
            "Condition (v) is invariance of comparisons under disjoint union "
            "with a third event. These axioms are recorded in order to state "
            "the KPS insufficiency theorem; they are not the hypotheses of "
            "Theorem 4.1.",
        ),
        Card(
            "C-IV03",
            456,
            459,
            "deFinetti_axioms_insufficient,atomVector,StrictlyPreferred",
            "The KPS counterexample and atom vectors",
            """```lean
def atomVector {B : Type u} [BooleanAlgebra B] (x : B) :
    {a : B // IsAtom a} → ℝ :=
  fun a ↦ if a.1 ≤ x then 1 else 0
```""",
            "The 32-element counterexample is the powerset of five atoms with "
            "the exact KPS rank order `KPSGe`. Lean verifies the bundled de "
            "Finetti axioms by finite inspection and proves "
            "non-representability from four strict inequalities among singleton "
            "weights, not by exhaustive search over measures. Atom vectors are "
            "the characteristic functions of the atoms below an event; disjoint "
            "suprema become vector sums. Scott's $x\\succ y$ is "
            "`StrictlyPreferred R x y := ¬ R y x`.",
        ),
        Card(
            "C-IV04",
            460,
            473,
            "theorem_4_1,ProbNontrivial,ProbNonneg,ProbTotal,ProbCancellation,theorem_4_1_vector,sum_atomVector_eq_iff",
            "Theorem 4.1",
            """```lean
theorem theorem_4_1 {B : Type u} [BooleanAlgebra B] [Fintype B]
    (R : B → B → Prop) :
    RealizableProbability R ↔
      ProbNontrivial R ∧ ProbNonneg R ∧
      ProbTotal R ∧ ProbCancellation R
```

The displayed algebraic sum is `theorem_4_1_vector`. The atom-count
reading Scott immediately supplies is the primary `ProbCancellation`.""",
            "$(1_B)$ is a strict comparison of $\\top$ with $\\bot$; $(2_B)$ "
            "is nonnegativity; $(3_B)$ is totality; $(4_B)$ is cancellation "
            "of sequences with equal atom multiplicities. Lean's primary "
            "statement uses that atom-count reading. The literal equality of "
            "characteristic-vector sums is an equivalent form, and "
            "`sum_atomVector_eq_iff` identifies the two languages. The "
            "distinguished index is again `finHead n`.",
        ),
        Card(
            "C-IV05",
            474,
            483,
            "atomLinearRepresentation_of_total_cancellation,probability_of_atomLinearRepresentation,theorem_4_1",
            "Proof of Theorem 4.1",
            "Totality and cancellation are transported to the finite rational "
            "range of `atomVector` and discharged by Theorem 1.3. The resulting "
            "`AtomLinearRepresentation` is normalized by $\\varphi(\\mathbf{1})$.",
            "Necessity is evaluation of a probability. Sufficiency applies "
            "Theorem 1.3 to atom vectors. The functional on incidence vectors "
            "is already a finitely additive signed charge on events. "
            "Nontriviality makes its value at $\\top$ positive; nonnegativity "
            "makes every event value nonnegative. Division by $\\varphi(\\top)$ "
            "is Scott's $\\mu(x)=\\varphi(x)/\\varphi(1)$ and does not change "
            "comparisons. This is the printed short proof.",
        ),
        Card(
            "C-IV06",
            484,
            487,
            "scott_p15_signed_charge,ProbCancellation.disjointUnionInvariant,ProbCancellation.transitive",
            "Signed charges and de Finetti's (v)",
            """```lean
theorem scott_p15_signed_charge (R : B → B → Prop) :
    RealizableSignedCharge R ↔ ProbTotal R ∧ ProbCancellation R

theorem ProbCancellation.disjointUnionInvariant
    {B : Type u} [BooleanAlgebra B] [Fintype B] {R : B → B → Prop}
    (h : ProbCancellation R) : ProbDisjointUnionInvariant R
```""",
            "Dropping $(1_B)$ and $(2_B)$ leaves a signed finitely additive "
            "charge, which is Scott's p. 15 remark. The derivation of "
            "disjoint-union invariance is the two-term instance of $(4_B)$ "
            "that he sketches: if $x\\succsim y$ but not "
            "$x\\cup z\\succsim y\\cup z$, totality and the identity "
            "$(y\\cup z)+x=(x\\cup z)+y$ force the opposite comparison. "
            "Lean also derives reflexivity and transitivity from cancellation, "
            "connecting Scott's criterion to the older qualitative axioms.",
        ),
        Card(
            "C-IV07",
            488,
            489,
            "reconstructed_infinite_theorem_4_1,GeneralizedKelleyCondition",
            "The unpublished infinite extension",
            """```lean
theorem reconstructed_infinite_theorem_4_1 (R : B → B → Prop) :
    RealizableProbability R ↔
      ProbNontrivial R ∧ ProbNonneg R ∧ ProbTotal R ∧
        GeneralizedKelleyCondition R
```

This is a modern theorem. It is not Scott's unpublished result.""",
            "Scott announces an extension via Hahn--Banach and Kelley (1959) "
            "and withholds the statement. Lean therefore does not attribute "
            "an infinite theorem to the 1964 paper. The library proves a "
            "separately labelled reconstruction: events embed in a normed "
            "span of evaluation functions, weak comparisons generate a closed "
            "cone, and a countable Kelley cover of the strict comparisons "
            "produces one functional that is nonnegative on weak comparisons "
            "and positive on strict ones. Normalization again yields a "
            "finitely additive probability. The extra hypothesis "
            "`GeneralizedKelleyCondition` is explicit and modern.",
        ),
    ]


def reference_cards() -> list[Card]:
    recon = (
        "Bibliographic only. The citation is recorded in the report "
        "bibliography; it is not a Lean declaration."
    )
    return [
        Card(
            "C-R00",
            490,
            491,
            "none",
            "References heading",
            none_panel(),
            recon,
        ),
        Card(
            "C-R01",
            492,
            493,
            "none",
            "Adams and Fagot 1956",
            none_panel(),
            recon,
        ),
        Card(
            "C-R02",
            494,
            495,
            "none",
            "Luce 1956",
            none_panel(),
            "Bibliographic only. Luce's semiorders motivate Problem I but "
            "are not imported as a Lean theory.",
        ),
        Card(
            "C-R03",
            496,
            497,
            "none",
            "Luce and Tukey 1964",
            none_panel(),
            recon,
        ),
        Card(
            "C-R04",
            498,
            499,
            "none",
            "Kelley 1959",
            none_panel(
                "`reconstructed_infinite_theorem_4_1` and `KelleyCover`, "
                "which follow Kelley's method without claiming Scott's "
                "unpublished theorem"
            ),
            "The report cites the correct *Pacific Journal of Mathematics* "
            "volume for Kelley. The vision transcription's volume number "
            "is an OCR discrepancy, not a Lean fact.",
        ),
        Card(
            "C-R05",
            500,
            501,
            "deFinetti_axioms_insufficient",
            "Kraft, Pratt, and Seidenberg 1959",
            none_panel("`deFinetti_axioms_insufficient` and the `KPSGe` order"),
            "The citation is bibliographic. The mathematical content of that "
            "paper used here is the five-atom order already aligned above.",
        ),
        Card(
            "C-R06",
            502,
            503,
            "finite_strict_separation",
            "Kuhn and Tucker 1956",
            none_panel("`finite_strict_separation`"),
            "Scott's separation citation is replaced, in the formal proof, "
            "by Mathlib's compact-closed Hahn--Banach theorem. The book is "
            "not a dependency of the Lean library.",
        ),
        Card(
            "C-R07",
            504,
            505,
            "finite_staircase_representation,ScottWeakOrder",
            "Scott and Suppes 1958",
            none_panel("`finite_staircase_representation`"),
            "The 1958 paper is the source of the completed converse to "
            "Theorem 2.1 and of the remark that $(2_D)$ is not finitely "
            "axiomatizable. Only the representation construction is "
            "formalized here.",
        ),
        Card(
            "C-R08",
            506,
            507,
            "none",
            "Suppes and Zinnes 1963",
            none_panel(),
            recon,
        ),
    ]


def validate(cards_list: list[Card]) -> None:
    prev_end = 6
    seen: set[str] = set()
    for card in cards_list:
        if card.card_id in seen:
            raise SystemExit(f"duplicate card id {card.card_id}")
        seen.add(card.card_id)
        if card.start != prev_end + 1:
            raise SystemExit(
                f"{card.card_id} starts at {card.start}, expected {prev_end + 1}"
            )
        if card.start > card.end:
            raise SystemExit(f"{card.card_id} has reversed range")
        prev_end = card.end
    if prev_end != 507:
        raise SystemExit(f"coverage ends at {prev_end}, expected 507")
    if "C16" not in seen:
        raise SystemExit("missing C16")


def render(cards_list: list[Card], lines: list[str]) -> str:
    parts: list[str] = [
        "### Front matter, abstract, and the three problems\n"
    ]
    section_breaks = {
        "C-I01": "### I. The general method\n",
        "C-II01": "### II. Intransitive indifference\n",
        "C-III01": "### III. Ordered differences\n",
        "C-IV01": "### IV. Subjective probability\n",
        "C-R00": "### References in Scott 1964\n",
    }
    for card in cards_list:
        if card.card_id in section_breaks:
            parts.append(section_breaks[card.card_id])
        parts.append(emit_card(card, lines))
    return "\n".join(parts).rstrip() + "\n"


def splice(arxiv_text: str, body: str) -> str:
    start = arxiv_text.find(BEGIN)
    end = arxiv_text.find(END)
    if start == -1 or end == -1 or end < start:
        raise SystemExit("arxiv.md is missing CONCORDANCE_BODY markers")
    return arxiv_text[: start + len(BEGIN)] + "\n\n" + body + "\n" + arxiv_text[end:]


def main() -> int:
    cards_list = cards()
    validate(cards_list)
    source_lines = SOURCE.read_text(encoding="utf-8").splitlines()
    body = render(cards_list, source_lines)
    arxiv = ARXIV.read_text(encoding="utf-8")
    ARXIV.write_text(splice(arxiv, body), encoding="utf-8")
    print(f"wrote {len(cards_list)} concordance cards into {ARXIV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
