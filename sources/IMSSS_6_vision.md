---
source_pdf: IMSSS_6.pdf
ocr_method: cursor-vision-triple-merge
verification_status: draft
---

# Transcription (LLM vision OCR)


<!-- page 1 -->

# FOUNDATIONAL ASPECTS OF THEORIES OF MEASUREMENT

BY DANA SCOTT AND PATRICK SUPPES

TECHNICAL REPORT NO. 6

APRIL 1, 1957

PREPARED UNDER CONTRACT Nonr 225(17) (NR 171-034) FOR OFFICE OF NAVAL RESEARCH

REPRODUCTION IN WHOLE OR IN PART IS PERMITTED FOR ANY PURPOSE OF THE UNITED STATES GOVERNMENT

BEHAVIORAL SCIENCES DIVISION  
APPLIED MATHEMATICS AND STATISTICS LABORATORY  
STANFORD UNIVERSITY  
STANFORD, CALIFORNIA

<!-- page 2 -->

# FOUNDATIONAL ASPECTS OF THEORIES OF MEASUREMENT$^{1/}$

by Dana Scott and Patrick Suppes

1. <u>Definition of Measurement.</u> It is a scientific platitude that there can be neither precise control nor prediction of phenomena without measurement. The point of a theory of measurement is to make explicit the structure that a set of empirical data must satisfy in order to apply numerical computations to them. From an abstract standpoint a set of empirical data consists of a collection of relations between a specified set of objects. The problem of measurement is to assign numbers to the objects in such a way that the relations receive an exact and reasonable numerical interpretation.

In constructing a particular theory of measurement it is not appropriate to consider only a single set of data, for the theory should be applicable to many situations. Furthermore the theory is not concerned with all possible sets of data on relevant sets of objects, but only with those which have a structure fixed in advance. Finally coherence is given to the theory by specifying a uniform numerical interpretation of this structure.

Before turning to problems connected with construction of theories of measurement, we want to give a precise set-theoretical meaning to the notions involved. To begin with, we treat sets of empirical data as being (finitary) relational systems, that is to say, finite sequences of the form

$$\mathfrak{A} = \langle A, R_1, \dots, R_n \rangle,$$

where $A$ is a non-empty set of elements called the <u>domain</u> of the relational system $\mathfrak{A}$, and $R_1, \dots, R_n$ are finitary relations on $A$. The relational system $\mathfrak{A}$ is called <u>finite</u> if the set $A$ is finite;

---

$^{1/}$ This research was supported under Contract NR 171-034, Group Psychology Branch, Office of Naval Research.

<!-- page 3 -->

otherwise, <u>infinite</u>. It should be obvious from this definition that we are mainly considering <u>qualitative empirical data</u>. Intuitively we may think of each particular relation $R_i$ (an $m_i$-ary relation, say) as representing a complete set of "yes" or "no" answers to a question asked of every $m_i$-termed sequence of objects in $A$. The point of this paper is not to consider that aspect of measurement connected with the actual collection of data, but rather the analysis of relational systems and their numerical interpretations.

If $s = \langle m_1, \dots, m_n \rangle$ is an $n$-termed sequence of positive integers then a relational system $\mathfrak{A} = \langle A, R_1, \dots, R_n \rangle$ is of <u>type</u> $s$ if for each $i = 1, \dots, n$ the relation $R_i$ is an $m_i$-ary relation. Two relational systems are <u>similar</u> if there is a sequence $s$ of positive integers such that they are both of type $s$. Notice that type of a relational system is uniquely determined only if all the relations are non-empty; the avoiding of this ambiguity is not worthwhile.

Suppose that two relational systems $\mathfrak{A} = \langle A, R_1, \dots, R_n \rangle$ and $\mathfrak{B} = \langle B, S_1, \dots, S_n \rangle$ are of type $s = \langle m_1, \dots, m_n \rangle$. Then $\mathfrak{B}$ is a <u>homomorphic image of</u> $\mathfrak{A}$ if there is a function $f$ from $A$ onto $B$ such that for each $i = 1, \dots, n$ and for each sequence $\langle a_1, \dots, a_{m_i} \rangle$ of elements of $A$

$$R_i(a_1, \dots, a_{m_i}) \quad \text{if and only if} \quad S_i(f(a_1), \dots, f(a_{m_i})).$$

