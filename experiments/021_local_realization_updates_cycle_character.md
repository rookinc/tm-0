# Experiment 021

## Title

Local Realization Updates Cycle Character

## Status

Executable candidate.

## Question

Can a local sign realization change switching-invariant cycle-space
character while preserving the graph incidence structure?

## Starting Result

Experiment 020 established that a connected signed graph carries a
cycle-space return signature.

The signature contains one invariant sign per independent cycle.

## Construction

Experiment 021 flips the sign of one relation:

    PRESERVE <-> INVERT

The vertex set and edge incidence remain unchanged.

The cycle-space signature is measured before and after the flip.

## Result

A local edge-sign flip changes the cycle-space character.

The graph incidence structure remains unchanged.

A chord flip changes one fundamental-cycle bit in the tested normal
form.

A tree-edge flip may change several fundamental-cycle bits because the
edge participates in several fundamental cycles.

## Interpretation

Character can change without rebuilding the relational body.

The body is the incidence structure.

The character is the switching-invariant cycle-space signature.

A local realization changes character according to the set of closed
relations that contain the affected edge.

## Consequence

TM-0 now has a first executable character update:

    chi_n -> chi_n+1

The update is local in the sign assignment and potentially distributed
in cycle space.

## Boundary

This experiment does not yet determine which edge flip is lawful or
possible.

It does not derive selection, probability, agency, energy, time, or
physical motion.

It does not yet update the future possibility address space.

## Keeper

A local realization can alter global return character without changing
the relational body.
