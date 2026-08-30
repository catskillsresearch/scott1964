---
source_pdf: ScottMeasurement1964.pdf
ocr_method: cursor-vision-triple-merge
verification_status: draft
---

# Transcription (LLM vision OCR)


<!-- page 1 -->

JOURNAL OF MATHEMATICAL PSYCHOLOGY: 1, 233-247 (1964)

# Measurement Structures and Linear Inequalities

**DANA SCOTT**

*Stanford University, Stanford, California*

The general mathematical criterion for the solvability of finite systems of linear inequalities is applied to some specific situations from measurement theory. Three examples are treated in detail, and in each case the necessary and sufficient conditions for existence of a suitable real-valued (utility) function on a finite structure are obtained.

In establishing a system of measurement one notices first that a class of objects (or events) has a certain inherent structure. Then the next step is to find a method of assigning (real) numbers to the objects in such a way that the observed structure corresponds exactly to reasonably simple arithmetical relationships involving the assigned numbers. In this paper some theoretical aspects of this subject will be discussed particularly in connection with the following specific problems:

**PROBLEM I. (Intransitive Indifference)**

Let $A$ be a finite set and let $P$ be a binary relation on $A$. Under what conditions on $P$ will there exist a real function $f$ on $A$ such that

$$xPy \quad \text{if and only if} \quad f(x) \geqslant f(y) + 1,$$

for all $x, y \in A$?

**PROBLEM II. (Ordered Differences)**

Let $A$ be a finite set and let $D$ be a quaternary relation on $A$. Under what conditions on $D$ will there exist a real function $f$ on $A$ such that

$$xy \mathrel{D} zw \quad \text{if and only if} \quad f(x) - f(y) \geqslant f(z) - f(w),$$

for all $x, y, z, w \in A$?

**PROBLEM III. (Subjective Probability)**

Let $B$ be a finite Boolean algebra and let $\succcurlyeq$ be a binary relation on $B$. Under what conditions on $\succcurlyeq$ will there exist a probability measure $\mu$ on $B$ such that

$$x \succcurlyeq y \quad \text{if and only if} \quad \mu(x) \geqslant \mu(y),$$

for all $x, y \in B$?

Problem I was first considered in Luce (1956), where a partial solution was given. The complete solution was given in Scott and Suppes (1958) and the proof, as well as a

<!-- page 2 -->

comprehensive survey of related problems, is also presented in Suppes and Zinnes (1963). For motivation imagine that the relation $xPy$ means that the object $x$ is *definitely preferred* to the object $y$. Hence if neither $xPy$ nor $yPx$ hold, then $x$ and $y$ are *indifferent*. Unfortunately human powers of discrimination often lead to cases where indifference is intransitive. The question is then to find numerical assignments in which the boundary between preference and indifference is made explicit: the arithmetic relation $\alpha \geqslant \beta + 1$ is an obvious candidate for performing this service (note that the constant 1 could be replaced by any other convenient positive constant by a change of units.) The solution in Scott and Suppes (1958), though direct, is a quite tedious and clumsy proof exploiting special properties of the particular situation. The method to be presented in Section I and applied in Section II uses very well-known theorems on the existence of solutions of linear inequalities. As a special virtue of the approach we find that analysis of the conditions from the general result specialized to the particular instance leads us to *discover* the required properties of the relation $P$ in an almost mechanical way. This virtue will be illustrated in the discussion of the other problems as well.

Problem III was solved in Kraft, Pratt, and Seidenberg (1959). Those authors suggest the kind of method used here, but carry out a different, more direct approach. Their conditions are a little hard to digest because they write certain formulas *multiplicatively* when an *additive* notation is more suggestive and more natural in application to Boolean algebras. For this reason, and for purely expository reasons, the author decided to include the details in Section IV; the proof, however, is quite short given the material of Section I.

A solution to Problem II has, to the author's best knowledge, not been previously published. (After this paper was prepared for publication, the referee informed the author that E. W. Adams had independently obtained similar results by pursuing the method of Adams and Fagot (1956). More specifically, Adams obtained results including those given below in Theorem 3.1 and 4.1. The details are contained in a dittoed report "Remarks on inexact additive measurement." The author is happy to acknowledge priority to Professor Adams. The purpose of the present paper is, in any case, to show how to apply a general method to many problems of this type.) For motivation the reader is referred to Luce and Tukey (1964) and Suppes and Zinnes (1963).

## I. THE GENERAL METHOD

Let $L$ be a finite-dimensional real linear vector space. A subset $X \subseteq L$ is *symmetric* if $X = -X = \{-x : x \in X\}$. A subset $N \subseteq X$ is called *realizable* in $X$ if there is a linear functional $\varphi$ on $L$ such that for all $x \in X$

$$x \in N \quad \text{if and only if} \quad \varphi(x) \geqslant 0.$$

<!-- page 3 -->

(Recall that a linear functional is a real-valued, homogeneous, additive function defined on $L$. Thus in case $N \neq X$ the condition means that there is a half-space $H$ of $L$ separating the sets $N$ and $X \sim N$ so that $X \cap H = N \cap H$. If $N = X$, the trivial $0$ functional shows that $N$ is realizable.) We shall employ a more suggestive notation writing $x \geqslant 0$ to mean $x \in N$. Further we write $x \leqslant 0$ to mean $-x \geqslant 0$, and $x \succ 0$ for not $x \leqslant 0$. The whole approach can be summed up by a simple, general theorem.