If the function $f$ is one-one, then $\mathfrak{B}$ is an <u>isomorphic image of</u> $\mathfrak{A}$ or simply $\mathfrak{A}$ and $\mathfrak{B}$ are <u>isomorphic</u>. $\mathfrak{A}$ is a <u>subsystem of</u> $\mathfrak{B}$ if $A \subseteq B$ and for each $i = 1, \dots, n$, the relation $R_i$ is the restriction of the relation $S_i$ to $A$. $\mathfrak{A}$ is <u>imbeddable in</u> $\mathfrak{B}$ if some subsystem of $\mathfrak{B}$ is a homomorphic

<!-- page 4 -->

image of $\mathfrak{A}$.$^{2/}$ A <u>numerical relational system</u> is simply a relational system whose domain of elements is the set $Re$ of all real numbers. A <u>numerical assignment</u> for a relational system $\mathfrak{A}$ with respect to a numerical relational system $\mathfrak{N}$ is a function which imbeds $\mathfrak{A}$ in $\mathfrak{N}$. A numerical assignment is not required to be one-one.

Within the framework of the preceeding formal definitions it is now possible to give an exact characterization of a theory of measurement. First of all the general outlines of a theory are determined by fixing a finite sequence $s$ of positive integers and only considering relational systems of type $s$. Next a numerical relational system $\mathfrak{N}$ of type $s$ is selected which corresponds to the intended numerical interpretation of the theory, and only relational systems imbeddable in $\mathfrak{N}$ are permitted. Moreover the theory need not concern all relational systems of type $s$ imbeddable in $\mathfrak{N}$ but only a distinguished subclass. Since it is reasonable that no special set of objects be preferred, we require that the distinguished subclass be closed under isomorphism. Indeed, those who desire to characterize theories of measurement as definite entities may actually identify each theory with its distinguished class of relational systems; to be more specific, it might be said that a theory of measurement <u>is</u> a class $K$ of relational systems closed under isomorphism for which there exists a finite sequence $s$ of positive integers and a numerical relational system $\mathfrak{N}$ of type $s$ such that all

---

$^{2/}$ Although in most mathematical contexts imbeddability is defined in terms of isomorphism rather than homomorphism, for theories of measurement this is too restrictive.

<!-- page 5 -->

relational systems in $K$ are of type $s$ and imbeddable in $\mathfrak{N}$.$^{3/}$ Though this definition has the advantage of formal correctness and even some intuitive justification, we do not maintain that this is the only possible definition of a theory of measurement. But when no definition is given at all it is hardly possible to ask, let alone answer, many interesting and natural questions. For this reason, if for no other, we are willing to commit ourselves to the proposed definition.

Some readers may object that the definition of theories of measurement should be linguistic rather than set-theoretical in character, since a theory is ordinarily thought of as a linguistic entity. To be sure, many theories of measurement have a natural formalization in first-order predicate logic with identity. Notice, however, that first-order axioms by themselves are not adequate, for if they admit one infinite relational system as a model then they have models of every infinite cardinality, and it is difficult to see how any natural connection can be established between numerical models and models of arbitrary cardinality. Even neglecting this criticism first-order axioms are not adequate to express properties involving arbitrary natural numbers; for example, the fact that a relational system is finite or that as an ordering it has Archimedean properties. Any linguistic definition of theories which will permit expression of these more general properties would require extensive machinery and be immediately involved

---

$^{3/}$ <u>In some contexts we shall say that the class $K$ is a theory of measurement of type $s$ relative to $\mathfrak{N}$.</u> Notice that a consequence of this definition is that if $K$ is a theory of measurement, then so, is every subclass of $K$ closed under isomorphism. Moreover, the class of all systems imbeddable in members of $K$ is also a theory of measurement.

<!-- page 6 -->

in some of the deepest problems of modern metamathematics. On the other hand, we do not wish to give the impression that we reject any linguistic questions. In fact, we use our set-theoretical definition as a point of departure for asking just such questions.

On the basis of the definition of theories of measurement adopted, two questions naturally arise, to each of which we devote a section. In the first place, is a given class of relational systems a theory of measurement? And in the second place, given a theory of measurement in what sense can it be axiomatized?

We would like to record here our indebtedness to Professor Alfred Tarski whose clear and precise formulation of the mathematical theory of models$^{4/}$ has greatly influenced our presentation. Although our theories of measurement do not constitute special cases of the arithmetic classes of Tarski, the notions are closely related, and we have made use of results and methods from the theory of models.

