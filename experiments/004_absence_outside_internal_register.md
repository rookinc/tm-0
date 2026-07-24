# Experiment 004

## Title

Absence Outside the Internal Register

## Status

Executable candidate.

## Question

Is ABSENT a lawful internal register value, or does it describe the
absence of a carrier instance?

## Competing Models

Experiment 003 used the quotient register:

    ABSENT
    NULL
    CHARACTERIZED

Experiment 004 separates carrier presence from internal registration.

Carrier condition:

    absent
    present

Internal register of a present carrier:

    NULL
    CHARACTERIZED

## Construction

Carrier absence is represented by:

    None

Carrier instantiation is:

    None -> Carrier(NULL)

Internal realization is:

    Carrier(NULL) -> Carrier(CHARACTERIZED)

Return to null is:

    Carrier(CHARACTERIZED) -> Carrier(NULL)

## Result Sought

If the current mechanics survives without ABSENT as an internal value,
then ABSENT has not earned membership in the possibility address space
of an existing carrier.

## Interpretation

Possibility is the internal address space.

A carrier must exist before it can occupy an address in that space.

NULL is the first lawful internal address.

Absence is a construction condition outside the register.

## Boundary

This experiment does not derive the carrier.

It does not prove that NULL and CHARACTERIZED are the only internal
states.

It does not derive polarity, return, character accumulation, history,
relation, closure, witness, graph structure, or physical behaviour.