**THEOREM 1.1.** Let $X$ be a finite, symmetric subset of $L$. For a subset $\{x \in X : x \geqslant 0\}$ to be realizable in $X$ it is necessary and sufficient that the conditions

$$x \geqslant 0 \quad \text{or} \quad x \leqslant 0, \tag{1}$$

$$\sum_{i<n} \lambda_i x_i = 0 \quad \text{implies} \quad x_0 \leqslant 0, \tag{2}$$

hold for all $x \in X$ and all sequences $x_0, \cdots, x_{n-1} \in X$, and all scalars $\lambda_0, \cdots, \lambda_{n-1}$, where $\lambda_i > 0$ and $x_i \geqslant 0$, for $i < n$, and $n > 0$.

**PROOF.** The necessity of (1) is clear. The necessity of (2) becomes at once clear when it is considered that a realizing functional makes $\sum_{i<n} \lambda_i x_i$ nonnegative because $\lambda_i > 0$ and $x_i \geqslant 0$, for $i < n$; and since the vector sum is actually $0$, the functional cannot make $x_0$ (or any other $x_i$, for that matter) strictly positive.

To prove the sufficiency, assume that the two conditions hold. Let $Q$ be the convex polyhedral cone generated by the set $\{x \in X : x \leqslant 0\}$ and let $P$ be the convex polyhedron generated by (the convex closure of) the set $\{x \in X : x \succ 0\}$. We can assume $P$ is nonempty, since otherwise $x \leqslant 0$ holds for all $x \in X$; and therefore $x \geqslant 0$ would hold for all $x \in X$, because $X$ is symmetric. If we can show that $P$ and $Q$ are *disjoint*, it follows at once (see Theorem 2, p. 50 of the book Kuhn and Tucker 1956, for example) that there is a linear functional $\varphi$ on $L$ such that for all $x \in L$,

$$x \in P \quad \text{implies} \quad \varphi(x) > 0$$

$$x \in Q \quad \text{implies} \quad \varphi(x) \leqslant 0.$$

Thus if $x \in X$ and $x \geqslant 0$, then $-x \leqslant 0$, $-x \in Q$, $\varphi(-x) \leqslant 0$, and $\varphi(x) \geqslant 0$. If $\varphi(x) \geqslant 0$, then $\varphi(-x) \not> 0$, so $-x \notin P$, and so $-x \leqslant 0$ and $x \geqslant 0$. Hence, $\varphi$ is the required functional.

Let us then suppose that there is a vector $z \in P \cap Q$. Now

$$z = \sum_{i<l} \lambda_i x_i = \sum_{i<m} \lambda'_i x'_i,$$

<!-- page 4 -->

where $x_i \succ 0$, $\lambda_i \geqslant 0$, for $i < l$, and $\sum_{i < l} \lambda_i = 1$, and where $x'_i \leqslant 0$, $\lambda'_i \geqslant 0$, for $i < m$. By condition (1), $x_i \geqslant 0$ holds for $i < l$. Thus

$$\sum_{i < l} \lambda_i x_i + \sum_{i < m} \lambda'_i (-x'_i) = 0.$$

We can assume that all the scalars are strictly positive, and because $\sum_{i < l} \lambda_i = 1$, we know $l > 0$. Since $-x'_i \geqslant 0$ for $i < m$, we can apply (2) to conclude that $x_0 \leqslant 0$. But this contradicts the assumption that $x_0 \succ 0$, and the proof is complete.

There is a case where condition (2) of Theorem 1.1 can be simplified. Let $S$ be a finite set and let $L = L(S)$ be the vector space of all real-valued functions defined on $S$ (the ordinary $S$-dimensional vector space). A *vector* (function) in $L$ is called *rational* if all its coordinates (values) are rational numbers. A *set of rational vectors* is also called rational. With these conventions Theorem 1.1 becomes more combinatorial.

**THEOREM 1.2.** Let $X$ be a finite, rational, symmetric subset of $L$. For a subset $\{x \in X : x \geqslant 0\}$ to be realizable it is necessary and sufficient that the conditions

$$x \geqslant 0 \quad \text{or} \quad x \leqslant 0, \tag{3}$$

$$\sum_{i < n} x_i = 0 \quad \text{implies} \quad x_0 \leqslant 0, \tag{4}$$

hold for all $x \in X$ and all sequences $x_0, \cdots, x_{n-1} \in X$, where $x_i \geqslant 0$ for $i < n$, and $n > 0$.

**PROOF.** Suppose that $\sum_{i < n} \lambda_i x_i = 0$, where $n > 0$, and $\lambda_i > 0$, $x_i \geqslant 0$ for $i < n$. In other words, the $\lambda_i$ are positive solutions to a system of homogeneous linear equations with *rational* coefficients (the coordinates of the $x_i$). Hence there must also be a *rational* set of positive $\lambda_i$ satisfying the equation. By clearing fractions and replacing integral multiples by repetitions, we can apply (4) to conclude that $x_0 \leqslant 0$. Thus condition (2) is verified and the result follows by Theorem 1.1.

Suppose next that $Y$ is any subset of $L$. Suppose further that $\succsim$ is a *binary relation* on $Y$. We shall write $x \preccurlyeq y$ for $y \succsim x$. We shall say that $\succsim$ is *realizable* if there exists a linear functional $\varphi$ on $L$ such that for all $x, y \in Y$ we have

$$x \succsim y \quad \text{if and only if} \quad \varphi(x) \geqslant \varphi(y).$$

Conditions for realizability are easily deduced from Theorem 1.2.

