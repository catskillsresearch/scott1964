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

<!-- page 4 -->

INTUITIVE PROBABILITY ON FINITE SETS

**DEFINITION.** *A completely arbitrary ordering of $T_1$ will be said to be compatible with a valuation if $\epsilon \prec \epsilon$ holds for no $\epsilon$. (In terms of the originally given relations, the condition $\epsilon \prec \epsilon$ holds for some $\epsilon$ can be expressed as follows: there exists a relation $\prod(\beta_i/\alpha_i) = 1$, with $\alpha_i, \beta_i$ in $T_1$, $\alpha_i < \beta_i$ each $i$, and $\alpha_i \prec \beta_i$ for at least one $i$.)*

**THEOREM 2.** *A completely arbitrary ordering of $T_1$, an arbitrary finite set of monomials, arises from a valuation if (and, trivially, only if) it is compatible with a valuation.*

For the proof it will be convenient to separate out the following lemma.

**LEMMA 0.** *(a). Given an arbitrary finite system of linear equalities and inequalities $\{l_i > 0, l_j' = 0, l_k'' \geqq 0\}$, where the $l_i$, $l_j'$, $l_k''$ are linear forms in indeterminates $x_1, \cdots, x_n$ with rational coefficients, one has an algorithm for deciding whether the system has a solution, and if it does, for finding one.*

*(b). The system $\{l_i > 0, l_j' = 0, l_k'' \geqq 0\}$ of (a) has a solution if (and, trivially, only if) the following hypothesis obtains:*

*(H): for no rational $\lambda_i \geqq 0$, $\mu_j$, $\nu_k \geqq 0$, $\lambda_i > 0$ for at least one $i$, does the linear form $L = \sum \lambda_i l_i + \sum \mu_j l_j' + \sum \nu_k l_k''$ equal zero (that is, have all its coefficients equal to zero).$^4$*

**PROOF OF THE LEMMA.** The idea of the proof of (b) is as follows: each step of the algorithm of (a) leads to a finite number of other systems of similar form, the disjunction of which is equivalent with the given system; moreover, the hypothesis (H) carries over, at each step, to at least one of the resulting systems. Ultimately the indeterminates $x_1, \cdots, x_n$ are eliminated, and (b) follows by verifying it, as one does trivially, in the case that there are no $x_i$.

As for the proof itself: if an inequality $l_1'' \geqq 0$ occurs, we can write the system as the disjunction of the following two systems:

$$(1)\quad \{l_i > 0, l_1'' > 0; l_j' = 0; l_k'' \geqq 0, \cdots \}$$

$$(2)\quad \{l_i > 0; l_j' = 0, l_1'' = 0; l_k'' \geqq 0, \cdots \}.$$

One sees without difficulty that the hypothesis (H) carries over to at least one of these two systems.$^5$ Therefore we may suppose all the inequalities (and equalities) to be of the form $l_i > 0$ or $l_j' = 0$. If now an equality $l_j' = 0$ occurs

---

$^4$ If in (H) we had the word *real* instead of *rational*, this would follow directly from ([2], p. 26, Criterion III); moreover, by Corollary 2 below, a system of linear inequalities with rational coefficients which has a real solution must also have a rational solution; and the theorem follows. Since theorems on linear inequalities are linked in an intimate way with facts about convex sets (see [2]), a knowledge of these facts renders the theorems transparent; but the fact is that in taking care of the additional point just mentioned, one can by-pass entirely the consideration of convex sets. With slight modifications, our proof of Theorem 2 yields quite simple proofs of all the theorems on inequalities given in ([2], pp. 23–28); in this connection, see Theorem 3, below.

$^5$ If it didn't, we would have an identity of the form $\sum \lambda_i l_i + \sum \mu_j l_j' + \sum \nu_k l_k'' = 0$, $\lambda_i \geqq 0$, $\nu_k \geqq 0$, and $\nu_1 > 0$, say $\nu_1 = 1$; and another such identity with $\lambda_i \geqq 0$, some $\lambda_i > 0$, $\nu_k \geqq 0$ for $k \geqq 2$, and $\nu_1 < 0$, say $\nu_1 = -1$. Adding the two identities gives an identity contradicting the hypothesis (H).

<!-- page 5 -->

C. H. KRAFT, J. W. PRATT, AND A. SEIDENBERG

and actually involves some letter $x_1$, we can use this relation to eliminate $x_1$. It is immediate that the hypothesis (H) carries over to the resulting system. Hence we may suppose only inequalities of the form $l_i > 0$ to occur. The system being of the form $\{l_i > 0\}$, we write it, relative to some $x_1$ that actually occurs, in the form $\{m_u - x_1 > 0, x_1 - m_v' > 0, m_w'' > 0\}$, where the $m_u$, $m_v'$, $m_w''$ are forms in $x_2, \cdots, x_n$. Necessary and sufficient for this system to have a solution is that the system $\{m_u - m_v' > 0, m_w'' > 0\}$ have a solution: in fact, if $\bar{x}_2, \cdots, \bar{x}_n$ is a solution of this system, then $\min m_u(\bar{x}) > \max m_v'(\bar{x})$; and taking $\bar{x}_1$ arbitrarily between these numbers we get a solution $\bar{x}_1, \cdots, \bar{x}_n$ of the original system. Moreover the hypothesis (H) carries over to the system in $x_2, \cdots, x_n$ as one easily sees. Hence the proof is complete by induction, subject to the verification for $n = 0$.

**PROOF OF THEOREM 2.** The theorem is seen to be a corollary of the lemma upon rewriting the theorem in additive form. If, namely, in any valuation, $x_j$ gets the value $\bar{x}_j$, then $\prod x_j^{r_j}$ gets the value $\sum r_j \bar{x}_j$. Let $\alpha = \prod x_j^{r_j}$, $\beta = \prod x_j^{s_j}$. Then $\alpha \prec \beta$ yields $\sum (s_j - r_j)\bar{x}_j \geqq 0$; $\alpha < \beta$ yields $\sum (s_j - r_j)\bar{x}_j > 0$. Corresponding to the power product $\beta/\alpha$, consider the linear form $l = \sum (s_j - r_j)x_j$ (in indeterminates $x_j$). Let $\{l_i\}$ be the set of linear forms arising from $\beta/\alpha$ with $\alpha < \beta$; $\{l_k''\}$, the set of linear forms arising from $\beta/\alpha$ with $\alpha \prec \beta$. The assertion that the ordering arises from a valuation thus comes to saying that the system $\{l_i > 0, l_k'' \geqq 0\}$ has a solution. A condition $\prod(\beta_g/\alpha_g) = 1$ rewritten in additive form becomes: $\sum l_g = 0$, that is, the linear form $L = \sum l_g$ has all its coefficients equal to zero. The compatibility condition can then be stated as follows: for no integral $\lambda_i \geqq 0$, $\nu_k \geqq 0$, $\lambda_i > 0$ for at least one $i$, does the linear form $L = \sum \lambda_i l_i + \sum \nu_k l_k''$ equal zero (here, if $L$ corresponds to $\prod(\beta_g/\alpha_g)$, $\lambda_i$ counts the number of times a $\beta_i/\alpha_i$ with $\alpha_i < \beta_i$ occurs; and $\nu_k$, the number of times a $\beta_k/\alpha_k$ with $\alpha_k \prec \beta_k$ occurs). Moreover, since the coefficients of $L$ are homogeneous in the $\lambda_i$, $\nu_k$, the compatibility hypothesis can also be stated as follows: for no rational $\lambda_i \geqq 0$, $\nu_k \geqq 0$, $\lambda_i > 0$ for at least one $i$, does $L = 0$. This is just hypothesis (H) of the lemma, so the system has a solution, and the desired valuation exists.

As corollaries of the lemma, we have the following.

**COROLLARY 1.** *Given an arbitrary ordering of $T_1$, an arbitrary finite set of monomials in $x_1, \cdots, x_n$, one has an algorithm for deciding whether the ordering arises from a valuation, and if it does, for finding one. The number $N$ of steps needed is a simple (in fact, primitive recursive) function of $n$ and $b$, where $b$ is a bound on the exponents of the $x_i$.*

The algorithm applies to a system over an arbitrary ordered field. Moreover one gets the following useful corollary.

**COROLLARY 2.** *If a finite system of linear equalities and inequalities with coefficients in an ordered field $F$ has a solution in an ordered extension field $G$ of $F$, then it also has a solution in $F$.*

**PROOF.** The algorithm for deciding relative to $G$ is identical with that relative to $F$.

<!-- page 6 -->

INTUITIVE PROBABILITY ON FINITE SETS

Given a linear system of equalities and inequalities with rational coefficients, let $B$ be a bound on the (absolute values of the) numerators and denominators of the coefficients when written as some quotients of integers. Following the above algorithm, one sees that $2B^4$ is a similar bound for the system obtained upon eliminating $x_1$. Hence one sees how to write down a simple function of $B$ and $n$ which will be a bound for possible numerators and denominators of some solution (if there are solutions). If the equalities and inequalities are homogeneous, then there is an integral solution, and one has a bound for one such. Now write $\epsilon \prec \epsilon$ for some $\epsilon$ in the form $\prod(\beta_i/\alpha_i)^{r_i} = 1$ with $\alpha_i, \beta_i \in T_1$, $\beta_i/\alpha_i \ne \beta_j/\alpha_j$ for $j \ne i$, $\alpha_i < \beta_i$ every $i$, $\alpha_i \prec \beta_i$ some $i$, $r_i \geqq 0$, $r_i > 0$ for at least one $i$ with $\alpha_i < \beta_i$. Writing out the $\alpha_i$, $\beta_i$ as monomials in the $x_i$ and comparing coefficients, one obtains a system of homogeneous linear conditions on the $r_i$. If the system has a solution, then it has one with the $r_i$ integral and bounded as just explained. Hence we have the following corollary.

**COROLLARY 3.** *Let $T_1$ be an arbitrary set of monomials in $n$ variables with exponents bounded by $b$. For every $n$ and $b$ one can find an $N$ such that an arbitrary ordering of $T_1$ arises from a valuation if and only if there is no relation of the form $\prod(\beta_i/\alpha_i)^{r_i} = 1$, $0 \leqq r_i \leqq N$, and some $r_i \ne 0$ for an $i$ such that $\alpha_i < \beta_i$. Here $N$ is a simple (in fact, primitive recursive) function of $n$ and $b$. (For $T_1 = T$ the bound will depend only on $n$.)$^6$*

In a general axiomatic theory of probability it would undoubtedly be of significance to let the values or measures be elements of an arbitrary simply ordered group, because such groups are capable of accommodating events $p$, $q$ with $p$ more probable than $q$ but only by an infinitely small amount. For finite sets, however, one has the following corollary.

**COROLLARY 4.** *If an ordering of $T_1$ arises by assigning values to the $x_i$ from a simply ordered group, then the ordering can also be obtained by assigning real numbers to the $x_i$.*

**PROOF.** If the ordering arises as assumed, then the condition of the theorem obviously obtains.

**DEFINITION.** By an *almost agreeing valuation* one means a valuation, other than the one for which $v(x_i) = 0$ for every $i$, such that $\alpha < \beta$ implies $v(\alpha) \leqq v(\beta)$. In the case $v(x_i) \geqq 0$ every $i$, we speak of an *almost agreeing measure*.

**THEOREM 3.** *Let $T_1$ be an arbitrary finite set of monomials containing $1, x_1, \ldots, x_n$ and ordered arbitrarily subject to the conditions $1 < x_1, \ldots, 1 < x_n$. Then the ordering admits an almost agreeing measure if and only if no monomial $\prod(\beta_i/\alpha_i)$, $\alpha_i, \beta_i \in T_1$, $\alpha_i < \beta_i$, has all its exponents negative.$^7$*

**PROOF.** This time (see Theorem 2, proof) we have a system $\{l_i \geqq 0\}$ for which there is to be a solution; the hypothesis is that for no rational $\lambda_i$, $\lambda_i \geqq 0$, some $\lambda_i > 0$, does the linear form $\sum \lambda_i l_i$ have all its coefficients negative. Taking into account Corollary 2 above, this follows directly from ([2] p. 27,

---

$^6$ For $T_1 = T$, a more special analysis shows that $N = n!$ is a suitable bound. The $\beta_i/\alpha_i$ can be taken to be $\leqq n + 1$ in number.

$^7$ Finiteness conditions hold here as in Theorem 2 and corollaries.

<!-- page 7 -->

C. H. KRAFT, J. W. PRATT, AND A. SEIDENBERG

Criterion VI). A short self-contained proof can be given as follows. Write the given system $\{l_i \geqq 0\}$ relative to some variable $x_1$ which occurs in the form $\{m_u - x_1 \geqq 0, x_1 - m_v' \geqq 0, m_w'' \geqq 0\}$. Then the hypothesis does *not* carry over to the system $\{m_u - m_v' \geqq 0, m_w'' \geqq 0\}$. However, if the elimination is likewise carried out relative to a second variable $x_2$ which occurs, then one sees that the hypothesis carries over to at least one of the resulting systems. Hence the induction holds, and the theorem follows upon verification for $n = 1$ (and $n = 0$).

**4. The counter-examples.** To facilitate the exposition, we state the following proposition and theorem, but postpone the proofs for a moment.

**PROPOSITION 1.** *In a simple ordering of the subsets of $S = \{x_1, \cdots, x_n\}$ which satisfies additivity, the last $2^{n-1}$ subsets are the complements of the first $2^{n-1}$ in reverse order.*

**THEOREM 4.** *Let the $2^n$ subsets of $S = \{x_1, \cdots, x_n\}$ be simply ordered and assume that the last $2^{n-1}$ subsets are the complements of the first $2^{n-1}$ in reverse order. Let $U$ be the first $2^{n-1} + 1$ subsets and assume that $1$, the empty set, is the first element of $U$ and that $\alpha\beta \in U$ implies $\alpha, \beta \in U$. Then if additivity holds for $U$ (i.e., if $\alpha\gamma < \beta\gamma$ implies $\alpha < \beta$ for all $\alpha\gamma$, $\beta\gamma$ in $U$), it also holds for the whole ordering of the $2^n$ subsets $T$.*

The first counter-example stems from trying to see whether Theorem 1 can be extended to three inequalities (in five letters, the fewest for which the extension can fail). One has to put down three inequalities such that all three, but no two, lead (as in Theorem 1) to a new relation; say

$$qs < p, \quad pq < rs, \quad ps < tq.$$

In any agreeing measure one would have to have $pqs < rt$, so we put down

$$rt < pqs$$

and try to fit these four inequalities into a simple ordering of the 32 subsets of $\{p, q, r, s, t\}$ which satisfies additivity. Starting with $1 < q < p < r < s < qr < qs < rs < qrs$, which obviously satisfies additivity, we adjoin the relations $qs < p$, $pq < rs$ to get

$$1 < q < r < s < qr < qs < p < pq < rs$$

(the complements of which, in $\{p, q, r, s\}$, in reverse order are

$$(pq < rs < qrs < pr < ps < pqr < pqs < prs < pqrs).$$

Additivity clearly holds for these first 9 subsets, hence also for all 16 by Theorem 4.

Since $rt$ and $pqs$ are complements, $rt$ will have to be among the first 16 of the sought example; hence also $qt$ and $t$. On the other hand $pqs$ is 14th in the above ordering of the subsets of $\{p, q, r, s\}$. Hence we try to adjoin $t < qt < rt$ to the 13 sets preceding $pqs$. It is convenient to try to take $rt$ as the 16th element, as then $pqs$ will be the 17th and no new elements enter into consideration.

<!-- page 8 -->

INTUITIVE PROBABILITY ON FINITE SETS

Placing $rt$ 16th, from $pqr < rt$ one gets the requirement $pq < t$; and from $tq < pqs$ one gets $t < ps$. Since $ps < tq$, we must place $tq$ either directly before $pqr$ or directly after it. Placing $tq < pqr$, from $qrs < tq < pqr$ one gets the requirements $rs < t < pr$. Now all requirements for additivity have been found. In fact, consider the ordering

$$1 < q < r < s < qr < qs < p < pq$$
$$< rs < t < qrs < rp < ps < tq < qrp < rt < spq$$

(and then by complements)

$$spq < st < rsp < qrt < qst < pt < qrsp < qpt < rst$$
$$< qrst < rpt < spt < qrpt < qspt < rspt < pqrst.$$

In checking additivity one has to see that cancelation with an element involving $t$ preserves order. As far as canceling $t$ is concerned, this checks upon observing that $t, tq, tr$ are in correct order. As for canceling $q$, one has only to consider the elements adjacent to $tq$ which involve $q$, namely $qrs$ and $qrp$; this gives $rs < t < rp$, which checks, and moreover was checked in the course of the construction. Similarly $qrp < rt$ yields $qp < t$, which checks. Of course one can check directly that the above ordering gives the desired counter-example, without recourse to Proposition 1 or Theorem 4, or Theorems 1, 2, and 3 for that matter.

One can also obtain a counter-example as follows. While the given inequalities have no strictly agreeing measure, they do have almost agreeing ones, and from one such one can easily obtain an additive ordering. In fact, let $P, Q, R, S, T$ be the values in an almost agreeing measure. Then from

$$Q + S \leqq P$$
$$P + Q \leqq R + S$$
$$P + S \leqq Q + T$$
$$R + T \leqq P + Q + S$$

and the fact that $(Q + S) + \cdots + (R + T) = P + \cdots + (P + Q + S)$ one finds $Q + S = P$, $P + Q = R + S$, $P + S = Q + T$, $R + T = P + Q + S$; from which $R = 2Q$, $P = Q + S$, $T = 2S$; and these conditions are sufficient. Taking $Q$ and $S$ so that $p, q, r, s, t$ get distinct values (say $Q = 1, S = 3; R = 2, P = 4, T = 6$), one sees that no element other than $rt$ and $pqs$ gets the value $v(rt) = v(pqs)$. Keeping $R$ and $T$ fixed but decreasing $Q, P, S$ slightly (say by $.1$ to $Q = .9, S = 2.9, P = 3.9$), we get a measure in which $qs < p, pq < rs, ps < qt, qps < rt$ and in which 15 elements have value less than $v(pqs)$ and 15 have value greater than $v(rt)$. Now we change $P, Q, R, S, T$ slightly so that the 32 elements get distinct values, the inequalities $qs < p, pq < rs, ps < qt, qps < rt$ are maintained, and also so that $qps$ and $rt$ remain in the middle (say by taking $S = 2.89, T = 5.9, R = 2.2$, keeping $Q = .9$,
