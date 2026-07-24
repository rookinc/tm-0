# Receipt 0011

## Title

Closure Needs Junctions, Not Named Carriers

## Status

Research receipt.

## Result

A directed sequence can compose and close using only:

    relation-local source ports

    relation-local target ports

    endpoint-equivalence registrations

No named carrier or vertex is required.

## Open Chain

    target(0) = source(1)

    target(1) = source(2)

The relations compose, but do not return.

## Closed Chain

Add:

    target(2) = source(0)

The same sequence now returns to its first source junction.

## Interpretation

The load-bearing structure is not carrier naming.

It is registered endpoint sameness.

## Consequence

The current ladder becomes:

    direction
        gives source and target ports

    endpoint equivalence
        gives junctions

    junctions
        permit composition

    closed composition
        gives return

## Keeper

Closure does not ask what the carriers are called.

Closure asks whether the final port is the first junction.
