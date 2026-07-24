# Experiment 002

## Title

Minimal Addressed-State Realization

## Status

Executable candidate.

## Question

Can TM-0 distinguish carrier existence from registration character
without assuming history, geometry, graphs, agency, or accumulated
character?

## Address Space

The experiment uses four addressable values:

    ABSENT
    NULL
    A
    B

ABSENT means no carrier is present.

NULL means a carrier is present with null registration.

A and B are characterized registrations.

## Candidate Transition Law

A realization changes the addressed state.

A realization need not produce A/B character.

Therefore:

    ABSENT -> NULL

is a realization even though the resulting registration is null.

Identity transitions are excluded:

    ABSENT -> ABSENT
    NULL   -> NULL
    A      -> A
    B      -> B

## Tested Realizations

    ABSENT -> NULL
    NULL   -> A
    NULL   -> B
    A      -> NULL
    B      -> NULL
    A      -> B
    B      -> A

## Boundary

This experiment does not establish that these are the only states or
transitions.

It does not model character accumulation, return cycles, witness,
relation, graph structure, probability, time, physical motion, or
higher-register observation.

It tests only whether carrier presence and registration character can
be separated in the smallest current executable model.