**THEOREM 1.3.** Let $Y$ be a finite rational subset of $L$. For a binary relation $\succsim$ on $Y$ to be realizable it is necessary and sufficient that the conditions

$$x \succsim y \quad \text{or} \quad x \preccurlyeq y, \tag{5}$$

$$\sum_{i < n} x_i = \sum_{i < n} y_i \quad \text{implies} \quad x_0 \preccurlyeq y_0, \tag{6}$$

<!-- page 5 -->

hold for all $x, y \in Y$ and all sequences $x_0, \cdots, x_{n-1}, y_0, \cdots, y_{n-1} \in Y$, where $x_i \succsim y_i$ for $i < n$ and $n > 0$.

**PROOF.** Assume (5) and (6). Let $X = Y - Y = \{x - y : x, y \in Y\}$. Clearly $X$ is finite, rational, and symmetric. Define $x - y \geqslant 0$ to mean that $x \succsim y$. This is justified because if $x - y = x' - y'$, $x, y, x', y' \in Y$, then by (6), $x \succsim y$ if and only if $x' \succsim y'$. The desired result is now a direct consequence of Theorem 1.2.

Let $Z$ be a subset of $L$ which is closed under addition ($Z + Z \subseteq Z$). A binary relation $\succsim$ on $Z$ will be called *strictly monotonic* if the following three conditions are satisfied:

(i) $x \succsim y$ or $x \preccurlyeq y$,

(ii) $x_0 \succsim y_0$ and $x_1 \succsim y_1$ imply $x_0 + x_1 \succsim y_0 + y_1$,

(iii) $x_0 + x_1 = y_0 + y_1$ and $x_1 \succsim y_1$ imply $x_0 \preccurlyeq y_0$,

for all $x, y, x_0, y_0, x_1, y_1 \in Z$. For a subset $Y \subseteq L$, we let $Y^+$, the additive closure of $Y$, denote the least set $Z \supseteq Y$ closed under addition. Using this terminology, we can restate Theorem 1.3.

**THEOREM 1.4.** Let $Y$ be a finite rational subset of $L$. For a binary relation $\succsim$ on $Y$ to be realizable it is necessary and sufficient that it be extendable to a *strictly monotonic* relation on $Y^+$.

**PROOF.** Suppose $\succsim$ on $Y$ is realizable. Let $\varphi$ be a functional that realizes $\succsim$. Define $\succsim$ on $Y^+$ by the condition

$$x \succsim y \quad \text{if and only if} \quad \varphi(x) \geqslant \varphi(y)$$

for all $x, y \in Y^+$. Then the new $\succsim$ is obviously an extension of the old $\succsim$ on $Y$, and the linearity of $\varphi$ makes it trivial to verify (i), (ii), and (iii). Conversely, if we have the extension $\succsim$ to $Y^+$, we need only verify condition (6). Thus suppose that $x_i, y_i \in Y$, $x_i \succsim y_i$ for $i < n$, $n > 0$ and that $\sum_{i < n} x_i = \sum_{i < n} y_i$. If $n = 1$, then $x_0 = y_0$ and so $x_0 \preccurlyeq y_0$. If $n > 1$, then $\sum_{0 < i < n} x_i \succsim \sum_{0 < i < n} y_i$ in view of (ii). But

$$x_0 + \sum_{0 < i < n} x_i = y_0 + \sum_{0 < i < n} y_i ,$$

so $x_0 \preccurlyeq y_0$ by virtue of (iii).

One should not suppose that a strictly monotonic relation on $Y^+$ is realizable on $Y^+$. We have only shown that the *restriction* of $\succsim$ is realizable on the *finite* set $Y$. (Example: Let $L = E^2$, the two dimensional space, and let $Y = \{(1, 0), (0, 1)\}$. Let $\succsim$ be defined on $Y^+$ by the stipulation

$$(n_0, m_0) \succsim (n_1, m_1) \quad \text{if and only if} \quad n_0 > n_1 \quad \text{or} \quad n_0 = n_1 \quad \text{and} \quad m_0 \geqslant m_1 .$$

This is a non-Archimedean ordering of $Y^+$.)

**Reconciliation notes** (only where the passes diverged):

| Discrepancy | Resolution |
|---|---|
| Pass 1 omits `\in Y` after `$x, y, x', y'$` | Image confirms `\in Y`; Passes 2 & 3 |
| Summation subscripts `i<n` vs `i < n` | Image shows spaced subscripts; Passes 2 & 3 |
| Italic *on* in “realizable on $Y^+$” (Pass 2 only) | Image shows *on* not italicized; Passes 1 & 3 |
| Trailing comma/period spacing in display math | Image shows comma after second sum equation and period before closing parenthesis in the example |

<!-- page 6 -->

The content of Theorem 1.4 amounts to this well-known fact from algebra: *Every finite subset of an ordered abelian group can be isomorphically embedded in the additive group of reals.* Proof: let $G$ be the abelian group with $\oplus$ as the group operation and $\textcircled{\geqslant}$ as the ordering. Let $S = \{g_0, \cdots, g_{m-1}\}$ be the finite subset of $G$. For each $i < m$ let $U_i$ be the characteristic function of the subset $\{g_i\}$ of $S$. So $U_i \in L = L(S)$, and $Y = \{U_0, \cdots, U_{m-1}\}$ is rational. Further $Y^+$ has only *integer-valued* functions as elements. Define $\succcurlyeq$ on $Y^+$ by the condition that for $x, y \in Y^+$

