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

The compared Palomar claim will be fixed in `Challenge.lean` /
`comparator.json` once the statement of record is chosen. The development
lives in `Scott1964/MeasurementStructures/`.

Palomar reviews and, if registered, preserves a pinned commit of *this*
repository.
