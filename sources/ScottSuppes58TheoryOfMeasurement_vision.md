---
source_pdf: ScottSuppes58TheoryOfMeasurement.pdf
ocr_method: cursor-vision-triple-merge
verification_status: draft
---

# Transcription (LLM vision OCR)


<!-- page 1 -->

**THE JOURNAL**<br>
**OF SYMBOLIC LOGIC**

**FOUNDATIONAL ASPECTS OF THEORIES OF MEASUREMENT**

**BY**<br>
**DANA SCOTT AND PATRICK SUPPES**

**REPRINTED FROM VOLUME 23, NUMBER 2, JUNE 1958**

*Copyright 1959 by the Association for Symbolic Logic, Inc.*

*Printed in The Netherlands*

<!-- page 2 -->

THE JOURNAL OF SYMBOLIC LOGIC<br>
Volume 23, Number 2, June 1958

# FOUNDATIONAL ASPECTS OF THEORIES OF MEASUREMENT$^1$

DANA SCOTT and PATRICK SUPPES

**1. Definition of measurement.** It is a scientific platitude that there can be neither precise control nor prediction of phenomena without measurement. Disciplines are diverse as cosmology and social psychology provide evidence that it is nearly useless to have an exactly formulated quantitative theory if empirically feasible methods of measurement cannot be developed for a substantial portion of the quantitative concepts of the theory. Given a physical concept like that of mass or a psychological concept like that of habit strength, the point of a theory of measurement is to lay bare the structure of a collection of empirical relations which may be used to measure the characteristic of empirical phenomena corresponding to the concept. Why a collection of relations? From an abstract standpoint a set of empirical data consists of a collection of relations between specified objects. For example, data on the relative weights of a set of physical objects are easily represented by an ordering relation on the set; additional data, and *a fortiori* an additional relation, are needed to yield a satisfactory quantitative measurement of the masses of the objects.

The major source of difficulty in providing an adequate theory of measurement is to construct relations which have an exact and reasonable numerical interpretation and yet also have a technically practical empirical interpretation. The classical analyses of the measurement of mass, for instance, have the embarrassing consequence that the basic set of objects measured must be infinite. Here the relations postulated have acceptable numerical interpretations, but are utterly unsuitable empirically. Conversely, as we shall see in the last section of this paper, the structure of relations which have a sound empirical meaning often cannot be succinctly characterized so as to guarantee a desired numerical interpretation.

Nevertheless this major source of difficulty will not here be carefully scrutinized in a variety of empirical contexts. The main point of the present paper is to show how foundational analyses of measurement may be grounded in the general theory of models, and to indicate the kind of problems relevant to measurement which may then be stated (and perhaps answered) in a precise manner.

Received September 24, 1957.

$^1$ We would like to record here our indebtedness to Professor Alfred Tarski whose clear and precise formulation of the mathematical theory of models has greatly influenced our presentation (see [7]). Although our theories of measurement do not constitute special cases of the arithmetical classes of Tarski, the notions are closely related, and we have made use of results and methods from the theory of models. This research was supported under Contract NR 171-034, Group Psychology Branch, Office of Naval Research.

<!-- page 3 -->

Before turning to problems connected with construction of theories of measurement, we want to give a precise set-theoretical meaning to the notions involved. To begin with, we treat sets of empirical data as being (finitary) relational systems, that is to say, finite sequences of the form $\mathfrak{A} = \langle A, R_1, \dots, R_n \rangle$, where $A$ is a non-empty set of elements called the *domain* of the relational system $\mathfrak{A}$, and $R_1, \dots, R_n$ are finitary relations on $A$. The relational system $\mathfrak{A}$ is called *finite* if the set $A$ is finite; otherwise, *infinite*. It should be obvious from this definition that we are mainly considering *qualitative* empirical data. Intuitively we may think of each particular relation $R_i$ (an $m_i$-ary relation, say) as representing a complete set of “yes” or “no” answers to a question asked of every $m_i$-termed sequence of objects in $A$. The point of this paper is not to consider that aspect of measurement connected with the actual collection of data, but rather the analysis of relational systems and their numerical interpretations.

If $s = \langle m_1, \dots, m_n \rangle$ is an $n$-termed sequence of positive integers, then a relational system $\mathfrak{A} = \langle A, R_1, \dots, R_n \rangle$ is of *type* $s$ if for each $i = 1, \dots, n$ the relation $R_i$ is an $m_i$-ary relation. Two relational systems are *similar* if there is a sequence $s$ of positive integers such that they are both of type $s$. Notice that the type of a relational system is uniquely determined only if all the relations are non-empty; the avoiding of this ambiguity is not worthwhile. Suppose that two relational systems $\mathfrak{A} = \langle A, R_1, \dots, R_n \rangle$ and $\mathfrak{B} = \langle B, S_1, \dots, S_n \rangle$ are of type $s = \langle m_1, \dots, m_n \rangle$. Then $\mathfrak{B}$ is a *homomorphic image* of $\mathfrak{A}$ if there is a function $f$ from $A$ onto $B$ such that, for each $i = 1, \dots, n$ and for each sequence $\langle a_1, \dots, a_{m_i} \rangle$ of elements of $A$, $R_i(a_1, \dots, a_{m_i})$ *if and only if* $S_i(f(a_1), \dots, f(a_{m_i}))$. If the function $f$ is one-one, then $\mathfrak{B}$ is an *isomorphic image* of $\mathfrak{A}$, or simply $\mathfrak{A}$ and $\mathfrak{B}$ are *isomorphic*. $\mathfrak{A}$ is a *subsystem* of $\mathfrak{B}$ if $A \subseteq B$ and, for each $i = 1, \dots, n$, the relation $R_i$ is the restriction of the relation $S_i$ to $A$. $\mathfrak{A}$ is *imbeddable* in $\mathfrak{B}$ if some subsystem of $\mathfrak{B}$ is a homomorphic image of $\mathfrak{A}$.$^2$ A *numerical relational system* is simply a relational system whose domain of elements is the set $Re$ of all real numbers. A *numerical assignment* for a relational system $\mathfrak{A}$ with respect to a numerical relational system $\mathfrak{N}$ is a function which imbeds $\mathfrak{A}$ in $\mathfrak{N}$. A numerical assignment is not required to be one-one.

Within the framework of the preceding formal definitions it is now possible to give an exact characterization of a theory of measurement. First of all the general outlines of a theory are determined by fixing a finite sequence $s$ of positive integers and only considering relational systems of type $s$. Next a numerical relational system $\mathfrak{N}$ of type $s$ is selected which

---

$^2$ Although in most mathematical contexts imbeddability is defined in terms of isomorphism rather than homomorphism, for theories of measurement this is too restrictive. However, the notion of homomorphism used here is actually closely connected with isomorphic imbeddability and the facts are explained in detail in Section 2.