$$x \succcurlyeq y \quad \text{if and only if}$$
$$x(g_0) \cdot g_0 \oplus \cdots \oplus x(g_{m-1}) \cdot g_{m-1} \textcircled{\geqslant} y(g_0) \cdot g_0 \oplus \cdots \oplus y(g_{m-1}) \cdot g_{m-1} .$$

It is obvious from the axioms for ordered abelian groups that $\succcurlyeq$ is a strictly monotonic relation on $Y^+$. Let $\varphi$ be some linear functional which realizes $\succcurlyeq$ on $Y$. The function $f$ on $S$ where

$$f(g_i) = \varphi(U_i)$$

is well-defined and, by construction, preserves the addition and order relations *within* the finite set $S$.

This trick of passing from an abstract structure to the "more concrete" vectors in a finite-dimensional linear space will now be consistently exploited for the solution of the three problems from measurement theory.

**II. SOLUTION TO THE PROBLEM OF INTRANSITIVE INDIFFERENCE**

Let $A$ be a finite nonempty set and let $P$ be a binary relation on $A$. For the purposes of this section we shall call $P$ *realizable* if there is a real-valued function $f$ on $A$ such that

$$xPy \quad \text{if and only if} \quad f(x) \geqslant f(y) + 1$$

for all $x, y \in A$. Realizable relations are obviously irreflexive, and so we shall assume $P$ is irreflexive.

Let $e$ be an element not in the finite set $A$ and set $S = A \cup \{e\}$. Each element $x \in S$ determines a vector in $L = L(S)$: namely, the characteristic function of $\{x\}$. To avoid clumsy notation, we shall identify each $x \in S$ with its corresponding vector and pretend that $S \subseteq L$. Thus $S$ becomes an *independent basis* for the $|S|$-dimensional space $L$.

We let $X$ be the subset of $L$ containing just the vectors of the forms $x - y - e$ or $y + e - x$, where $x, y \in A$. We define $\succcurlyeq 0$ by these stipulations:

(i) $x - y - e \succcurlyeq 0$ if and only if $xPy$;

(ii) $y + e - x \succcurlyeq 0$ if and only if not $xPy$;

<!-- page 7 -->

MEASUREMENT STRUCTURES AND LINEAR INEQUALITIES

for all $x, y \in A$. This is justified because $P$ is irreflexive. Obviously $X$ is a finite, rational, symmetric set. Further $u \succcurlyeq 0$ or $-u \succcurlyeq 0$ holds for all $u \in X$. We are now going to find necessary conditions on $P$ that will verify the conditions of Theorem 1.2 to make $\succcurlyeq 0$ realizable on $X$. Using such a realization we will then be able to show that the conditions are sufficient to make $P$ realizable in the sense of the present section.

Since $P$ is irreflexive, we see that this means that $e \succcurlyeq 0$ holds while $-e \succcurlyeq 0$ does not hold, in other words $e \succ 0$. Hence, assuming that $\succcurlyeq 0$ is realizable on $X$, we would have a linear functional $\varphi$ realizing $\succcurlyeq 0$ such that $\varphi(e) > 0$. Multiplying by a positive scalar, we can assume that $\varphi(e) = 1$. It follows at once that

$$xPy \quad \text{if and only if} \quad \varphi(x) \geqslant \varphi(y) + 1,$$

for $x, y \in A$. Hence $\varphi$ restricted to $A$ gives the realization of $P$. To complete the picture, we need now only find further necessary conditions on $P$ that will imply condition (2) of 1.2 for $\succcurlyeq 0$ as defined on $X$.

Suppose, therefore, that we have sequences $x_0, \cdots, x_{k-1}, y_0, \cdots, y_{k-1}, x'_0, \cdots, x'_{m-1}, y'_0, \cdots, y'_{m-1} \in A$ where $x_i P y_i$ holds for $i < k$, but not $x'_i P y'_i$ holds for $i < m$. We assume $k + m = n > 0$. If we can establish that in this situation the equation

$$\sum_{i < k} (x_i - y_i - e) + \sum_{i < m} (y'_i + e - x'_i) = 0$$

is *never valid*, then we will have indeed verified what amounts to condition (4) of Theorem 1.2.

Thus, by way of contradiction, let us assume that this last equation does hold for the indicated system of elements of $A$. We can rewrite the equation as

$$\sum_{i < k} (x_i - y_i) + \sum_{i < m} (y'_i - x'_i) + (m - k) \cdot e = 0.$$

Now the vector $e \in L$ is known to be *independent* of vectors in $A$, thus $m - k = 0$ and $m = k > 0$. In the equation

$$\sum_{i < k} (x_i - y_i) + \sum_{i < m} (y'_i - x'_i) = 0$$

only vectors from $A$ appear, and $A$ is an independent set of vectors. Unfortunately in the equation vectors can occur several times with both positive and negative coefficients. The best we can say in view of the independence of $A$ is that the two arrays of vectors

$$(x_0, \cdots, x_{k-1}, y'_0, \cdots, y'_{m-1})$$

and

$$(y_0, \cdots, y_{k-1}, x'_0, \cdots, x'_{m-1})$$

<!-- page 8 -->

are alike in that one is a *permutation* of the other. Let us make a tour through these arrays following out the permutation.

Start with $y_0$ in the lower array. Since $P$ is irreflexive, $x_0 \neq y_0$, so $y_0$ coincides with some other element in the upper array. Take the element in the lower array *directly under* the element in the upper array just considered. It must coincide with *some other* element in the upper array. Proceeding in this manner, passing from an element in the lower array to an equal element in the upper and then dropping to the corresponding element of the lower directly below this upper element, we shall eventually come back to our starting element $y_0$. We shall have traced out a *cycle*. There are two cases.

