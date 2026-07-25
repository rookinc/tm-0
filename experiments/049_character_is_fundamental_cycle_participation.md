# Experiment 049

## Title

Character Is Fundamental Cycle Participation

## Status

Executable candidate.

## Question

Can TM-0 replace the full simple-cycle catalogue with a compact
independent cycle basis for state character?

## Starting Result

Experiment 048 derived character from participation in all simple
directed cycles.

That construction can be redundant and grow rapidly.

## Construction

The directed motion rules are treated as distinct undirected edges for
cycle-space construction.

A deterministic spanning forest is built from relation-name order.

Each non-tree relation closes one fundamental cycle with the unique
tree path between its endpoints.

The resulting fundamental cycles define independent cycle coordinates.

Each state receives one binary coordinate per basis cycle:

    one when the state participates in that basis cycle

    zero otherwise

## Result

The spanning forest is deterministic.

The number of non-tree relations equals the undirected cycle rank.

Each non-tree relation generates one fundamental cycle.

The character width equals the cycle rank.

States with different basis-cycle participation receive different
characters.

States outside every basis cycle receive the zero character.

A graph with zero cycle rank is rejected.

## Interpretation

A compact return address does not require every possible cycle.

A fundamental cycle basis preserves independent cycle-space structure
without carrying the full redundant cycle catalogue.

The state character now records participation in independent return
coordinates.

## Consequence

The character pipeline is now:

    motion graph

    deterministic spanning forest

    non-tree relations

    fundamental cycle basis

    state-by-basis-cycle incidence

    compact binary character field

This gives the body and thalion search a smaller structural address
space.

## Boundary

Directed motion rules are treated as distinct undirected edges during
basis construction.

The chosen basis depends on deterministic relation-name ordering.

Different spanning forests can produce different basis coordinates
while representing the same cycle space.

The character records state participation in basis cycles.

It does not yet record signed cycle product, switching class, or a
basis-independent cycle-space functional.

## Keeper

All cycles describe return.

A basis records only the independent ways return can close.