2. <u>Existence of Measurement.</u> A simple counterexample shows that not every class of relational systems of a given type closed under isomorphism is a theory of measurement. Let $\mathcal{O}$ be the class of all relational systems of type $\langle 2 \rangle$ that are simple orderings. Let $\langle A, R \rangle$ be a system in $\mathcal{O}$ where $R$ well-orders $A$ and $A$ has a power not equal to or less than that of the continuum. Such a relational system can be proved to exist even without the help of the axiom of choice, but of course with aid of this axiom the existence is obvious. By way of contradiction suppose that $\mathcal{O}$ is a theory of measurement

---

$^{4/}$ See Tarski [6].

<!-- page 7 -->

relative to a numerical relational system $\langle Re, S \rangle$. From the definition it follows that $\langle A, R \rangle$ is imbeddable in $\langle Re, S \rangle$ and that there is a numerical assignment $f$ mapping $A$ onto a subset of $Re$ such that

$$xRy \quad \text{if and only if} \quad f(x)\ S\ f(y)$$

for all elements $x, y \in A$. Let $a, b$ be elements of $A$ such that $f(a) = f(b)$. From the hypothesis that $R$ is a simple ordering, we can assume without loss of generality that $aRb$. Hence, we have $f(a)\ S\ f(b)$, and then $f(b)\ S\ f(a)$, and finally $bRa$. $R$ is antisymmetric, and so $a = b$. This argument shows that the function $f$ is one-one. Whence, $A$ has the same power as a subset of $Re$, which is impossible.

This proof shows that every theory of measurement included in the class $\mathcal{O}$ contains only relational systems of power at most that of the continuum. It is an unsolved problem of set-theory closely connected with the continuum hypothesis whether the class $\mathcal{O}$ restricted to systems of power at most that of the continuum is actually a theory of measurement.$^{5/}$ At least it can be very easily shown that $\mathcal{O}$ so restricted is not a theory of measurement relative to the system $\langle Re, \le \rangle$, where the relation $\le$ is the usual ordering of the real numbers.$^{6/}$ Indeed, the exact condition that a relational system in $\mathcal{O}$ must satisfy to be imbeddable in $\langle Re, \le \rangle$, is not really

---

$^{5/}$ In this connection see Sierpinski [4] Section 7, page 141 ff., in particular Proposition $C_{75}$, where of course different terminology is used.

$^{6/}$ It is sufficient here to consider a relational system isomorphic to the ordering of the ordinals of the second number class or to the lexicographical ordering of all pairs of real numbers.

<!-- page 8 -->

elementary and the proof of the necessity involves the axiom of choice.$^{7/}$

Let $\mathcal{O}'$ be $\mathcal{O}$ restricted to countable$^{8/}$ relational systems. It was proved by Cantor that $\mathcal{O}'$ is a theory of measurement relative to $\langle Re, \le \rangle$, to formulate somewhat irreverently his classical result in the terminology of this paper. This restriction to countable relational systems is always sufficient. For it can be shown that the class of <u>all</u> countable relational systems of a given type is a theory of measurement; however, the numerical relational system required is so bizarre as to be of no practical value.

One of the aims of measurement is to provide a means of convenient computation. But among the morass of all possible numerical relational systems only a very few are of any computational value, indeed only those definable in terms of the ordinary arithmetical notions. From an empirical standpoint most sets of qualitative data can find numerical interpretation by relations defined in terms of addition and ordering alone. By way of example we may cite the measurement of masses, distances, sensation intensities, and subjective probabilities. Frequently the consideration of weighted averages requires also the use of the multiplication of numbers. However, in the examples given in this paper we shall restrict ourselves to the notions of addition and ordering.

No natural scientific situation would seem strictly to require the consideration of sets of infinite data. This state of affairs suggests that theories of measurement containing only finite relational systems would

---

$^{7/}$ A simple ordering is imbeddable in $\langle Re, \le \rangle$ if and only if it contains a countable dense subset. For the exact formulation and a sketch of a proof see Birkhoff [1], pp. 31-32, Theorem 2.

$^{8/}$ The word 'countable' means at most denumerable and it refers to the cardinality of the domains of the relational systems.

<!-- page 9 -->

suffice for empirical purposes. The problem is delicate, however, for the measurement of a meteorological quantity such as temperature by an automatic recording device is usually treated as continuous both in its own scale and in time. Yet the important problem of measurement does not really lie in the correct use of such recording devices but rather in their initial calibration, a process proceeding from a finite number of qualitative decisions. Because of the akwardness of the uniform application of finite relational systems, we shall not generally make this restriction.