CASE 1. *The cycle never leaves the unprimed elements.* By a simple permutation of subscripts we can assume that we have an $l < k$, $l > 0$, such that

$$y_0 = x_1, y_1 = x_2, \cdots, y_{l-1} = x_l, y_l = x_0 ,$$

and that $x_i P y_i$ holds for all $i < k$, thus we have a cycle in $P$-relationships:

$$x_0 P x_1 P x_2 \cdots x_l P x_0 .$$

This can easily be ruled out by assuming that $P$ is *transitive*, so that $x_0 P x_0$ would follow contradicting the irreflexivity of $P$. If $P$ is realizable, then $P$ is necessarily transitive, because $\alpha \geqslant \beta + 1$ is obviously a transitive relation between real numbers.

CASE 2. *The cycle passes through primed and unprimed elements.* If the cycle starting with $y_0$ has *more* primed than unprimed elements, forget it. It cannot contain all the unprimed elements, because $k = m$. Start with an unused element $y_i$. Its cycle we may assume has both primed and unprimed elements, otherwise we are back in Case 1. Again, if there are more primed elements, start a new cycle. By this argument we may be sure that the cycle we obtain finally has *at least as many* unprimed elements as primed. Let us use the notation $y Q x$ as shorthand for *not* $x P y$. This time we will get a cycle of relationships which, after a change of subscripts, we can assume to be of the form

$$x_0 P x_1 \cdots x_l P y'_0 Q y'_1 \cdots y'_j Q x_{l+1} \cdots x_0 .$$

The number of $P$'s is the same as the number of $x$'s and the $Q$'s as the $y$'s; hence, there are at least as many $P$'s as $Q$'s. A degenerate case is $x_0 P y'_0 Q x_0$, which is the only case where there is only one $P$. This case is impossible because $y'_0 Q x_0$ means that *not* $x_0 P y'_0$. Thus we may assume there are at least two $P$'s.

Suppose there are two $P$'s adjacent in the cycle. The situation looks like

$$z P x P y Q w$$

or like

$$w Q z P x P y ,$$

<!-- page 9 -->

(where the letters $x, y, z, w$ now no longer refer to the arrays from which the cycle was obtained.) Assuming that $P$ is realizable by a function $f$ we would have in the first situation

$$f(z) \geqslant f(x) + 1, \quad f(x) \geqslant f(y) + 1, \quad \text{and} \quad f(y) + 1 > f(w).$$

Therefore $f(z) \geqslant f(w) + 1$, and $zPw$ would follow. In the second situation by a similar argument $wPy$ would follow. These *two* transitivity conditions are equivalent and are equivalent to the following implication

$$zPxPy \quad \text{implies} \quad wPy \quad \text{or} \quad zPw,$$

for $x, y, z, w \in A$. If we assume that $P$ has this necessary property, then our cycle of $P, Q$-relationships can be reduced to a *shorter cycle* where there are still as many $P$'s as $Q$'s.

Applying the above reasoning, we shall reduce the cycle either to one $P$ and one $Q$ (which is impossible) or to a cycle where there are no adjacent $P$'s. Since there are as many $P$'s as $Q$'s, there can be no pair of adjacent $Q$'s either. Thus a part of the cycle must look like

$$xPyQzPw.$$

Assuming that $f$ realizes $P$ on $A$ we have

$$f(x) \geqslant f(y) + 1 > f(z) \geqslant f(w) + 1,$$

whence $f(x) \geqslant f(w) + 1$ and so $xPw$. This means that if we assume about $P$ the necessary implication that

$$xPy \quad \text{and} \quad zPw \quad \text{implies} \quad xPw \quad \text{or} \quad zPy,$$

for $x, y, z, w \in A$, then our cycle can be reduced step by step to $xPx$ which is already assumed impossible. This completes the impossibility argument.

Notice in this last implication that if we substitute $y$ for $z$ and eliminate the false $yPy$, then $P$ is found to satisfy the transitive law. We can thus summarize this lengthy discussion as a theorem.

**THEOREM 2.1.** *Let $A$ be a finite nonempty set and let $P$ be a binary relation on $A$. For $P$ to be realizable it is necessary and sufficient that the conditions*

$(1_p)$ *not* $xPx$,

$(2_p)$ $xPy$ *and* $zPw$ *imply* $xPw$ *or* $zPy$,

$(3_p)$ $xPy$ *and* $zPx$ *imply* $wPy$ *or* $zPw$,

*hold for all* $x, y, z, w \in A$.

<!-- page 10 -->

It will be noted that in our argument we did not make full use of some *strict inequalities* that turned up. The reason is that we did not require the more definite information; indeed, the method gives a realization $f$ of $P$ where for all $x, y \in A$,

$$f(x) \geqslant f(y) + 1 \quad \text{if and only if} \quad f(x) > f(y) + 1$$

holds for all $x, y \in A$.

The author does not claim that the proof of Theorem 2.1 given here is particularly attractive. But he does feel that the relentless application of Theorem 1.2 gave the required solution without having to know the answer in advance—that by elementary combinatorial analysis the result was systematically uncovered.

## III. SOLUTION TO THE PROBLEM OF ORDERED DIFFERENCES

Before presenting the solution to Problem II, we shall treat a related, but simpler, question which also has independent interest.

