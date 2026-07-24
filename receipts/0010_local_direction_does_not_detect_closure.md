# Receipt 0010

## Title

Local Direction Does Not Detect Closure

## Status

Research receipt.

## Result

A rooted open path and a rooted directed cycle can have identical
anonymous local directed profiles.

Both roots have:

    indegree = 1

    outdegree = 1

Yet only the directed cycle admits a positive-length return to its
root.

## Interpretation

Incoming and outgoing roles are insufficient to determine closure.

The missing structure is endpoint incidence across composed
relations.

## Consequence

The current ladder is:

    direction
        gives source and target roles

    incidence
        permits composition

    composition
        permits paths

    closed composition
        permits return

Incidence is now an earned candidate mechanism.

It is not yet declared primitive.

## Keeper

A local arrow can show direction.

Only composed incidence can show that the arrow came home.
