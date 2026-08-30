# Systems of Inequalities in Representational Measurement Theory: Foundations, Scope, and Formalization

## 1. Overview and Context

Determining the existence of solutions to systems of inequalities is a fundamental problem across mathematical optimization, real algebraic geometry, and variational analysis. In the foundational literature of mathematical psychology, decision theory, and the social sciences—exemplified by Dana Scott’s seminal paper, *"Measurement Structures and Linear Inequalities"* (1964)—this problem takes center stage within **Representational (Axiomatic) Measurement Theory**.

Measurement theory investigates the formal conditions under which qualitative, empirical observations (such as preference orderings, perceived intensity, or comparative likelihoods) can be faithfully represented by real numbers. 

---

## 2. Mathematical Foundations: Linear Inequalities and Representation Theorems

When qualitative comparisons on finite sets (e.g., $A \succsim B$) are translated into numerical relations (e.g., $u(A) \ge u(B)$ or $P(A) \ge P(B)$), the problem reduces to determining whether a finite system of linear inequalities has a non-trivial real solution.

### Core Mathematical Machinery
1. **Theorems of the Alternative (Convex Optimization & Polyhedral Geometry):**
   * **Farkas’ Lemma & Motzkin’s Transposition Theorem:** These results establish that a system of linear inequalities $Ax \le b$ has a solution if and only if a dual system has no solution. 
   * In measurement theory, dual non-solvability yields finite **cancellation axioms** (such as the Kraft–Pratt–Seidenberg conditions for finite comparative probability), guaranteeing the existence of an agreeing numerical scale.
2. **Fourier–Motzkin Elimination:**
   * An algorithmic technique for projecting systems of linear inequalities onto lower-dimensional subspaces, providing constructive proofs for feasibility.
3. **Model Theory and Relational Structures:**
   * Establishing representation theorems as structure-preserving homomorphisms from an empirical relational structure $\langle A, R_1, \dots, R_k \rangle$ into a numerical structure $\langle \mathbb{R}, \ge, +, \dots \rangle$.

---

## 3. Disambiguation: Measurement Theory vs. Measure Theory

Although their names are frequently conflated, **Measurement Theory** and **Measure Theory** address fundamentally distinct questions:

| Dimension | **Measure Theory** | **Measurement Theory** |
| :--- | :--- | :--- |
| **Primary Domain** | Real Analysis, Functional Analysis, Probability | Mathematical Psychology, Decision Theory, Foundations of Science |
| **Core Question** | How do we rigorously assign size, area, volume, and integration to abstract sets? | Under what axiomatic conditions can empirical relations be mapped homomorphically to numbers? |
| **Key Objects** | $\sigma$-algebras, Borel measures, $L^p$ spaces, Lebesgue integration | Relational structures, scales (ordinal, interval, ratio), semiorders, conjoint structures |
| **Foundational Figures** | Lebesgue, Borel, Radon, Carathéodory | Scott, Suppes, Luce, Krantz, Tversky |

*Point of Contact:* The two fields briefly intersect in **subjective probability**, where measurement theory formulates axioms ensuring that a comparative probability relation $\succsim$ induces an agreeing numerical probability distribution—which is a measure in the analytic sense.

---

## 4. Formalization Landscape in Interactive Theorem Proving (Lean / Mathlib)

As of current developments in Lean 4’s mathematical library (`Mathlib`):

* **Dedicated Measurement Theory:** There is currently no dedicated library for representational measurement theory, Scott's representation theorems, semiorders, or additive conjoint measurement.
* **Underlying Building Blocks in Mathlib:**
  * **Convex Geometry & Duality:** `Mathlib.Analysis.Convex.Cone.InnerDual` contains geometric formulations of hyperplane separation theorems and dual cone properties (Farkas' Lemma).
  * **Inequality Decision Procedures:** `Mathlib.Tactic.Linarith` and the `omega` tactic internally implement Fourier–Motzkin elimination and Presburger arithmetic decision procedures to certify the solvability of linear inequality systems.
  * **Order Theory:** `Mathlib.Order.Extension.Linear` contains Szpilrajn's Extension Theorem, and `Mathlib.Order.Hom.*` provides general machinery for order embeddings and relational homomorphisms.

---

## References

1. Adams, E. W., & Fagot, R. F. (1956). *A model of riskless choice* (Tech. Rep. No. 4). Applied Mathematics and Statistics Laboratory, Stanford University.
2. Kelley, J. L. (1959). Measures on Boolean algebras. *Pacific Journal of Mathematics*, 9(4), 1165–1172.
3. Kraft, C. H., Pratt, J. W., & Seidenberg, A. (1959). Intuitive probability on finite sets. *The Annals of Mathematical Statistics*, 30(2), 408–419.
4. Kuhn, H. W., & Tucker, A. W. (Eds.). (1956). *Linear Inequalities and Related Systems* (Annals of Mathematics Studies, No. 38). Princeton University Press.
5. Luce, R. D. (1956). Semiorders and a theory of utility discrimination. *Econometrica*, 24(2), 178–191.
6. Luce, R. D., & Tukey, J. W. (1964). Simultaneous conjoint measurement: A new type of fundamental measurement. *Journal of Mathematical Psychology*, 1(1), 1–27.
7. Scott, D. (1964). Measurement structures and linear inequalities. *Journal of Mathematical Psychology*, 1(2), 233–247.
8. Scott, D., & Suppes, P. (1958). Foundational aspects of theories of measurement. *Journal of Symbolic Logic*, 23(2), 113–128.
9. Suppes, P., & Zinnes, J. L. (1963). Basic measurement theory. In R. D. Luce, R. R. Bush, & E. Galanter (Eds.), *Handbook of Mathematical Psychology* (Vol. 1, pp. 1–76). John Wiley & Sons.