Let $A$ and $A^*$ be two finite nonempty sets, and let $V$ be a quaternary relation which we treat as a binary relation on the cartesian product $A \times A^*$. Think of $A$ and $A^*$ as sets of two different kinds of commodities, and interpret $x x^* V y y^*$, where $x, y \in A$, $x^*, y^* \in A^*$, to mean that the combination of $x$ and $x^*$ is *more valuable than* the combination of $y$ and $y^*$. The question about these structures is whether there exist real-valued functions $f$ and $f^*$ on $A$ and $A^*$, respectively, that realize $V$ in the sense that

$$x x^* V y y^* \quad \text{if and only if} \quad f(x) + f^*(x^*) \geqslant f(y) + f^*(y^*),$$

for all $x, y \in A$, $x^*, y^* \in A^*$. Such a pair $f, f^*$ of functions is called a pair of *utility functions* for $V$. Thinking of $f$ and $f^*$ as assigning values to the commodities, the interpretation of $V$ as an ordering of the combinations is clear. Of course, we are treating the situation with the philosophy that “the whole is equal to the sum of its parts”; hence, a straightforward adding of utilities in finding the utility of a combination is assumed to be subtle enough for the present theory.

We shall now apply our general Theorem 1.3 to characterize the relations $V$ realizable in the above sense. To this end let $S = A \cup A^*$ be the finite set determining the linear space $L = L(S)$. As in Section II we identify $S$ with the set of basis vectors for $L$ in the obvious way. We let

$$Y = \{x + x^* : x \in A, x^* \in A^*\}.$$

Without loss of generality we can assume that the sets $A$ and $A^*$ are *disjoint*, so that $Y$ is in a one-one correspondence with the set $A \times A^*$. We define $\geqslant$ on $Y$ in the inescapable way for $x, y \in A$, $x^*, y^* \in A^*$:

$$x + x^* \geqslant y + y^* \quad \text{if and only if} \quad x x^* V y y^*.$$

<!-- page 11 -->

MEASUREMENT STRUCTURES AND LINEAR INEQUALITIES

It is immediate that the binary relation $\geqslant$ is realizable on the finite rational set $Y$ (in the sense of Section I) if and only if $V$ is realizable on $A$ by a pair of utility functions.

Considering Theorem 1.3, we need now only transcribe conditions (5) and (6) into equivalent conditions about $V$. There is no problem about (5): we must assume the relation $V$ has the property that $x x^* V y y^*$ or $y y^* V x x^*$ holds for all $x, y \in A, x^*, y^* \in A^*$.

For property (6), assume we have elements satisfying the equation

$$\sum_{i < n} (x_i + x_i^*) = \sum_{i < n} (y_i + y_i^*)$$

where $x_i, y_i \in A, x_i^*, y_i^* \in A^*$ and $x_i x_i^* V y_i y_i^*$ holds for $i < n$ and $n > 0$. We require conditions on $V$ so that $y_0 y_0^* V x_0 x_0^*$ follows from these assumptions.

Now in the linear space $L$, remember that the vectors in $S = A \cup A^*$ are independent of each other. Hence, for the above equation to be valid, we must have

$$\sum_{i < n} x_i = \sum_{i < n} y_i \quad \text{and} \quad \sum_{i < n} x_i^* = \sum_{i < n} y_i^*,$$

because the sets $A$ and $A^*$ are assumed disjoint. In other words, there must exist a pair $\pi, \sigma$ of permutations of the indices $\{0, 1, \cdots, n - 1\}$ such that the equations

$$y_i = x_{\pi(i)} \quad \text{and} \quad y_i^* = x_{\sigma(i)}^*$$

hold for $i < n$. Therefore, the required assumption about $V$ states that $x_i x_i^* V x_{\pi(i)} x_{\sigma(i)}^*$ for $i < n$ implies $x_{\pi(0)} x_{\sigma(0)}^* V x_0 x_0^*$, where $n > 0$, $\pi$ and $\sigma$ are permutations of $\{0, 1, \dots, n - 1\}$, and $x_i \in A, x_i^* \in A^*$ for $i < n$. (Actually the hypothesis of this implication is too strong. In view of the other assumption on $V$, we need only take $i > 0$ in the hypothesis of the second assumption.) It should be clear to everyone that these two conditions are necessary for $V$ to be realizable, and that 1.3 shows conversely the sufficiency. We can therefore state the desired theorem.

**THEOREM 3.1.** *Let $A$ and $A^*$ be two finite nonempty sets and let $V$ be a binary relation on $A \times A^*$. For $V$ to be realizable by a pair of utility functions on $A$ and $A^*$ it is necessary and sufficient that the conditions*

$$(1_V) \quad x x^* V y y^* \quad \text{or} \quad y y^* V x x^*,$$

$$(2_V) \quad x_i x_i^* V x_{\pi(i)} x_{\sigma(i)}^* \quad \text{for} \quad i < n, \; i > 0, \quad \text{implies} \quad x_{\pi(0)} x_{\sigma(0)}^* V x_0 x_0^*,$$

*hold for all $x, y \in A, x^*, y^* \in A^*$ and all sequences $x_0, \dots, x_{n-1} \in A, x_0^*, \dots, x_{n-1}^* \in A^*$ and all permutations $\pi, \sigma$ of $\{0, \dots, n - 1\}$, where $n > 0$.*

We do not need to assume that $A$ and $A^*$ are disjoint. That assumption was only a technical device in the proof to obtain *two* utility functions from *one* linear functional on $L = L(S) = L(A \cup A^*)$.

<!-- page 12 -->

SCOTT