Further remarks about establishing the existence of measurement are best motivated by reference to a concrete example. In a recent paper$^{9/}$ R. D. Luce has introduced a generalization of simple orderings which he calls <u>semiorders</u>. A <u>semiorder</u> is a relational system $\langle A, P \rangle$ of type $\langle 2 \rangle$ which satisfies the following axioms for all $x, y, z, w \in A$:

S1. <u>Not</u> $xPx$.

S2. <u>If</u> $xPy$ <u>and</u> $zPw$, <u>then</u> <u>either</u> $xPw$ <u>or</u> $zPy$.

S3. <u>If</u> $xPy$ <u>and</u> $zPx$, <u>then</u> <u>either</u> $wPy$ <u>or</u> $zPw$.$^{10/}$

Such relations are most likely to occur in situations where objects are to be arranged in order and where it is difficult to say exactly when two objects are indifferent. For example, to say that $xPy$ might be interpreted as meaning that the pitch of the sound $x$ is <u>definitely higher</u> than the pitch

---

$^{9/}$ See Luce [3].

$^{10/}$ See Luce [3] Section 2, p. 181. The axioms given here are actually a simplification of those given by Luce.

<!-- page 10 -->

of $y$, or that the hue of color $x$ is <u>definitely brighter</u> than the hue of color $y$, or that the weight of the object $x$ is <u>noticeably greater</u> than that of $y$, etc. Indifference between two objects $x$ and $y$ (in symbols: $xIy$) is defined as not $xPy$, and not $yPx$. The point of Luce's axioms is that the relation $I$ of indifference is not always transitive, a fact easily appreciated for each of the intuitive interpretations given above.

In his paper Luce gives a certain numerical interpretation for certain kinds of semiorders, but he does not show that any particular class of semiorders is a theory of measurement in the sense used here, because his interpretations are not relative to a fixed numerical relation. In the denumerable case the situation is very simple indeed. Let $\gg$ be the relation between real numbers defined by the condition

$$x \gg y \quad \text{if and only if} \quad x > y + 1.$$

Obviously, if $x$ and $y$ are real numbers such that $x \gg y$, then $x$ is <u>definitely greater than</u> $y$ or better $x$ is <u>noticeably greater than</u> $y$. The following result is not difficult to establish.

<u>The class of countable semiorders is a theory of measurement relative to the numerical relational system $\langle Re, \gg \rangle$ (which is itself a semiorder).</u>

It is possible to characterize all semiorders imbeddable in $\langle Re, \gg \rangle$, similar to the result for simple orderings, but this shall not concern us here.

For the remainder of this discussion let $C$ be the class of all countable semiorders. The class $C$ affords an example of a theory of measurement (relative to $\langle Re, \gg \rangle$) for which not all numerical assignments are one-one functions.$^{11/}$ However, this theory has the peculiarity that those systems

---

$^{11/}$ For example, consider any semiorders in which any two elements are indifferent.

<!-- page 11 -->

having only one-one assignments can be distinguished by a simple additional axiom. Let $\langle A, P \rangle$ be any semiorder. Define a relation $E$ between elements of $A$ by the condition

$$xEy \quad \text{if and only if for all } z \in A \text{ the formulas } xIz \text{ and } yIz \text{ are equivalent.}$$

The relation $E$ is easily proved to be an equivalence relation, and, in fact, it is a congruence relation in the sense that for all $x, y, z \in A$

$$\text{if } xPz \text{ and } xEy \text{ then } yPz, \text{ and}$$
$$\text{if } zPx \text{ and } xEy, \text{ then } zPy.$$

Furthermore, we can show that if $f$ is any numerical assignment imbedding $\langle A, P \rangle$ in $\langle Re, \gg \rangle$ then for all $x, y \in A$, if $f(x) = f(y)$, then $xEy$. Consider then the axiom:

<u>S4.</u> If $xEy$, then $x = y$.

Let $C^*$ be the class of all systems in $C$ which satisfy S4. Clearly from our remarks above it follows that any system in $C^*$ has only one-one numerical assignments. In the other direction, assume that $\langle A, P \rangle$ is a system in $C$ possessing only one-one assignments. Since the relation $E$ is a congruence relation for the system $\langle A, P \rangle$, we can reduce by $E$ and form a system of cosets $\langle A^*, P^* \rangle$, where $A^*$ is the family of equivalence classes under $E$, and $P^*$ is defined in the natural way. Obviously $\langle A^*, P^* \rangle$ is in $C^*$ and $\langle A, P \rangle$ is imbeddable in $\langle A^*, P^* \rangle$ (in fact, $\langle A^*, P^* \rangle$ is a homomorphic image of $\langle A, P \rangle$). Let $f^*$ be any assignment for $\langle A^*, P^* \rangle$. In a straightforward way we can define an assignment $f$ for $\langle A, P \rangle$ such