<!-- page 4 -->

corresponds to the intended numerical interpretation of the theory, and only relational systems imbeddable in $\mathfrak{N}$ are permitted. Moreover the theory need not concern all relational systems of type $s$ imbeddable in $\mathfrak{N}$ but only a distinguished subclass. Since it is reasonable that no special set of objects be preferred, we require that the distinguished subclass be closed under isomorphism. We thus arrive at the following characterization of theories of measurement as definite entities: a theory of measurement *is* a class $\mathbf{K}$ of relational systems closed under isomorphism for which there exists a finite sequence $s$ of positive integers and a numerical relational system $\mathfrak{N}$ of type $s$ such that all relational systems in $\mathbf{K}$ are of type $s$ and imbeddable in $\mathfrak{N}$.$^3$

Some readers may object that the definition of theories of measurement should be linguistic rather than set-theoretical in character, since a theory is ordinarily thought of as a linguistic entity. To be sure, many theories of measurement have a natural formalization in first-order predicate logic with identity. Notice, however, that first-order axioms by themselves are not adequate, for if they admit one infinite relational system as a model then they have models of every infinite cardinality, and it is difficult to see how any natural connection can be established between numerical models and models of arbitrary cardinality. Even neglecting this criticism first-order axioms are not adequate to express properties involving arbitrary natural numbers, for example, that a relational system is finite or that as an ordering it has Archimedean properties. Any linguistic definition of theories which will permit expression of these more general properties would require extensive machinery and be immediately involved in some of the deepest problems of modern metamathematics. On the other hand, we do not wish to give the impression that we reject any linguistic questions. In fact, we use our set-theoretical definition as a point of departure for asking just such questions.

On the basis of the definition of theories of measurement adopted, two questions naturally arise, to each of which we devote a section. In the first place, is a given class of relational systems a theory of measurement ? And in the second place, given a theory of measurement, in what sense can it be axiomatized?

**2. Existence of measurement.** A simple counterexample shows that not every class of relational systems of a given type closed under isomorphism is a theory of measurement. Let $\mathbf{O}$ be the class of all relational systems of type $\langle 2 \rangle$ that are simple orderings. Let $\langle A, R \rangle$ be a system in $\mathbf{O}$ where $R$

---

$^3$ In some contexts we shall say that the class $\mathbf{K}$ is a *theory of measurement of type $s$ relative to $\mathfrak{N}$*. Notice that a consequence of this definition is that, if $\mathbf{K}$ is a theory of measurement, then so is every subclass of $\mathbf{K}$ closed under isomorphism. Moreover, the class of all systems imbeddable in members of $\mathbf{K}$ is also a theory of measurement

<!-- page 5 -->

<!-- page 116 -->

well-orders $A$ and $A$ has a power not equal to or less than that of the continuum. Such a relational system can be proved to exist even without the help of the axiom of choice, but of course with aid of this axiom the existence is obvious. By way of contradiction suppose that $\mathbf{O}$ is a theory of measurement relative to a numerical relational system $\langle \text{Re}, S \rangle$. From the definition it follows that $\langle A, R \rangle$ is imbeddable in $\langle \text{Re}, S \rangle$ and that there is a numerical assignment $f$ mapping $A$ onto a subset of $\text{Re}$ such that $xRy$ *if and only if* $f(x)\ S\ f(y)$ for all elements $x, y \in A$. Let $a, b$ be elements of $A$ such that $f(a) = f(b)$. From the hypothesis that $R$ is a simple ordering, we can assume without loss of generality that $aRb$. Hence, we have $f(a)\ S\ f(b)$, and then $f(b)\ S\ f(a)$, and finally $bRa$. $R$ is antisymmetric, and so $a = b$. This argument shows that the function $f$ is one-one. Hence $A$ has the same power as a subset of $\text{Re}$, which is impossible. This proof shows that every theory of measurement included in the class $\mathbf{O}$ contains only relational systems of power at most that of the continuum. It is an unsolved problem of set-theory closely connected with the continuum hypothesis whether the class $\mathbf{O}$ restricted to systems of power at most that of the continuum is actually a theory of measurement.$^4$ At least it can be very easily shown that $\mathbf{O}$ so restricted is not a theory of measurement relative to the system $\langle \text{Re}, \le \rangle$, where the relation $\le$ is the usual ordering of the real numbers.$^5$ Indeed, the exact condition that a relational system in $\mathbf{O}$ must satisfy to be imbeddable in $\langle \text{Re}, \le \rangle$ is not really elementary, and the proof of the necessity involves the axiom of choice.$^6$

Let $\mathbf{O}'$ be $\mathbf{O}$ restricted to countable relational systems.$^7$ It was proved by Cantor that $\mathbf{O}'$ is a theory of measurement relative to $\langle \text{Re}, \le \rangle$, to formulate somewhat irreverently his classical result in the terminology of this paper. This restriction to countable relational systems is always sufficient. For it can be shown that the class of *all* countable relational systems of a given type is a theory of measurement; however, the numerical relational system required is so bizarre as to be of no practical value.

A primary aim of measurement is to provide a means of convenient computation. Practical control or prediction of empirical phenomena requires that unified, widely applicable methods of analyzing the important relationships between the phenomena be developed. Imbedding the dis-

---

$^4$ In this connection see Sierpinski [5], Section 7, pp. 141 ff., in particular *Proposition* $C_{75}$, where of course different terminology is used.

$^5$ It is sufficient here to consider a relational system isomorphic to the ordering of the ordinals of the second number class or to the lexicographical ordering of all pairs of real numbers.

$^6$ A simple ordering is imbeddable in $\langle \text{Re}, \le \rangle$ if and only if it contains a countable dense subset. For the exact formulation and a sketch of a proof, see Birkhoff [1], pp. 31–32, Theorem 2.

$^7$ The word 'countable' means at most denumerable and it refers to the cardinality of the domains of the relational systems.

<!-- page 6 -->

FOUNDATIONAL ASPECTS OF THEORIES OF MEASUREMENT

covered relations in various numerical relational systems is the most important such unifying method that has yet been found. But among the morass of all possible numerical relational systems only a very few are of any computational value, indeed only those definable in terms of the ordinary arithmetical notions. From an empirical standpoint most sets of qualitative data can find numerical interpretation by relations defined in terms of addition and ordering alone. By way of example we may cite the measurement of masses, distances, sensation intensities, and subjective probabilities. Frequently the consideration of weighted averages requires also the use of the multiplication of numbers. However, in the examples given in this paper we shall restrict ourselves to the notions of addition and ordering.

