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
