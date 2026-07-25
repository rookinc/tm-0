# Receipt 0048

## Title

Character Records Cycle Participation

## Status

Research receipt.

## Result

TM-0 can derive a binary state character field from participation in
simple directed cycles.

The motion graph supplies:

    directed relations

    simple directed cycles

    canonical cycle coordinates

Each state receives one coordinate per cycle.

A coordinate is:

    one when the state participates in that cycle

    zero otherwise

States with different cycle participation receive different
characters.

States outside all cycles receive the zero character.

## Interpretation

Mutual return class is only a coarse identity.

Cycle participation records how return is locally carried through each
state.

Two states can be mutually reachable while still participating in
different return structures.

## Consequence

The character pipeline now supports:

    motion graph

    directed cycle enumeration

    canonical cycle coordinates

    state-by-cycle incidence

    derived binary character field

This reconnects body and thalion derivation with explicit cycle
structure.

## Limitation

The construction uses all simple directed cycles rather than an
independent cycle basis.

The resulting character may be redundant and can grow rapidly.

Cycle identity depends on relation names and direction.

The character records participation only.

It does not yet record signed cycle product, switching class, or a
linear cycle-space functional.

The exhaustive search is intended only for small graphs.

## Keeper

Return class records where return is possible.

Cycle participation records how return passes through a state.