No natural scientific situation would seem strictly to require the consideration of sets of infinite data. This state of affairs suggests that theories of measurement containing only finite relational systems would suffice for empirical purposes. The problem is delicate, however, for the measurement of a meteorological quantity such as temperature by an automatic recording device is usually treated as continuous both in its own scale and in time. Yet the important problem of measurement does not really lie in the correct use of such recording devices but rather in their initial calibration, a process proceeding from a finite number of qualitative decisions. Because of the awkwardness of the uniform application of finite relational systems, we shall not generally make this restriction.

Further remarks about establishing the existence of measurement are best motivated by reference to a concrete example. In a recent paper [4], Luce has introduced a generalization of simple orderings which he calls *semiorders*. A *semiorder* is a relational system $\langle A, P \rangle$ of type $\langle 2 \rangle$ which satisfies the following axioms for all $x, y, z, w \in A$:

S1. *Not* $xPx$.

S2. *If* $xPy$ *and* $zPw$, *then either* $xPw$ *or* $zPy$.

S3. *If* $xPy$ *and* $zPx$, *then either* $wPy$ *or* $zPw$.$^8$

Such relations are most likely to occur in situations where objects are to be arranged in order and where it is difficult to say exactly when two objects are indifferent. For example, to say that $xPy$ might be interpreted as meaning that the pitch of the sound $x$ is *definitely higher* than the pitch of $y$, or that the hue of color $x$ is *definitely brighter* than the hue of color $y$, or that the weight of the object $x$ is *noticeably greater* than that of $y$, etc. *Indifference* between two objects $x$ and $y$ (in symbols: $xIy$) is defined as not $xPy$, and not $yPx$. The point of Luce's axioms is that the relation $I$ of

---

$^8$ See [4], Section 2, p. 181. The axioms given here are actually a simplification of those given by Luce.

<!-- page 7 -->

indifference is not always transitive, a fact easily appreciated for each of the intuitive interpretations given above.

In his paper Luce gives a certain numerical interpretation for certain kinds of semiorders, but he does not show that any particular class of semiorders is a theory of measurement in the sense used here, because his interpretations are not relative to a fixed numerical relation. However, in the finite case the situation becomes relatively simple. Let $\gg$ be that relation between real numbers defined by the condition: $x \gg y$ *if and only if* $x > y + 1$. Clearly, if $x$ and $y$ are real numbers such that $x \gg y$, then it is fair to say that $x$ is *definitely greater than* $y$, or better, $x$ is *noticeably greater than* $y$. It is in fact a simple exercise to prove that the relational system $\langle \text{Re}, \gg \rangle$ is a semiorder. Further we shall give the proof of the following result:

*The class of finite semiorders is a theory of measurement relative to the numerical relational system $\langle \text{Re}, \gg \rangle$.*

Before presenting the proof of the above, it would be well to outline a general method in proofs of the existence of measurement which we shall call the *method of cosets*. Let $\mathfrak{A} = \langle A, R_1, \dots, R_n \rangle$ be a relational system of type $\langle m_1, \dots, m_n \rangle$. A uniquely determined equivalence relation $E$ is introduced into $\mathfrak{A}$ by the condition: $xEy$ *if and only if* for each $i = 1, \dots, n$ and each pair $\langle z_1, \dots, z_{m_i} \rangle, \langle w_1, \dots, w_{m_i} \rangle$ of $m_i$-termed sequences of elements of $A$, if $z_j \neq w_j$ implies $\{z_j, w_j\} = \{x, y\}$ for $j = 1, \dots, m_i$, then $R_i(z_1, \dots, z_{m_i})$ *if and only if* $R_i(w_1, \dots, w_{m_i})$.

Even though the above definition is complicated to state in general, the meaning of the relation $xEy$ is simple: elements $x$ and $y$ stand in the relation $E$ just when they are perfect substitutes for each other with respect to all the relations $R_i$.$^9$

The notion of a weak ordering can serve as an example. Let $\mathfrak{A} = \langle A, R \rangle$ where the binary relation $R$ is connected and transitive. Then $xEy$ is equivalent to the condition: For all $z \in A$, $xRz$ *if and only if* $yRz$, and $zRx$ *if and only if* $zRy$. However, this simplifies finally to: $xRy$ and $yRx$.

Returning now to the general case, define, for each $x \in A$, $[x]$ to be the class of all $y$ such that $xEy$. $[x]$ is called the *coset* of $x$. Let $A^*$ be the class of all $[x]$ for $x \in A$. Directly from the definition of $E$ we can deduce that it is permissible to define $m_i$-ary relations $R_i^*$ over $A^*$ such that, for all $x_1, \dots, x_{m_i} \in A$, $R_i^*([x_1], \dots, [x_{m_i}])$ *if and only if* $R_i(x_1, \dots, x_{m_i})$. The relational system $\mathfrak{A}^* = \langle A^*, R_1^*, \dots, R_n^* \rangle$ is called the *reduction of $\mathfrak{A}$ by cosets*.

It is at once obvious that $\mathfrak{A}^*$ is a homomorphic image of $\mathfrak{A}$ and that $\mathfrak{A}^{**}$ is isomorphic with $\mathfrak{A}^*$. What is not quite obvious is the following:

*If $\mathfrak{B}$ is a homomorphic image of $\mathfrak{A}$, then $\mathfrak{A}^*$ is a homomorphic image of $\mathfrak{B}$.*

---

$^9$ The authors are indebted to the referee for pointing out the work by Hailperin in [3] which suggested this general definition.

<!-- page 8 -->

By way of proof, let $f$ be a homomorphism of $\mathfrak{A}$ onto $\mathfrak{B}$. We wish to show that if $f(x) = f(y)$, then $[x] = [y]$. Instead of the general case, assume for simplicity that $\mathfrak{A}$ and $\mathfrak{B}$ are of type $\langle 2 \rangle$ and $\mathfrak{A} = \langle A, R \rangle$, $\mathfrak{B} = \langle B, S \rangle$. We must show that if $f(x) = f(y)$, then $xEy$, or in other words, for all $z \in A$, $xRz$ *if and only if* $yRz$, and $zRx$ *if and only if* $zRy$. Assume $xRz$. It follows that $f(x)\ S\ f(z)$, and hence $f(y)\ S\ f(z)$, which implies that $yRz$. The argument is clearly symmetric. We have therefore shown that there is a function $g$ from $B$ onto $A^*$ such that $g(f(x)) = [x]$ for $x \in A$. It is trivial to verify that $g$ is a homomorphism of $\mathfrak{B}$ onto $\mathfrak{A}^*$.

Notice the following relation between the concepts of homomorphic image and subsystem: if $\mathfrak{B}$ is a homomorphic image of $\mathfrak{A}$, then $\mathfrak{B}$ is isomorphic to a subsystem of $\mathfrak{A}$. For let $f$ be a homomorphism of $\mathfrak{A}$ onto $\mathfrak{B}$. Let $g$ be any function from $B$ into $A$ such that $f(g(y)) = y$ for all $y \in B$. The restriction of $\mathfrak{A}$ to the range of $g$ yields the subsystem of $\mathfrak{A}$ isomorphic with $\mathfrak{B}$.

