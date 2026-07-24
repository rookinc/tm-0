# Experiment 026

## Title

Structured Absence From Constraint

## Status

Executable candidate.

## Question

Can a constraint partition the possibility frontier into admissible
realizations and structured absence without deleting any address from
possibility?

## Starting Result

Experiment 022 defined possibility as an address space of candidate
local realizations.

Experiment 025 showed that one-step reachability is induced by actual
local realizations.

## Toy Constraint

Experiment 026 applies one minimal non-backtracking rule:

    the address used by the most recent realization
    is excluded from the next admissible frontier

This is a scaffold only.

It is not proposed as a universal TM law.

## Construction

The full possibility frontier remains unchanged.

It is partitioned into:

    admissible

    structured absence

If there is no previous address, all candidates are admissible.

If there is a previous address, that address remains in possibility
but is placed in structured absence.

## Result

The blocked address remains fully addressable.

It is excluded from immediate realization.

The admissible and absent sets are disjoint.

Their union reconstructs the full possibility frontier.

## Interpretation

Constraint does not destroy possibility.

Constraint structures absence within possibility.

Structured absence is therefore:

    addressable
    identifiable
    currently inadmissible

## Consequence

The executable TM-0 loop now contains:

    character

        ->

    possibility frontier

        ->

    constraint partition

        ->

    admissible frontier
    structured absence

Resolution remains absent.

No candidate is selected or executed by this experiment.

## Boundary

The non-backtracking rule is assumed for the experiment.

The experiment does not derive constraint from cycle character.

It does not introduce agency, preference, policy, probability, time,
energy, geometry, or physical motion.

## Keeper

Constraint does not erase an address.

It makes the address absent from the present frontier.
