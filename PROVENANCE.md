# Provenance

This repository is a standalone Lean 4 formalization of Dana Scott's 1964
paper *Measurement Structures and Linear Inequalities* (Journal of
Mathematical Psychology 1 (1964), 233–247). It is not a thin wrapper and not
a reimplementation of an independent formalization.

Dana Scott did not participate in, review, or endorse this formalization.
The formalization was produced by Lars Warren Ericson without input from
Scott. The source paper is cited as literature only.

Sibling formalizations of related Scott papers:

- [`catskillsresearch/scott1972`](https://github.com/catskillsresearch/scott1972)
  — Continuous Lattices (LNM 274, 1972)
- [`catskillsresearch/scott1976`](https://github.com/catskillsresearch/scott1976)
  — Data Types as Lattices (PRG-5 / SIAM J. Comput. 5, 1976)
- [`catskillsresearch/scott1980`](https://github.com/catskillsresearch/scott1980)
  — PRG-19 neighborhood systems (1980/1981)
- [`catskillsresearch/scott1982`](https://github.com/catskillsresearch/scott1982)
  — Domains for denotational semantics / information systems (1982)

The 1964 measurement paper predates and is mathematically independent of the
domain-theory siblings above; nothing is imported from them.
**This repository is submitted to Palomar on its own**, for the 1964 paper
alone, following the same Challenge / Solution pattern as
[`catskillsresearch/cardb`](https://github.com/catskillsresearch/cardb) and
`scott1976`.

The Palomar statement of record compares all eight numbered theorems in the
published paper (1.1--1.4, 2.1, 3.1, 3.2, and 4.1) and one additional,
separately labelled modern result. The published Theorem 4.1 concerns finite
Boolean algebras. Scott's final paragraph only announces an infinite
extension without stating or proving it; this repository does not attribute
its `reconstructed_infinite_theorem_4_1` to Scott. That theorem is a modern
Hahn--Banach/Kelley reconstruction under the explicit
`GeneralizedKelleyCondition`.

Beyond the eight numbered theorems, the development formalizes source-facing
material that is not promoted to a ninth published theorem: Scott's
ordered-group observation via `finite_local_real_embedding`, a lexicographic
strictly-monotonic example and its global real-representation obstruction,
the literal vector-sum form of `(4_B)`, and Scott's p. 15 signed-charge
characterization. Theorem 2.1 currently uses the direct finite Scott--Suppes
staircase proof; `Preference/Cycle.lean` separately records the local
cycle-shortening reductions in Scott's 1964 argument.

The bundled `DeFinettiAxioms` counterexample is an integrated formalization of
the five-atom construction from Kraft, Pratt, and Seidenberg (1958), not an
additional numbered theorem of Scott's 1964 article. It proves both that the
exact KPS order satisfies those five axioms and that
`RealizableProbability` fails.

The sorry-free development lives in `Scott1964/MeasurementStructures/`.
`Challenge.lean` contains the deliberate Palomar holes. No project-defined
axioms are introduced; the compared proofs use only `propext`, `Quot.sound`,
and `Classical.choice`, as disclosed in `comparator.json`.

Palomar reviews and, if registered, preserves a pinned commit of *this*
repository.