Using the above remarks we can establish at once the equivalence: $\mathfrak{A}$ is imbeddable in $\mathfrak{B}$ *if and only if* $\mathfrak{A}^*$ is imbeddable in $\mathfrak{B}$.

Further, it follows that any function imbedding $\mathfrak{A}^*$ in $\mathfrak{B}$ is always an isomorphism of $\mathfrak{A}^*$ onto a subsystem of $\mathfrak{B}$, and of all homomorphic images of $\mathfrak{A}$ this property is characteristic of $\mathfrak{A}^*$.

Let $\mathbf{K}$ now be any class of relational systems closed under isomorphism. Let $\mathbf{K}^*$ be the class of all systems isomorphic to some $\mathfrak{A}^*$ for $\mathfrak{A} \in \mathbf{K}$. In effect we have shown above:

(i) $\mathbf{K}$ is a theory of measurement relative to a numerical relational system $\mathfrak{N}$ *if and only if* $\mathbf{K}^*$ is also.

(ii) If $\mathbf{K}$ in addition is closed under the formation of subsystems, then $\mathbf{K}^*$ is the class of all systems in $\mathbf{K}$ possessing only one-one numerical assignments.

To use our example again, if $\mathbf{K}$ is the class of weak orders, then $\mathbf{K}^*$ is the class of *simple orders*. Notice that the proof in the first paragraph of this section is a special case of (ii).

It should be remarked that for a relational system $\mathfrak{A}$, $\mathfrak{A}$ and $\mathfrak{A}^*$ always satisfy exactly the same formulas of first-order logic not involving the notion of identity. Hence, if $\mathbf{K}$ is the class of all relational systems satisfying first-order axioms without identity, then $\mathbf{K}^*$ is the class of all systems satisfying the axioms for $\mathbf{K}$ and in addition satisfying the axiom:

(*) If $xEy$, then $x = y$.

The application of this remark to weak orderings and simple orderings is left to the reader.

Consider again the case of semiorders. Let $\mathbf{S}$ be the class of all finite semiorders. For any $\langle A, P \rangle \in \mathbf{S}$, consider the relation $I$ of indifference defined above. In terms of $I$ one can establish a simplified characterization of $E$: $xEy$ if and only if for all $z \in A$, $xIz$ if and only if $yIz$.

<!-- page 9 -->

Introduce $(*)$ as a new axiom S4. The class of all $\mathfrak{A} \in \mathbf{S}$ satisfying S4 is just the class $\mathbf{S}^*$. Notice that unlike the pleasant situation with weak orderings and simple orderings, the class $\mathbf{S}^*$ is not closed under the formation of subsystems even though $\mathbf{S}$ is.

For any semiorder $\langle A, P \rangle$ introduce a further relation $R$ as follows: $xRy$ if and only if for all $z$, if $zPx$ then $zPy$, and if $yPz$ then $xPz$.

We leave to the reader the elementary verification of the fact that $R$ is a weak ordering of $A$, and that $xEy$ if and only if $xRy$ and $yRx$. Thus, if $\langle A, P \rangle \in \mathbf{S}^*$, then $R$ is a simple ordering of $A$. The connection between $P$ and $R$ is clearer if one notices that $xPy$ implies $xRy$, and that, if $xRx_1$, $x_1Py_1$, and $y_1Ry$, then $xPy$.

Now let $\mathfrak{A} = \langle A, P \rangle$ be a fixed member of $\mathbf{S}^*$. We wish to show that $\mathfrak{A}$ has an assignment in $\langle \text{Re}, \gg \rangle$. Under the relation $R$, $A$ is simply ordered. Let $A = \{x_0, \dots, x_n\}$ where $x_i R x_{i-1}$ and $x_i \neq x_{i-1}$. Define by a course of values recursion a sequence $a_0, \dots, a_n$ of rational numbers determined uniquely by the following two conditions:

(1) If $x_i I x_0$, then $a_i = \frac{i}{i+1}$.

(2) If $x_i I x_j$ and $x_i P x_{j-1}$ where $j > 0$, then $a_i = \frac{i}{i+1} a_j + \frac{1}{i+1} a_{j-1} + 1$.

Notice that in (2) the hypothesis implies that $j \le i$, while in the case $j = i$ the formula for $a_i$ simplifies to $a_i = a_{i-1} + i + 1$. Notice further that every element $x_i$ comes either under (1) or (2); for letting $x_j$ be the first element such that $x_j I x_i$, there are two cases: $j = 0$, $j > 0$. Clearly we always have $a_i \ge 0$.

We show first that $a_i > a_{i-1}$ by induction on $i$. For case (1), this is obvious. Passing to (2), assume that $x_i I x_j$ and $x_i P x_{j-1}$. If $x_{i-1} I x_0$, then $a_{i-1} < 1$ while $a_i > 1$. Hence we can assume not $x_{i-1} I x_0$, or in other words $x_{i-1} P x_0$. Let $x_k$ be the first element such that $x_{i-1} I x_k$ and $x_{i-1} P x_{k-1}$. By definition $a_{i-1} = \frac{i-1}{i} a_k + \frac{1}{i} a_{k-1} + 1$. If $j = i$, there is no problem. Assume then that $j < i$. Now $x_{i-1} R x_j$, $x_i R x_{i-1}$, and $x_j I x_i$, hence $x_j I x_{i-1}$, and so by our choice of $k$ we have $k \le j$. By the induction hypothesis on $i$, it follows that $a_j > a_{j-1}$ and $a_k > a_{k-1}$. If $k = j$, the required inequality is obvious. If $k \le j-1$, then $a_i > a_{j-1} + 1$. Similarly $a_{i-1} < a_k + 1$, but again, by the induction hypothesis, $a_k \le a_{j-1}$, and hence $a_i > a_{i-1}$.

The next step is to prove that, if $x_i P x_k$, then $a_i > a_k + 1$. Let $x_j$ be the first element such that $x_i I x_j$ and $x_i P x_{j-1}$. We have $j - 1 \ge k$, and, in view of the preceding argument, $a_{j-1} \ge a_k$. But $a_{j-1} + 1 < a_i$, whence $a_i > a_k + 1$.

Conversely we must show that, if $a_i > a_k + 1$, then $x_i P x_k$. The hypothesis of course implies $i > k$. Assume by way of contradiction that not $x_i P x_k$. It follows that $x_i I x_k$. Let $x_j$ be the first element such that $x_i I x_j$; then

<!-- page 10 -->

