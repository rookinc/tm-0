# Experiment 028

## Title

Boundary Persistence Conditions Admissibility

## Status

Executable candidate.

## Question

Can admissibility be derived from persistence of the current boundary
rather than from an arbitrary character score?

## Starting Result

Experiment 027 showed that character can condition admissibility.

Its monotone POLAR-count rule was a toy scaffold.

Experiment 028 replaces that score with a structural condition.

## Construction

The current possibility partition defines a boundary through:

    character classification

    adjacency

    cross-class contact

Each candidate realization produces a resulting partition.

A candidate is admissible when the resulting boundary set is identical
to the current boundary set.

A candidate is placed in structured absence when it moves, creates, or
removes boundary addresses.

## Result

A candidate preserving the boundary is admitted.

A candidate changing the boundary is placed in structured absence.

Mixed candidate sets partition cleanly.

Internal changes that leave the boundary unchanged remain admissible.

## Interpretation

Boundary persistence can act as a structural admissibility law.

This is stronger than ranking character by an arbitrary scalar.

The rule asks whether the current inside/outside distinction survives
the candidate realization.

## Consequence

The executable TM-0 loop now supports:

    character

        ->

    possibility partition

        ->

    boundary

        ->

    boundary-persistence constraint

        ->

    admissible frontier
    structured absence

## Boundary

The current partition and adjacency are supplied to the experiment.

The experiment does not yet derive the candidate resulting partitions
from the signed-graph character update.

It does not prove that all lawful bodies must preserve their boundary.

Boundary change may later describe growth, decay, division, or failure
rather than inadmissibility.

No agency, selection, probability, time, energy, geometry, or physical
motion is introduced.

## Keeper

A realization may change character without changing who is inside.