It is mildly amusing to note how condition $(2_V)$ implies that $V$ is transitive. Suppose $x x^* V y y^*$ and $y y^* V z z^*$ both hold. Let $x_0 = z$, $x_1 = x$, $x_2 = y$, and $x_0^* = z^*$, $x_1^* = x^*$, $x_2^* = y^*$. Let $\pi(i) = \sigma(i) = i + 1 \pmod 3$. Then by $(2_V)$ we see that $x_1 x_1^* V x_0 x_0^*$ holds; that is, $x x^* V z z^*$ holds as required.

Turning now to the ordered differences, we have in this case only *one* finite non-empty set $A$ and a quaternary relation $D$ on $A$ (that is, a binary relation on $A \times A$). The problem is to characterize those $D$ realizable by a single utility function $f$ on $A$ such that

$$xy D zw \quad \text{if and only if} \quad f(x) - f(y) \geqslant f(z) - f(w)$$

for all $x, y, z, w \in A$.

Note that if we define a relation $V$ in terms of $D$ by the condition

$$xw V zy \quad \text{if and only if} \quad xy D zw$$

for all $x, y, z, w \in A$, then $D$ is also definable in terms of $V$. Further, if $D$ is realizable in the sense just defined, then $V$ is realizable in the sense of Theorem 3.1 where $A = A^*$ and the two utility functions coincide. Suppose we assume $(1_V)$ and $(2_V)$ of Theorem 3.1, which can be equivalently rewritten in terms of $D$. (By the remark just made, these are necessary conditions for $D$ to be realizable.) In view of Theorem 3.1 there must exist a *pair* of utility functions on $A$, which we shall call $g$ and $h$, such that

$$xy D zw \quad \text{if and only if} \quad g(x) - h(y) \geqslant g(z) - h(w)$$

for all $x, y, z, w \in A$. Unfortunately, $g$ and $h$ need not be the same function, so the problem is not yet solved.

To complete the solution, we note that not all necessary conditions for $D$ to be realizable by a single utility function have yet been appreciated. In particular, there is an obvious *commutativity* condition that $D$ must satisfy to be realizable:

$$xy D zw \quad \text{implies} \quad wz D yx$$

for all $x, y, z, w \in A$. Assuming this property we see that if $xy D zw$ holds, then

$$g(x) - h(y) \geqslant g(z) - h(w)$$

and

$$g(w) - h(z) \geqslant g(y) - h(x).$$

Therefore,

$$h(x) - g(y) \geqslant h(z) - g(w),$$

and so, by adding inequalities,

$$[g(x) + h(x)] - [g(y) + h(y)] \geqslant [g(z) + h(z)] - [g(w) + h(w)].$$

<!-- page 13 -->

MEASUREMENT STRUCTURES AND LINEAR INEQUALITIES

Similarly, if $xy \mathrel{D} zw$ does not hold, then neither does $wz \mathrel{D} yx$. Whence, we find that

$$g(x) - h(y) < g(z) - h(w),$$

and

$$g(w) - h(z) < g(y) - h(x),$$

and so

$$[g(x) + h(x)] - [g(y) + h(y)] < [g(z) + h(z)] - [g(w) + h(w)].$$

In other words, define the function $f$ on $A$ so that $f(x) = g(x) + h(x)$ for all $x \in A$, then $f$ realizes $D$ in the required sense. This discussion leads directly to our main result.

**THEOREM 3.2.** *Let $A$ be a finite nonempty set and let $D$ be a quaternary relation on $A$. For $D$ to be realizable by a single utility function on $A$ it is necessary and sufficient that the conditions*

$$(1_D) \quad xy \mathrel{D} zw \quad \text{or} \quad zw \mathrel{D} xy,$$

$$(2_D) \quad x_i y_i \mathrel{D} x_{\pi(i)} y_{\sigma(i)} \quad \text{for} \quad i < n, \; i > 0, \quad \text{implies} \quad x_{\pi(0)} y_{\sigma(0)} \mathrel{D} x_0 y_0,$$

$$(3_D) \quad xy \mathrel{D} zw \quad \text{implies} \quad wz \mathrel{D} yx,$$

*hold for all $x, y, z, w \in A$ and all sequences $x_0, \dots, x_{n-1}, y_0, \dots, y_{n-1} \in A$ and all permutations $\pi, \sigma$ of $\{0, \dots, n - 1\}$, where $n > 0$.*

It should be remarked that $(2_D)$ is an infinite bundle of conditions (for each $n > 0$, each $\pi, \sigma$), and it was shown in Scott and Suppes (1958), that no finite number of them could be sufficient.

## IV. SOLUTION TO THE PROBLEM OF SUBJECTIVE PROBABILITIES

Let $B$ be a finite Boolean algebra that we can call the algebra of *events*. A binary relation $\succcurlyeq$ is given on $B$, where $x \succcurlyeq y$ means that the event $x$ is *more probable than* the event $y$ in some subjective sense. We wonder if these subjective decisions about probabilities are *rational* in the sense that $\succcurlyeq$ is realizable by some real-valued probability measure $\mu$ on $B$ where

$$x \succcurlyeq y \quad \text{if and only if} \quad \mu(x) \geqslant \mu(y)$$

for all $x, y \in B$.

<!-- page 14 -->

It seems that de Finetti first raised this question and proposed these obviously necessary axioms for $\succcurlyeq$ for all $x, y, z, w \in B$:

(i) not $0 \succcurlyeq 1$,

(ii) $x \succcurlyeq 0$,

(iii) $x \succcurlyeq y$ or $y \succcurlyeq x$,

