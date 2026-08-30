---
source_pdf: KraftPrattSeidenberg1958.pdf
ocr_method: cursor-vision-triple-merge
verification_status: draft
---

# Transcription (LLM vision OCR)


<!-- page 1 -->

# INTUITIVE PROBABILITY ON FINITE SETS¹

**BY CHARLES H. KRAFT, JOHN W. PRATT, AND A. SEIDENBERG**

*Michigan State University, University of Chicago and Harvard University, and University of California (Berkeley)*

**1. Introduction.** Let $x_1, \cdots, x_n$ be the distinct elements of a set $S$. By assigning nonnegative numbers $v(x_i)$ to the $x_i$ and $v(x_{i_1}) + \cdots + v(x_{i_s})$ to the set $\{x_{i_1}, \cdots, x_{i_s}\}$, we obtain an ordering of the subsets of $S$, namely, the subsets are ordered in accordance with the values as just assigned.² We denote by $v(\alpha)$ the value assigned to $\alpha$, and write $\alpha \prec \beta$ if $v(\alpha) \leqq v(\beta)$. For this ordering the following conditions obtain:

*Comparability (C):* For any $\alpha$, $\beta$, $\alpha \prec \beta$ or $\beta \prec \alpha$ (or both).

*Transitivity (T):* $\alpha \prec \beta$ and $\beta \prec \gamma$ implies $\alpha \prec \gamma$

*Additivity (A):* Let $\gamma$ be disjoint from $\alpha$, $\beta$; then $\alpha \prec \beta$ if and only if

$$\alpha \cup \gamma \prec \beta \cup \gamma.$$

Also $\phi \prec \gamma$ for every $\gamma$, where $\phi$ is the empty set.

Let $T$ be the set of subsets of $S$. We shall say that an ordering of $T$ obtained by assigning values to the $x_i$ *arises from a measure*. Conversely, B. de Finetti [1] (see also [4], p. 40) has asked whether every ordering of $T$ subject to the above conditions arises from a measure; and moreover has conjectured that it does; but we show by a counter-example that the conjecture is false for $n = 5$. In Theorem 2 we give a necessary and sufficient condition that an ordering arises from a measure; the proof includes a procedure for checking in a finite number of steps whether the condition obtains.

The connection with intuitive probability (i.e., the axiomatic theory of probability) is as follows: one has $n$ incompatible events $x_1, \cdots, x_n$; and one supposes that one can confront the disjunction of any subset of them with the disjunction of any other, being able to say (or judge) whether they are equally likely, and if not, which is the more likely. Thus one has a transitive ordering of $T$; moreover, this ordering is subject to the additivity condition (and, if one likes, to any further conditions similar to the above which obtain for an ordering arising from a measure). The question then is whether one can assign a numerical probability to the event $x_i$ in such a way that the corresponding ordering of $T$ coincides with the given ordering; or in other words, whether there exists a *strictly agreeing measure*. As said, the answer is *no*.

---

Received March 14, 1958; revised November 22, 1958.

¹ Prepared with partial support of the Office of Naval Research to the first two named authors. This paper may be reproduced in whole or in part for any purpose of the United States Government.

² By an *ordering* of a set $S$ we mean an arbitrary, possibly empty, subset of the Cartesian product $S \times S$, that is, an arbitrary set of ordered pairs $(a, b)$ with $a$, $b$ elements of $S$. If $(a, b)$ is such a pair, we write $a \prec b$. An ordering is sometimes also called a relation.

<!-- page 2 -->

INTUITIVE PROBABILITY ON FINITE SETS

In ([1] Section 3, p. 3), de Finetti suggests that if the answer to his conjecture should be *no*, then this is because the “right” axioms haven’t been put down. In Theorem 5, we show that if we subject our judgment to certain conditions of the same general character as (C), (T), and (A), then we will, in fact, reject any ordering which does not arise from a measure. The counter-example is thus only a partial answer to de Finetti’s conjecture; and Theorem 5 completes the answer.

The question of *almost agreeing measures* (see definition below) is also taken up. A counter-example is given to show that an ordering can be subject to (C), (T), (A) without having any almost agreeing measure.

For a systematic treatment of intuitive probability see [4] and the literature there cited, in particular, [3].