$k \ge j$ and $a_k \ge a_j$. If $j = 0$, then $x_i I x_0$ and $x_k I x_0$, because $x_i R x_k$. But then $0 \le a_i < 1$ and $0 \le a_k < 1$, which contradicts the inequality $a_i > a_k + 1$. We can conclude that $j > 0$. Now $a_i < a_j + 1$, but $a_k \ge a_j$, and thus $a_i < a_k + 1$, which again is a contradiction. All cases have been covered, and the argument is complete.

Finally define a function $f$ on $A$ such that $f(x_i) = a_i$. We have actually shown that $f$ imbeds $\mathfrak{A}$ in $\langle \text{Re}, \gg \rangle$. Thus it has been proved that $\mathbf{S}^*$ is a theory of measurement relative to $\langle \text{Re}, \gg \rangle$, and, by the general remarks on the method of cosets, we conclude that $\mathbf{S}$ is also a theory of measurement relative to $\langle \text{Re}, \gg \rangle$.

Notice that the above proof would also work in the infinite case as long as the ordering $R$ is a well-ordering of type $\omega$.

Let us now summarize the steps in establishing the existence of measurement using as examples simple orderings and semiorders. First, after one is given a class, $\mathbf{K}$ say, of relational systems, the numerical relational system should be decided upon. The numerical relational system should be suggested naturally by the structure of the systems in $\mathbf{K}$, and as was remarked, it is most practical to consider numerical systems where all the relations can be simply defined in terms of addition and ordering of real numbers. Second, if the proof that $\mathbf{K}$ is a theory of measurement is not at once obvious, the cardinality of systems in $\mathbf{K}$ should be taken into consideration. The restriction to countable systems would always seem empirically justified, and adequate results are possible with a restriction to finite systems. Third, the proof of the existence of measurement can often be simplified by the reduction of each relational system in $\mathbf{K}$ by the method of cosets. Then, instead of trying to find numerical assignments for each member of $\mathbf{K}$, one concentrates only on the reduced systems. This plan was helpful in the case of semiorders. Instead of cosets, it is sometimes feasible to consider imbedding by subsystems. That is to say, one considers some convenient subclass $\mathbf{K}' \subseteq \mathbf{K}$ such that every element of $\mathbf{K}$ is a subsystem of some system in $\mathbf{K}'$. If $\mathbf{K}'$ is a theory of measurement, then so is $\mathbf{K}$. In the case of semiorders we could have used either plan: cosets or subsystems.

After the existence of measurement has been established, there is one question which is often of interest: For a given relational system, what is the class of all its numerical assignments? We present an example.

Consider relational systems $\mathfrak{A} = \langle A, D \rangle$ of type $\langle 4 \rangle$. For such systems we introduce the following definitions: $xRy$ *if and only if* $xyDyy$. $xyM^1zw$ *if and only if* $xyDzw$, $zwDxy$, $yRz$ and $zRy$. $xyM^{n+1}zw$ *if and only if* there exist $u, v \in A$ such that $xyM^n uv$ and $uvM^1 zw$.

Let $\mathbf{H}$ be the class of all such relational systems which satisfy the following axioms for every $x, y, z, u, v, w \in A$:

A1. *If* $xyDzw$ *and* $zwDuv$, *then* $xyDuv$.

A2. $xyDzw$ *or* $zwDxy$.

<!-- page 11 -->

**A3.** *If* $xyDzw$, *then* $xzDyw$.

**A4.** *If* $xyDzw$, *then* $wzDyx$.

**A5.** *If* $xRy$ *and* $yzDuv$, *then* $xzDuv$.

**A6.** *There is a* $z \in A$ *such that* $xzDzy$ *and* $zyDxy$.

**A7.** *If not* $xyDzw$ *and not* $xRy$, *then there is a* $u \in A$ *such that* $zwDxu$, *not* $xRu$, *and not* $uRy$.

**A8.** *If* $xyDzw$ *and not* $xRy$, *then there are* $u, v \in A$ *and an* $n$ *such that* $zuM^n vw$ *and* $zuDxy$.

These axioms imply that for a system $\mathfrak{A}$ in $\mathbf{H}$, the relation $R$ is a weak ordering of $A$, and the intuitive interpretation of $xyDzw$ in case $yRx$ and $wRz$ is that the interval between $x$ and $y$ is not greater than the interval between $z$ and $w$. Making heavy use of the last three existence axioms, it can be shown that $\mathbf{H}$ is a theory of measurement relative to the numerical relational system $\langle \text{Re}, \Delta \rangle$ where $\Delta$ is the quaternary relation defined by the condition $xy \Delta zw$ if and only if $x - y \le z - w$ for all $x, y, z, w \in \text{Re}$. It must be stressed that the Archimedean property of the ordering embodied in A8 cannot be formulated in first-order logic, because it implies that all systems in $\mathbf{H}^*$ have cardinality not more than the power of the continuum. In addition, it can be shown that, if $\mathfrak{A}$ is in $\mathbf{H}$, and $f$ and $g$ are two numerical assignments of $\mathfrak{A}$ relative to $\langle \text{Re}, \Delta \rangle$, then $f$ and $g$ are related by a positive linear transformation;$^{10}$ that is, there exist $\alpha, \beta \in \text{Re}$ with $\alpha > 0$ such that, for all $x \in \text{Re}$, $f(x) = \alpha g(x) + \beta$. This gives in a certain sense the answer to the question above: If we know one numerical assignment for $\mathfrak{A}$, we know them all. Except for very special systems in $\mathbf{H}$, nothing more specific can really be expected.

Notice that all relational systems in $\mathbf{H}$ are necessarily infinite. In the next section we shall consider in detail the theory of measurement $\mathbf{F}$ consisting of all finite relational systems imbeddable in $\langle \text{Re}, \Delta \rangle$. Here the situation is quite hopeless. There simply is no apparent general statement that can be made about the relation between assignments. In as much as any function $\varphi$ which imbeds $\langle \text{Re}, \Delta \rangle$ in itself is necessarily a linear transformation and conversely, it follows that, if $\mathfrak{A}$ is a system in $\mathbf{F}$ and $f$ is an assignment for $\mathfrak{A}$, then $f$ composed with a linear transformation is also an assignment. The main difficulty with $\mathbf{F}$ is that two assignments for the same system in $\mathbf{F}$ need not be related by a linear transformation.

**3. Axiomatizability.** Given a theory of measurement, it is natural to ask various questions about its axiomatizability, for the axiomatic analysis of any mathematical theory usually throws considerable light on the structure of the theory. In particular, given an extrinsic characteri-

---

$^{10}$ The proofs of both these facts about $\mathbf{H}$ are very similar to the corresponding proofs in Suppes and Winet [6].

<!-- page 12 -->

**FOUNDATIONAL ASPECTS OF THEORIES OF MEASUREMENT**