(iv) $x \succcurlyeq y \succcurlyeq z$ implies $x \succcurlyeq z$,

(v) $x \succcurlyeq y$ if and only if $x \cup z \succcurlyeq y \cup z$,

in case $z$ is disjoint from both $x$ and $y$.

It was shown in Kraft, Pratt, and Seidenberg (1959) by an ingenious counter-example in a 32-element Boolean algebra that the axioms (i)–(v) are *not* sufficient. The proper strengthening of the axioms was also given in Theorem 2 of that paper and we shall derive what amounts to their result as a consequence of Theorem 1.3.

Let $S$ be the (finite) set of atoms of $B$. In the well-known way, we can identify $B$ with the set of $\{0, 1\}$-valued functions on $S$ (that is, the set of characteristic functions of subsets of $S$.) Thus we imagine that $B$ is a subset of $L = L(S)$, and so the 0 element of $B$ is the 0 vector of $L$, the 1 element of $B$ is the vector with coordinates all equal to 1. Further if $x, y \in B$ are disjoint, then the vector sum $x + y = x \cup y$. Of course, if $x, y \in B$ overlap, then $x + y \notin B$. We shall write $x \succ y$ for not $y \succcurlyeq x$ and $x \preccurlyeq y$ for $y \succcurlyeq x$. With these conventions the desired result can be formulated as follows:

**THEOREM 4.1.** *Let $B$ be a finite Boolean algebra and let $\succcurlyeq$ be a binary relation on $B$. For $\succcurlyeq$ to be realizable by a probability measure on $B$ it is necessary and sufficient that the conditions*

$$(1_B) \quad 1 \succ 0,$$

$$(2_B) \quad x \succcurlyeq 0,$$

$$(3_B) \quad x \succcurlyeq y \quad \text{or} \quad x \preccurlyeq y,$$

$$(4_B) \quad x_0 + x_1 + \cdots + x_{n-1} = y_0 + y_1 + \cdots + y_{n-1} \quad \text{implies} \quad x_0 \preccurlyeq y_0,$$

*hold for all $x, y \in B$ and all sequences $x_0, \dots, x_{n-1}, y_0, \dots, y_{n-1} \in B$, where $x_i \succcurlyeq y_i$ for $i < n$, $i > 0$, and $n > 0$.*

The unpleasant feature of $(4_B)$ is that it is not a strictly Boolean condition: $x_0 + x_1 + \cdots + x_{n-1}$ means the *algebraic sum* of characteristic functions and *does not* stand for the *union* of the $x_i$. However, the equation in the hypothesis of $(4_B)$ does have a reasonably simple interpretation in words: every point (atom) belongs to exactly the same number of the $x_i$ as the $y_i$.

**PROOF OF THEOREM 4.1.** There is no question that the conditions are necessary. To apply Theorem 1.3, we simply take $Y = B$. Thus there will be a linear functional $\varphi$ on $L$ that realizes $\succcurlyeq$ on $B$. In view of $(1_B)$ we have $\varphi(1) > 0$; while $\varphi(x) \geqslant 0$ for

<!-- page 15 -->

$x \in B$ follows from $(2_B)$. Then the measure $\mu$ we are looking for is defined by the equation:

$$\mu(x) = \varphi(x)/\varphi(1)$$

for all $x \in B$.

This argument shows that Theorem 4.1 is almost immediately a special case of Theorem 1.3. If we had left out $(1_B)$ and $(2_B)$, the best we could have said is that $\succcurlyeq$ is realized by a *signed* measure on $B$.

The derivation of (v) from $(3_B)$ and $(4_B)$ is quite easy. Suppose $x \succcurlyeq y$ but not $x + z \succcurlyeq y + z$. Then $y + z \succcurlyeq x + z$ and $(y + z) + x = (x + z) + y$. So by $(4_B)$ $y + z \preccurlyeq x + z$ must indeed hold. The converse is analogous.

The author has obtained an extension of Theorem 4.1 to infinite Boolean algebras by using the Hahn-Banach Theorem in the same way that it was applied in Kelley (1959), where the problem of the existence of strictly positive measures was solved. If the result proves to be of interest, it will be published in a future paper.

## REFERENCES

ADAMS, E. W., AND FAGOT, R. F. A model of riskless choice. *Rep. No. 4, Applied Mathematics and Statistics Laboratory, Stanford University*, 1956.

LUCE, R. D. Semi-orders and a theory of utility discrimination. *Econometrica*, 1956, **24**, 178-191.

LUCE, R. D., AND TUKEY, J. W. Simultaneous conjoint measurement: a new type of fundamental measurement. *J. math. Psychol.*, 1964, **1**, 1-27.

KELLEY, J. L. Measures on Boolean algebras. *Pacific J. Math.*, 1959, **18**, 1165-1172.

KRAFT, C. H., PRATT, J. W., AND SEIDENBERG, A. Intuitive probability on finite sets. *Ann. Math. Statist.*, 1959, **30**, 408-419.

KUHN, H. W., AND TUCKER, A. W. (Eds.) Linear inequalities and related systems. *Annals of mathematics studies*, No. 38, 1956.

SCOTT, D., AND SUPPES, P. Foundational aspects of theories of measurement. *J. Symbolic Logic*, 1958, **23**, 113-128.

SUPPES, P., AND ZINNES, J. L. Basic measurement theory. *Handbook of mathematical psychology*, Vol. 1. New York: Wiley, 1963. Pp. 1-76.

RECEIVED : September 20, 1963