**2. Preliminaries.** We designate the subsets of $S$ multiplicatively: thus $x_1 x_2 x_3$, for example, is the set consisting of the elements $x_1, x_2, x_3$. The empty set is designated by $1$. The set $T$ of subsets of $S$ is thus identified with the monomials in $n$ indeterminates $x_1, \ldots, x_n$ in which the exponents are $0$ or $1$. In the standard terminology for polynomials, the intersection $\delta$ of two sets $\alpha$, $\beta$ is their greatest common divisor. The product $\alpha\beta$ need not be in $T$; in fact it will be in $T$ if and only if $\delta = 1$. The union of two sets $\alpha$, $\beta$ is $\alpha\beta/\delta$.

In addition to the monomials in $T$, it is convenient to consider the group $G$ of monomials $x_1^{i_1} \cdots x_n^{i_n}$, $i_1, \ldots, i_n$ arbitrary integers; and extend the measure $v$ on $T$ to $G$ in such a way that $v(\alpha\beta) = v(\alpha) + v(\beta)$. There is, in fact, one and only one way to make this extension, namely, by placing $v(x_1^{i_1} \cdots x_n^{i_n}) = i_1 v(x_1) + \cdots + i_n v(x_n)$. We will call a mapping $\alpha \mapsto v(\alpha)$ of $G$ into the additive group of real numbers for which $v(\alpha\beta) = v(\alpha) + v(\beta)$ a *valuation*. There is thus a $1$–$1$ correspondence between measures and the valuations in which $v(x_i) \geqq 0$ for every $i$, and such valuations could, without great confusion, be called measures.

Let $v$ be a valuation of $G$, corresponding to a measure, and giving rise to an ordering of $T$. In addition to the conditions (C), (T), (A), there are several other obvious conditions that one can write down. For example: if $\alpha \prec \beta$ and $\gamma \prec \delta$, then $\alpha\gamma \prec \beta\delta$. Here, even if $\alpha, \beta, \gamma, \delta$ are in $T$, $\alpha\gamma$ and $\beta\delta$ need not be. In order to confine ourselves to $T$, we consider the case that $\alpha, \beta, \gamma, \delta$ are in $T$ and there exists a monomial $\epsilon$ such that $\alpha\gamma/\epsilon$ and $\beta\delta/\epsilon$ are in $T$. The question then is whether (C), (T), (A) imply that $\alpha\gamma/\epsilon < \beta\delta/\epsilon$. A *priori* either this implication can be established in a purely formal way, or it cannot, and if it cannot, the question is whether intuition requires the conclusion $\alpha\gamma/\epsilon < \beta\delta/\epsilon$. For the time being, we need not enter into considerations of the latter kind, as we have the following theorem. We write $\alpha < \beta$ if $\alpha \prec \beta$ obtains but $\beta \prec \alpha$ does not obtain.

**THEOREM 1.** *On $T$ let there be a relation $(\prec)$ subject to the conditions (T), (A). If $\alpha, \beta, \gamma, \delta$ are in $T$ and there is a monomial $\epsilon$ such that $\alpha\gamma/\epsilon$ and $\beta\delta/\epsilon$ are in $T$, then $\alpha \prec \beta$ and $\gamma \prec \delta$ implies $\alpha\gamma/\epsilon \prec \beta\delta/\epsilon$. If in addition $\alpha < \beta$ or $\gamma < \delta$, then $\alpha\gamma/\epsilon < \beta\delta/\epsilon$.*

<!-- page 3 -->

C. H. KRAFT, J. W. PRATT, AND A. SEIDENBERG

**PROOF.** First suppose $\alpha$, $\beta$ have greatest common divisor $1$ and $\gamma$, $\delta$ have greatest common divisor $1$. Then also g.c.d. $(\alpha, \gamma) = 1$ and g.c.d. $(\beta, \delta) = 1$. For if, say, $x_1$ were a factor of $\alpha$ and $\gamma$, then it would not be a factor of $\beta$ or $\delta$, and there could exist no $\epsilon$ such that $\alpha\gamma/\epsilon$ and $\beta\delta/\epsilon$ would be in $T$; similarly with $\beta$, $\delta$. Writing

$$\alpha = \alpha'\delta_1, \quad \gamma = \gamma'\gamma_1, \quad \beta = \beta'\gamma_1, \quad \delta = \delta'\delta_1,$$

$$\gamma_1 = \text{g.c.d. } (\beta, \gamma), \quad \delta_1 = \text{g.c.d. } (\alpha, \delta),$$