zation of a theory of measurement via a particular numerical relational system, it is quite desirable to have an intrinsic axiomatic characterization of the theory to be able better to recognize when a relational system actually belongs to the theory. In view of the paucity of metamathematical results concerning the axiomatics of higher-order theories, we shall restrict ourselves to the problem of axiomatizing theories of measurement in first-order logic.

It is a well-known result that, if a set of first-order axioms has one infinite model, then it has models of unbounded cardinalities. Since for the most part we are interested in one-one assignments with values in the set of real numbers, unbounded cardinalities are hardly an asset. That is to say, the class of all relational systems that are models of a given set of first-order axioms is usually not a theory of measurement. To remove such difficulties without having to understand them, we simply restrict the cardinalities under consideration. Even a restriction to finite cardinalities is not too strong and leads to some rather difficult questions. Thus for the remainder of this section we shall consider only *finitary theories of measurement*, i.e., theories containing only finite relational systems. Such a theory is called *axiomatizable*, if there exists a set of sentences of first-order logic (the axioms of the theory) such that a finite relational system is in the theory if and only if the system satisfies all the sentences in the set. A theory is *finitely axiomatizable* if it has a finite set of axioms. A theory is *universally axiomatizable* if it has a set of axioms each of which is a universal sentence (i.e., a sentence in prenex normal form with only universal quantifiers).

It should be observed, first, that *any* finitary theory of measurement is axiomatizable. This is no deeper than saying that in first-order logic we can write down a sentence completely describing the isomorphism type of each finite relational system not in the given theory, and clearly the negations of these sentences can serve as the required set of axioms. It is of course quite obvious that we cannot in each instance give an effective method for writing down the axioms, since there are clearly a continuum of distinct finitary theories of measurement. Notice also that if the theory is closed under subsystems then the axioms may be taken as universal sentences, and conversely. In case one considers theories consisting of all finite relational systems imbeddable in a given numerical relational system, then the problem of a recursive or effective axiomatization is simply the problem of whether the class of universal sentences true in the given numerical relational system is recursively enumerable or not. It is not difficult to establish that this last problem is equivalent to the problem of giving a recursive enumeration of all the relation types of finite relational systems *not* imbeddable in the given numerical relational system. For numerical relational systems whose relations are definable in first-order logic in terms

<!-- page 13 -->

of $+$ and $\le$, these problems do not arise since the first-order theory of $+$ and $\le$ is decidable, and it is to these relational systems that we shall primarily restrict our further attention.

In the second place, in all domains of mathematics a finite axiomatization of a theory is usually felt to be the most satisfactory result. No doubt the psychological basis for such a feeling rests on the fact that only a finite characterization can in one step explicitly lay bare the full structure of a theory. Of course an extremely complicated axiomatization may be of little practical value, and as regards theories of measurement there is a further complication. Namely, if an axiomatization in first-order logic, no matter how elegant it may be, involves a combination of several universal and existential quantifiers, then the confirmation of this axiom may be highly contingent on the relatively arbitrary selection of the particular domain of objects. From the empirical standpoint, aside from the possible requirement of a fixed minimal number of objects, results ought to be independent of an exact specification of the extent of the domain.

We are thus brought to our third observation: A finite universal axiomatization of a theory of measurement always yields a characterization independent of accidental object selection. To be precise, consider a fixed universal sentence. This formula will obviously contain just a finite number of variables. Hence, to verify the truth of the sentence in a particular relational system, we need consider only subsets of the domain of a uniformly bounded cardinality. Furthermore, verification for each subset is completely independent of any relationships with the complementary set.

Simple orderings and semiorders are examples of this last point. To determine whether a finite relational system of type $\langle 2 \rangle$ is a simple ordering, one has only to consider triples of objects; for semiorders, quadruples. In constructing an experiment, say, on the simple ranking of objects with respect to a certain property, the design is ordinarily such that connectivity and antisymmetry of the relation are satisfied, because for each pair of objects the subjects is required to decide the ranking one way or the other, but not in both directions. Analysis of the data then reduces to searching for 'intransitive triads'.

Vaught [8] has provided a useful criterion for certain classes of relational systems to be axiomatizable by means of a universal sentence. A straightforward analysis of his proof yields immediately the following criterion for finitary theories of measurement.

*A finitary theory of measurement $\mathbf{K}$ is axiomatizable by a universal sentence, if and only if $\mathbf{K}$ is closed under subsystems and there is an integer $n$ such that, if any finite relational system $\mathfrak{A}$ has the property that every subsystem of $\mathfrak{A}$ with no more than $n$ elements is in $\mathbf{K}$, then $\mathfrak{A}$ is in $\mathbf{K}$.*

Though classes of finite simple orderings and finite semiorders are two examples of finitary theories of measurement axiomatizable by a universal

<!-- page 14 -->

**FOUNDATIONAL ASPECTS OF THEORIES OF MEASUREMENT**

sentence, there are interesting examples of finitary theories of measurement closed under subsystems which are *not* axiomatizable by a universal sentence. We now turn to the proof for one such case.

Let $\mathbf{F}$ be the class of all finitary relational systems of type $\langle 4 \rangle$ imbeddable in the numerical relational system $\langle \text{Re}, \Delta \rangle$. A wide variety of sets of empirical data are in $\mathbf{F}$. In fact, all sets of psychological data based upon judgments of differences of sensation intensities or of differences in utility qualify as candidates for membership in $\mathbf{F}$. For example, in an experiment concerned with the subjective measurement of loudness of $n$ sounds, the appropriate empirical data would be obtained by asking subjects to compare each of the $n$ sounds with every other and then to compare the difference of loudness in every pair of sounds with every other. More elaborate interpretations are required to obtain appropriate data on utility differences for individuals or social groups (cf. Davidson, Suppes and Siegel [2], Suppes and Winet [6]). It may be of some interest to mention one probabilistic interpretation closely related to the classical scaling method of paired comparisons. Subjects are asked to choose only between objects, but they are asked to make this choice a number of times. There are many situations in which they vacillate in their choice, and the probability $p_{xy}$ that $x$ will be chosen over $y$ may be estimated from the relative frequency with which $x$ is so chosen. From inequalities of the form $p_{xy} \le p_{zw}$ we may obtain a set of empirical data, that is, a finite relational system of type $\langle 4 \rangle$, which is a candidate for membership in $\mathbf{F}$. The intended interpretation is that, if $p_{xy} \ge \frac{1}{2}$ and $p_{zw} \ge \frac{1}{2}$, then $p_{xy} \le p_{zw}$ if and only if the difference in sensation intensity or difference in utility between $x$ and $y$ is equal to or less than that between $z$ and $w$, the idea being, of course, that if $x$ and $y$ are closer together than $z$ and $w$ in the subjective scale, then the relative frequency of choice of $x$ over $y$ is closer to one-half than that of $z$ over $w$.

