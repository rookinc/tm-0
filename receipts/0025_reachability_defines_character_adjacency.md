# Receipt 0025

## Title

Reachability Defines Character Adjacency

## Status

Research receipt.

## Result

One-bit distance in cycle-space character does not always match
one-step realization reachability.

A chord-edge realization may change one cycle-space bit.

A tree-edge realization may change several cycle-space bits while
remaining one local act.

## Interpretation

Character distance is not the general mechanical definition of
adjacency.

The correct adjacency relation is:

    one available local realization connects the states

This may coincide with one-bit distance in some cases.

It need not coincide in general.

## Consequence

The possibility address space inherits its neighbourhood from the
current realization operators.

Boundary should therefore be evaluated across reachable transitions,
not across abstract Hamming distance alone.

## Correction

Experiment 024 remains a valid coordinate-level construction.

It does not define the full mechanical neighbourhood.

Experiment 025 replaces:

    one bit differs
        -> adjacent

with:

    one lawful realization reaches the target
        -> adjacent

## Limitation

The current model still treats every local edge-sign flip as available.

It has not yet derived which realizations are admissible from the
current character.

It does not introduce resolution, selection, probability, agency,
time, energy, or physical motion.

## Keeper

Character distance describes separation.

Realization defines the next step.
