# Receipt 0049

## Title

Character Uses Independent Return Coordinates

## Status

Research receipt.

## Result

TM-0 can derive a compact binary character field from a fundamental
cycle basis.

The motion graph supplies:

    registered states

    directed relations

A deterministic spanning forest separates:

    tree relations

    non-tree relations

Each non-tree relation closes one fundamental cycle with the unique tree
path between its endpoints.

Each basis cycle becomes one character coordinate.

A state receives:

    one when it participates in that basis cycle

    zero otherwise

The character width equals the undirected cycle rank.

## Interpretation

Independent return structure does not require the full catalogue of
simple cycles.

A fundamental basis gives a compact address for the distinct ways the
graph can close.

State character can therefore record participation in independent
return coordinates.

## Consequence

The character stack now supports:

    motion graph

    deterministic spanning forest

    fundamental cycle basis

    state-by-basis-cycle incidence

    compact binary character field

    body search

    thalion search

This reduces redundant character width while preserving independent
cycle structure.

## Limitation

The basis depends on the selected spanning forest.

The current forest is made deterministic by relation-name ordering.

Different bases can describe the same cycle space with different
coordinates.

Directed relations are treated as distinct undirected edges during
basis construction.

The character records participation only.

It does not yet record signed cycle product, switching class, or a
basis-independent cycle-space functional.

## Keeper

The full cycle catalogue tells every way return can close.

The basis keeps only the independent receipts.