Before formally proving that the theory of measurement $\mathbf{F}$ is not axiomatizable by a universal sentence, we intuitively indicate for a relational system of ten elements the kind of difficulty which arises in any attempt to axiomatize $\mathbf{F}$. Let the ten elements be $a_1, \dots, a_{10}$ ordered as shown on the following diagram with atomic intervals given the designations indicated.

```
    α₁      α₂      α₃      α₄            γ             β₁      β₂      β₃      β₄
    |       |       |       |             |             |       |       |       |
────┼───────┼───────┼───────┼─────────────┼─────────────┼───────┼───────┼───────┼────
    a₁      a₂      a₃      a₄      a₅                  a₆      a₇      a₈      a₉     a₁₀
```

Let $\alpha$ be the interval $(a_1, a_5)$, let $\beta$ be the interval $(a_6, a_{10})$, and let $\gamma$ be larger than $\alpha$ or $\beta$. We suppose further that $\alpha_1, \alpha_2, \alpha_3, \alpha_4$ is equal in size to $\beta_2, \beta_4, \beta_1, \beta_3$, respectively, but $\alpha$ is less than $\beta$.$^{11}$

---

$^{11}$ Essentially this example was first given in another context by Herman Rubin to show that a particular set of axioms is defective.

<!-- page 15 -->

The size relationships among the remaining intervals may be so chosen that any subsystem of nine elements is imbeddable in $\langle \text{Re}, \Delta \rangle$, whereas the full system of ten elements is clearly not.

Generalizing this example and using the criterion derived from Vaught's theorem we now prove:

**THEOREM.** *The theory of measurement* $\mathbf{F}$ *is not axiomatizable by a universal sentence.*

**PROOF.** In order to apply the criterion of axiomatizability by a universal sentence, we need to show that for every $n$ there is a finite relational system $\mathfrak{A}$ of type $\langle 4 \rangle$ such that every subsystem of $\mathfrak{A}$ with $n$ elements in its domain is in $\mathbf{F}$ but $\mathfrak{A}$ is not.

To this end, for every even integer $n = 2m \ge 10$ we construct a finite relational system $\mathfrak{A}$ of type $\langle 4 \rangle$ such that every subsystem of $2m - 1$ elements is in $\mathbf{F}$. (*A fortiori* every subsystem of $2m - k$ elements for $k < 2m$ is in $\mathbf{F}$.) To make the construction both definite and compact, we take numbers as elements of the domain and disrupt exactly one numerical relationship. Let now $m$ be an even integer equal to or greater than 10. The selection of numbers $a_1, \dots, a_{2m}$ may be most easily described by specifying the numerical size of the atomic intervals. We define $\alpha_i = a_{i+1} - a_i$ for $i = 1, \dots, m - 1$ and $\beta_i = a_{m+i+1} - a_{m+i}$ for $i = 1, \dots, m - 1$. We then set $a_1 = 1$, $\alpha_i = 2^i$ for $i = 1, \dots, m - 1$, and $a_{m+1} = 2^{2m}$. In fixing the size of $\beta_i$, we have two cases to consider depending on the parity of $m$.

**CASE 1.** $m$ is even. Then $m - 1$ is odd, and we set $\beta_i = \alpha_{i/2}$ for $i = 2, 4, \dots, m - 2$ and $\beta_i = \alpha_{(m+i-1)/2}$ for $i = 1, 3, \dots, m - 1$.

**CASE 2.** $m$ is odd. Then $m - 1$ is even, and we set $\beta_i = \alpha_{i/2}$ for $i = 2, 4, \dots, m - 1$ and $\beta_i = \alpha_{(m+i)/2}$ for $i = 1, 3, \dots, m - 2$. Thus if $n = 2m = 12$, we have $\alpha_1 = \beta_2$, $\alpha_2 = \beta_4$, $\alpha_3 = \beta_1$, $\alpha_4 = \beta_3$, $\alpha_5 = \beta_5$. With the set $A = \{a_1, \dots, a_{2m}\}$ defined, we now define the relation $D$ as the expected numerical relation except for permutations of $a_1, a_m, a_{m+1}$ and $a_{2m}$. If $x, y, z, w \in A$ and $\langle x, y, z, w \rangle$ is not some permutation of $\langle a_1, a_m, a_{m+1}, a_{2m} \rangle$, then $\langle x, y, z, w \rangle \in D$ if and only if

$$(1) \qquad x - y \le z - w.$$

Moreover, let $a = a_1$, $b = a_m$, $c = a_{m+1}$, $d = a_{2m}$. Then we put the following nine permutations of $\langle a, b, c, d \rangle$ in $D$:

$$\begin{array}{lll}
\langle b, a, d, c \rangle & \langle a, b, d, c \rangle & \langle c, b, d, a \rangle \\
\langle b, d, a, c \rangle & \langle a, c, d, b \rangle & \langle c, d, a, b \rangle \\
\langle b, d, c, a \rangle & \langle a, d, c, b \rangle & \langle c, d, b, a \rangle
\end{array}$$

(These nine permutations correspond exactly to the strict inequalities following from $b - a < d - c$. All nine are needed to make the subsystems of $\langle A, D \rangle$ have the appropriate properties.)

<!-- page 16 -->

From the choice of the numbers in $A$ and the definition of $D$ it is obvious that $\langle A, D \rangle$ is not imbeddable in $\langle \text{Re}, \Delta \rangle$, that is, that $\langle A, D \rangle$ is not in $\mathbf{F}$; for the atomic intervals between $a_1$ and $a_m$ must add up to a length equal to the sum of the atomic intervals between $a_{m+1}$ and $a_{2m}$, but by hypothesis the interval $(a_1, a_m)$ is less than the interval $(a_{m+1}, a_{2m})$. It remains to show that every subsystem of $2m - 1$ elements is in $\mathbf{F}$. Two cases naturally arise.

CASE 1. The element omitted in the subsystem is $a_1$, $a_m$, $a_{m+1}$ or $a_{2m}$. Then the nine permutations of (2) are not in $D$ restricted to the subsystem, and the subsystem is not merely imbeddable in $\langle \text{Re}, \Delta \rangle$, but by virtue of (1) is a subsystem of it.

CASE 2. The element omitted is neither $a_1$, $a_m$, $a_{m+1}$ nor $a_{2m}$. Let $a_i$ be the element not in the subsystem. There are two cases to consider.