<!-- page 12 -->

that $f(x) = f^*([x])$, where $x \in A$ and $[x]$ is the $E$-equivalence class of $x$. Now by assumption $f$ is one-one. Hence if $xEy$, then $[x] = [y]$, and so $f^*([x]) = f^*([y])$, which implies $f(x) = f(y)$ and $x = y$. Thus $\langle A, P \rangle$ itself satisfies S4. We have shown that $C^*$ is exactly the class of all systems in $C$ possessing only one-one assignments.

To be truthful, the above discussion has somewhat inverted the natural sequence of steps. In order to establish the existence of measurement for $C$ (that is, to show that $C$ is a theory of measurement relative to $\langle Re, \gg \rangle$), it is far better to consider the class $C^*$ first and prove that it is a theory of measurement relative to $\langle Re, \gg \rangle$. Finally it need only be remarked that every system in $C$ can be imbedded in a system of $C^*$ by the method of cosets. As a matter of fact it can also be proved that every system in $C$ is a sub-system of some system in $C^*$, which is another method of proving that $C$ is a theory of measurement.

Let us now summarize the steps in establishing the existence of measurement using as models the simple orderings and the semiorders. First, after one is given a class, $K$ say, of relational systems, the numerical relational system should be decided upon. The numerical relational system should be naturally suggested by the structure of the systems in $K$, and as was remarked, it is most practical to consider numerical systems where all the relations can be simply defined in terms of addition and ordering of real numbers. Second, if the proof that $K$ is a theory of measurement is not at once obvious, the cardinality of systems in $K$ should be taken into consideration. The restriction to countable systems would always seem empirically justified, and adequate results are often possible with a restriction to finite systems. Third, the

<!-- page 13 -->

proof of the existence of measurement can often be simplified by the reduction of each relational system in $K$ by the method of cosets. One usually looks for a uniform and natural method of introducing into each relational system in $K$ an equivalence relation which preserves all the relations between the elements. Then, instead of trying to find numerical assignments for each member of $K$, one concentrates only on the reduced systems. This plan was very helpful in the case of semiorders. Instead of cosets, it is sometimes feasible to consider imbedding by subsystems. That is to say, one considers some convenient subclass $K' \subseteq K$ such that every element of $K$ is a subsystem of some system in $K'$. If $K'$ is a theory of measurement then so is $K$. In the case of semiorders we could have used either plan: cosets or subsystems.

After the existence of measurement has been established, there are two questions which are often of interest: for a given relational system what is the class of all its numerical assignments? and how can the class of all systems isomorphic to the given system be described? These two questions are not unrelated, though in some cases one can be answered without deciding the other. We shall present two examples.

Consider relational systems $\langle A, D \rangle$ of type $\langle 4 \rangle$. For such systems we introduce the following definitions:

$$xRy \quad \text{if and only if} \quad xyDyy$$

$$xyM^1 zw \quad \text{if and only if} \quad xyDzw, zwDxy, yRz \text{ and } zRy$$

$$xyM^{n+1} zw \quad \text{if and only if there exist}$$
$$u, v \in A \text{ such that}$$
$$xyM^n uv \quad \text{and} \quad uvM^1 zw.$$

<!-- page 14 -->

Let $H$ be the class of all relational systems $\langle A, D \rangle$ of type $\langle 4 \rangle$ which satisfy the following axioms for every $x, y, z, u, v, w \in A$:

A1. <u>If</u> $xyDzw$ <u>and</u> $zwDuv$ <u>then</u> $xyDuv$.

A2. $xyDzw$ <u>or</u> $zwDxy$.

A3. <u>If</u> $xyDzw$ <u>then</u> $xzDyw$.

A4. <u>If</u> $xyDzw$ <u>then</u> $wzDyx$.

A5. <u>If</u> $xRy$ <u>and</u> $yzDuv$ <u>then</u> $xzDuv$.

A6. <u>There is a</u> $z \in A$ <u>such that</u> $xzDzy$ <u>and</u> $zyDxy$.

A7. <u>If not</u> $xyDzw$ <u>and not</u> $xRy$ <u>then there is a</u> $u \in A$ <u>such that</u> $zwDxu$, <u>not</u> $xRu$ <u>and not</u> $uRy$.

