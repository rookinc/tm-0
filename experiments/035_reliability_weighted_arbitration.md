# Experiment 035

## Title

Reliability-Weighted Arbitration

## Status

Executable candidate.

## Question

Can accumulated witness reliability resolve disagreement more
informatively than simple report count?

## Starting Result

Experiment 034 made witness reliability an accumulated result of later
closure comparison.

Experiment 032 used strict majority without reliability weighting.

## Construction

Each witness contributes:

    current report

    accumulated reliability history

The current toy weight is:

    confirmed - contradicted

Total weight is accumulated separately for:

    SAME

    POLAR

The greater total resolves the disagreement.

Equal total weight remains unresolved.

## Result

Equal reliability weight remains unresolved.

The more reliable report resolves the disagreement.

One reliable dissenting witness can outweigh two weak reports.

A witness with no evaluated history contributes zero weight.

Negative reliability counts against the report being made.

## Interpretation

Witness influence can emerge from accountable history rather than
headcount alone.

A majority of weak reports need not outweigh one strongly receipted
dissent.

## Consequence

The witness layer now contains:

    independent provenance

    accumulated closure history

    earned reliability

    reliability-weighted arbitration

## Important Boundary

The current weight rule is a toy scaffold.

Negative reliability may need a different treatment.

The experiment does not prove that net confirmation count is the right
measure of reliability.

It does not model context dependence, uncertainty, coordinated error,
forgery, or reliability decay.

## Keeper

Witness count says how many spoke.

Reliability history says how much their reports have earned.