one finds $\gamma'\alpha \prec \gamma'\beta = \beta'\gamma \prec \beta'\delta$ and $\gamma'\alpha \prec \beta'\delta$, from which $\alpha\gamma/\epsilon \prec \beta\delta/\epsilon$ follows. In the general case, let $\lambda = \text{g.c.d. } (\alpha, \beta)$, $\mu = \text{g.c.d. } (\gamma, \delta)$. Then $\alpha/\lambda \prec \beta/\lambda$, $\gamma/\mu \prec \delta/\mu$, by additivity; also $(\alpha/\lambda)(\gamma/\mu)/(\epsilon/\lambda\mu)$ and $(\beta/\lambda)(\delta/\mu)/(\epsilon/\lambda\mu)$ are in $T$. By the first part of the proof, we now have $(\alpha/\lambda)(\gamma/\mu)/(\epsilon/\lambda\mu) \prec (\beta/\lambda)(\delta/\mu)/(\epsilon/\lambda\mu)$, that is, $\alpha\gamma/\epsilon \prec \beta\delta/\epsilon$.

For the second part of the theorem, keeping in mind that $\lambda \prec \mu$, $\mu \prec \nu$ and $\nu \prec \lambda$ implies $\mu \prec \lambda$, $\nu \prec \mu$, $\lambda \prec \nu$, and assuming $\beta'\delta \prec \gamma'\alpha$, we obtain $\gamma'\beta \prec \gamma'\alpha$, $\beta'\delta \prec \beta'\gamma$, whence $\beta \prec \alpha$ and $\delta \prec \gamma$. Thus if $\alpha < \beta$ or $\gamma < \delta$, then $\gamma'\alpha \prec \beta'\delta$; and $\alpha\gamma/\epsilon < \beta\delta/\epsilon$ follows.

We shall have occasion to refer to the following condition:

*Generalized Additivity* (GA): If $\alpha_i \prec \beta_i$, $i = 1, \cdots, s$, and $\prod \alpha_i$, $\prod \beta_i$ are in $T$, then $\prod \alpha_i \prec \prod \beta_i$. If in addition $\alpha_i < \beta_i$ for some $i$, then $\prod \alpha_i < \prod \beta_i$.

**COROLLARY TO THEOREM 1.** *Let $T$ be ordered by a relation subject to the conditions (T), (A). Then (GA) also obtains.*

The proof is by induction on $s$. On the other hand, if one drops the assumption that $\prod \alpha_i$, $\prod \beta_i$ are in $T$ and assumes only that there is a monomial $\epsilon$ such that $\prod \alpha_i/\epsilon$, $\prod \beta_i/\epsilon$ are in $T$, then (even assuming (C)) one cannot conclude, as we shall see from the counter-example below, that $\prod \alpha_i/\epsilon < \prod \beta_i/\epsilon$.$^3$

**3. Agreeing and almost agreeing measures.** Let $T_1$ be an arbitrary set of monomials, with exponents possibly negative, and let $<$, $\prec$ be two completely arbitrary order relations on $T_1$. Of these relations individually taken we assume nothing, not even transitivity; in other words, we have given, for $<$ say, a set $R$ of pairs: $R = \{(\alpha, \beta) \mid \alpha, \beta \in T_1\}$, and we write $\alpha < \beta$ if $(\alpha, \beta) \in R$; similarly for $\prec$ there is a set of pairs $S$. Although $S \subseteq R$ need not be assumed for what follows, for slight notational conveniences which will involve practically no loss of generality, we assume that $\alpha \prec \beta$ implies $\alpha < \beta$. We refer to the completely arbitrary ordering $(<, \prec)$, and say it arises from the valuation $v$ if $\alpha \prec \beta$ implies $v(\alpha) \leqq v(\beta)$ and $\alpha < \beta$ implies $v(\alpha) < v(\beta)$.

Let us write (for arbitrary monomials $\alpha$, $\beta$) $\alpha \prec \beta$ if $\alpha = \prod \alpha_i$, $\beta = \prod \beta_i$, $\alpha_i, \beta_i \in T_1$, $\alpha_i < \beta_i$, $i = 1, \cdots, s$; and $\alpha < \beta$ if in addition $\alpha_i \prec \beta_i$ for at least one $i$. If the given ordering arises from a valuation, then clearly $\epsilon \prec \epsilon$ for no $\epsilon$.

---

$^3$ Below we shall have $qs \prec p$, $pq \prec rs$, $ps \prec tq$, but not $spq = (qs)(pq)(ps)/spq \prec (p)(rs)(tq)/spq = rt$.