A8. <u>If</u> $xyDzw$ <u>and not</u> $xRy$ <u>then there are</u> $u, v \in A$ <u>and an</u> $n$ <u>such that</u> $zuM^n vw$ <u>and</u> $zuDxy$.

These axioms imply that for a system $\langle A, D \rangle$ in $H$, the relation $R$ is a weak ordering of $A$, and the intuitive interpretation of $xyDzw$ in case $yRx$ and $wRz$ is that the interval between $x$ and $y$ is not greater than the interval between $z$ and $w$. Making heavy use of the last three existence axioms (note that A8 gives an Archimedean property to the ordering), it can be shown that $H$ is a theory of measurement relative to the numerical relational system $\langle Re, \Delta \rangle$ where $\Delta$ is the quaternary relation defined by the condition

$$xy \Delta zw \quad \text{if and only if} \quad x - y \le z - w$$

for all $x, y, z, w \in Re$. In addition, it can be shown that if $\langle A, D \rangle$ is in

<!-- page 15 -->

$H$ and $f$ and $g$ are two numerical assignments of $\langle A, D \rangle$ relative to $\langle Re, \Delta \rangle$, then $f$ and $g$ are related by a positive linear transformation;$^{12/}$ that is, there exist $\alpha, \beta \in Re$ with $\alpha > 0$ such that for all $x \in Re$, $f(x) = \alpha g(x) + \beta$. This gives in a certain sense the answer to the first question above: if we know one numerical assignment of $\langle A, D \rangle$, we know them all. Except for very special systems in $H$, nothing more specific can really be expected.

Notice that all relational systems in $H$ are necessarily infinite. In the next section we shall consider in detail the theory of measurement $F$ consisting of all finite relational systems imbeddable in $\langle Re, \Delta \rangle$. Here the situation is quite hopeless. There simply is no apparent general statement that can be made about the relation between assignments. In as much as any function $\varphi$ which imbeds $\langle Re, \Delta \rangle$ in itself is necessarily a linear transformation and conversely, it follows that if $\langle A, D \rangle$ is a system in $F$ and $f$ is an assignment for $\langle A, D \rangle$, then $f$ composed with a linear transformation is also an assignment. The main difficulty with $F$ is that two assignments for the same system in $F$ need not be related by a linear transformation.

The situation with regard to the class $C^*$ of semiorders introduced above is much the same as that for $F$, in as much as there is no apparent relation between assignments. However, though it seems difficult to describe all the different finite systems in $F$, we can answer this question for the finite systems in $C^*$. The description is facilitated by the following definition.

---

$^{12/}$ The proofs of both these facts about $H$ are very similar to the corresponding proofs in Suppes and Winet [5].

<!-- page 16 -->

Let $s = \langle s_1, \dots, s_n \rangle$ and $t = \langle t_1, \dots, t_n \rangle$ be two finite sequences of positive integers of the same length $n$. We write $s \varepsilon t$ to mean:

(i) $s_{i+1} > s_i$ for $i < n$,

(ii) $t_{i+1} > t_i$ for $i < n$,

(iii) $s_i > t_i$ for $i \le n$.

Let $m$ be any integer not less than $s_n$. We define $\mathcal{O}_m(s,t)$, where $s \varepsilon t$, to be the relational system $\langle A, P \rangle$, where $A = \{1, \dots, m\}$ and the binary relation $P$ is defined by the condition

$$k P \ell \quad \text{if and only if there is an integer } i \le n \text{ such that}$$

$$k \ge s_i > t_i \ge \ell$$

for all $k, \ell \in A$.

It is possible without much trouble to establish the following facts:

(1) $\mathcal{O}_m(s,t)$ is a semiorder;

(2) If $\mathcal{O}_m(s,t)$ satisfies axiom S4, and if $\mathcal{O}_m(s,t)$ is isomorphic to $\mathcal{O}_{m'}(s',t')$, then $m = m'$, $s = s'$, and $t = t'$;

(3) Any finite semiorder is isomorphic to a system $\mathcal{O}_m(s,t)$ for suitable $m$, $s$, and $t$.

Thus what has been accomplished is the exhibition of exactly one representative of each isomorphism type of finite semiorders which satisfy axiom S4. Actually, with very little more effort we could do the same for arbitrary finite semiorders. Since a system $\mathcal{O}_m(s,t)$ seems to be a definite object that we can constructively define, we feel that this construction yields an adequate
