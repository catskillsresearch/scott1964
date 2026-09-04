/-
Copyright (c) 2026  Lars Warren Ericson.  All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Lars Warren Ericson.
-/

import Scott1964.MeasurementStructures.FinHead
import Scott1964.MeasurementStructures.LinearInequalities.Definitions
import Scott1964.MeasurementStructures.LinearInequalities.Separation
import Scott1964.MeasurementStructures.LinearInequalities.Rationalization
import Scott1964.MeasurementStructures.LinearInequalities.Sequences
import Scott1964.MeasurementStructures.LinearInequalities.ScottTheorems
import Scott1964.MeasurementStructures.LinearInequalities.OrderedGroup
import Scott1964.MeasurementStructures.Preference.Direct
import Scott1964.MeasurementStructures.Preference.Cycle
import Scott1964.MeasurementStructures.Preference.Intransitive
import Scott1964.MeasurementStructures.Differences.Pair
import Scott1964.MeasurementStructures.Differences.Ordered
import Scott1964.MeasurementStructures.Probability.Basic
import Scott1964.MeasurementStructures.Probability.Atoms
import Scott1964.MeasurementStructures.Probability.Finite
import Scott1964.MeasurementStructures.Probability.KPSCounterexample
import Scott1964.MeasurementStructures.Probability.Infinite.EventSpace
import Scott1964.MeasurementStructures.Probability.Infinite.HahnBanach
import Scott1964.MeasurementStructures.Probability.Infinite.Kelley
import Scott1964.MeasurementStructures.Probability.Infinite.Reconstructed

/-!
# Scott 1964 — Measurement Structures and Linear Inequalities

Primary source: Dana S. Scott, *Measurement Structures and Linear
Inequalities*, Journal of Mathematical Psychology 1 (1964), 233–247.
Working transcription: `sources/ScottMeasurement1964_vision.md`.

The paper applies the general solvability criterion for finite systems of
linear inequalities (Theorems 1.1–1.4) to three measurement problems:
intransitive indifference (Theorem 2.1), ordered differences (Theorems 3.1
and 3.2), and subjective probability (Theorem 4.1).

This module re-exports the complete sorry-free development imported by
`Solution.lean`: Scott's eight published theorems, the finite KPS
counterexample, and the separately labelled modern reconstruction of the
infinite probability theorem.
-/

namespace Scott1964.MeasurementStructures

end Scott1964.MeasurementStructures
