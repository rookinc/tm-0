# Experiment 016

## Title

Cycle Sign Product

## Status

Executable candidate.

## Question

Is returned orientation determined exactly by the product of local
orientation signs around a closed relation cycle?

## Starting Result

Experiment 015 showed that incidence does not select between:

    PRESERVE

    INVERT

Local orientation behaviour is additional structure.

## Construction

Each relation carries one local sign:

    PRESERVE = +1

    INVERT = -1

For a closed cycle C, define:

    Sigma(C) = product of all local signs on C

## Expected Law

    Sigma(C) = +1 -> SAME

    Sigma(C) = -1 -> POLAR

## Tested Cases

All local signs preserve:

    product = +1

    registration = SAME

One local inversion:

    product = -1

    registration = POLAR

Two local inversions:

    product = +1

    registration = SAME

The result depends on inversion parity, not cycle length alone.

## Interpretation

Returned polarity is a closure residue of local orientation character.

Odd cycle length predicts polarity only in the special case where
every local relation inverts.

The more general invariant is the sign product around the cycle.

## Boundary

This experiment does not derive the local signs.

It does not establish why a relation preserves or inverts.

It does not yet derive a cocycle law, switching equivalence, character
accumulation, witness, or a thalion.

## Keeper

The cycle does not ask how many relations it contains.

It asks what local character survives their product.