CASE 2a. $a_i < a_m$. For this situation we may use for our numerical assignment the function $f$ defined by $f(a_{i-j}) = a_{i-j} + 1$ for $j = 1, \dots, i-1$, $f(a_{i+j}) = a_{i+j}$ for $j = 1, \dots, n-i$. It is straightforward but tedious to verify that $f$ is a numerical assignment, that is, that it preserves the relation $D$ as defined by (1) and (2). Only two observations are crucial to this verification. First, regarding atomic intervals (in the full system), if $a_{i-j+1} - a_{i-j} = a_{k+1} - a_k$ for $k > i$, then $f(a_{i-j+1}) - f(a_{i-j}) = (a_{i-j+1} - 1) - (a_{i-j} - 1) = a_{k+1} - a_k = f(a_{k+1}) - f(a_k)$. Second, the numbers in $A$ were so chosen that, if $x, y, z, w \in A$, and $(z, w)$ is not an atomic interval, and $(x, y) \neq (z, w)$ and $x - y \leq z - w$, then $x - y + 2 \leq z - w$. Then it is clear from the definition of $f$ that $f(x) - f(y) \leq f(z) - f(w)$. (Note that the above implies the weaker result that no two distinct nonatomic intervals have the same size.)

CASE 2b. $a_i > a_{m+1}$. Here we may use a numerical assignment $f$ defined, as would be expected from the previous case, by $f(a_{i-j}) = a_{i-j}$ for $j = 1, \dots, i-1$, $f(a_{i+j}) = a_{i+j} + 1$ for $j = 1, \dots, n-i$. This completes the proof of the theorem.

It would be pleasant to report that we could prove a stronger result about the theory of measurement $\mathbf{F}$, namely, that it is not finitely axiomatizable. Unfortunately, there seems to be a paucity of tools available for studying such questions for classes of relational systems. However, we would like to state a conjecture which if true would provide one useful tool for studying the finite axiomatizability of finitary theories of measurement like $\mathbf{F}$ which are closed under submodels. We say that two sentences are *finitely equivalent* if and only if they are satisfied by the same finite relational systems, and we conjecture: *If $S$ is a sentence such that if it is satisfied by a finite model it is satisfied by every submodel of the finite model, then there is a universal sentence finitely equivalent to $S$.* If this conjecture is true, it follows that any finitary theory of measurement closed under submodels is finitely axiomatizable if and only if it is axiomatizable by a universal sentence.

The proof (or disproof) of this conjecture appears difficult. It easily follows

<!-- page 17 -->

<!-- page 128 -->

The proof (or disproof) of this conjecture appears difficult. It easily follows from Tarski's results [7] on universal (arithmetical) classes in the wider sense that, if the finitistic restrictions are removed throughout in the conjecture, the thus modified conjecture is true; for the class of relational systems satisfying $S$, being closed under submodels, is a universal class in the wider sense and is axiomatizable by a denumerable set of universal sentences. Since $S$ is logically equivalent to this set of universal sentences, it is a logical consequence of some finite subset of them; but because it implies the full set, it also implies the finite subset and is thus equivalent to it.

Our conjecture is one concerning the general theory of models and its pertinence is not restricted to theories of measurement. In conclusion we should like to mention an unsolved problem typical of those which arise in the special area of measurement. *Let $R$ be any binary numerical relation definable in an elementary manner in terms of plus and less than. Is the finitary theory of measurement of all systems imbeddable in $R$ finitely axiomatizable?* (If our conjecture about finite models is true, then the theory of measurement $\mathbf{F}$ is not finitely axiomatizable and shows that the answer to this problem is negative for quaternary relations definable in terms of plus and less than.)

**REFERENCES**

[1] G. BIRKHOFF, *Lattice theory*, American Mathematical Society colloquium series, vol. 25, revised ed. (1948), xiv + 283 pp.

[2] D. DAVIDSON, P. SUPPES and S. SIEGEL, *Decision making: An experimental approach*, Stanford, California (Stanford University Press), 1957, 121 pp.

[3] T. HAILPERIN, *Remarks on identity and description in first-order axiom systems*, this JOURNAL, vol. 19 (1954), pp. 14–20.

[4] R. D. LUCE, *Semiorders and a theory of utility discrimination*, ***Econometrica***, vol. 24 (1956), pp. 178–191.

[5] W. SIERPINSKI, *Hypothèse du continu*, Warsaw and Lwów 1934, v + 192 pp.

[6] P. SUPPES and M. WINET, *An axiomatization of utility based on the notion of utility differences*, ***Management science***, vol. 1 (1955), pp. 259–270.

[7] A. TARSKI, *Contributions to the theory of models, I, II, III*, ***Indagationes mathematicae***, vol. 16 (1954), pp. 572–581, 582–588, and vol. 17 (1955), pp. 56–64.

[8] R. VAUGHT, *Remarks on universal classes of relational systems*, ***Indagationes mathematicae***, vol. 16 (1954), pp. 589–591.

PRINCETON UNIVERSITY AND STANFORD UNIVERSITY

<!-- page 18 -->

# ASSOCIATION FOR SYMBOLIC LOGIC

*President:* S. C. Kleene, University of Wisconsin, Madison 6, Wisconsin.

*Vice-President:* F. B. Fitch, Yale University, New Haven, Connecticut

*Secretary-Treasurer:* Joshua Barlaz, Rutgers University, New Brunswick, New Jersey.

THE ASSOCIATION FOR SYMBOLIC LOGIC is an international organization for the promotion of research and of critical studies in the field of formal logic. It is intended to provide a meeting ground for mathematicians and philosophers interested in this field, to encourage cooperation and mutual criticism among various groups, and to promote a wider general knowledge and appreciation of current research and recent advances in the field. Membership dues are five dollars per annum payable in the currency of the United States. For European members, dues may be paid in the currency of Belgium or the Netherlands.

THE JOURNAL OF SYMBOLIC LOGIC is the official organ of the Association. It provides a medium for the publication, in English, French, or German, of research and of critical or expository articles in symbolic logic and immediately related fields. Volume $1$ contains a bibliography of symbolic logic for the period $1666$–$1935$; a list of additions and corrections to this bibliography, together with indexes to the whole, appears in Volume $3$, Number $4$. A complete current bibliography of the literature of symbolic logic from January $1$, $1936$, including both books and articles, is provided by prompt publication of critical reviews (indexed by authors biennially, and by subjects at longer intervals).

Subscription to the Journal is $\$ 5.00$ annually. Single numbers of the current volume are $\$ 1.50$ each. Completed volumes (four numbers) will be sold at $\$ 6.00$.

Single copies of the bibliographical number, Volume $1$, number $4$, will be sold at $\$2.00$. Other single numbers are $\$1.75$. Offprints of the list of additions, corrections, and indexes to the bibliography are on sale at $\$1.25$. These contain a title-page and may be bound with Volume $1$, Number $4$ to form a complete bibliography of symbolic logic to the end of the year $1935$.

Orders and requests for information should be addressed to the Secretary-*Treasurer of the Association for Symbolic Logic, Rutgers University, New Brunswick, New Jersey.*
