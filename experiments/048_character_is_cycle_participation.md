# Experiment 048

## Title

Character Is Cycle Participation

## Status

Executable candidate.

## Question

Can TM-0 refine state character from mutual-return class identity to
participation in distinct directed cycles?

## Starting Result

Experiment 047 derived character from strongly connected return classes.

That construction is too coarse inside one strongly connected region.

States can belong to the same mutual-return class while participating in
different local cycles.

## Construction

The motion graph is searched for simple directed cycles.

Each cycle is normalized by cyclic rotation while preserving direction.

The canonical cycle order defines character coordinates.

Each state receives one binary coordinate per cycle:

    one if the state participates in that cycle

    zero otherwise

The result is a state-by-cycle participation character field.

## Result

Distinct simple directed cycles are enumerated.

Equivalent cyclic rotations normalize to the same cycle.

States participating in different cycle combinations receive different
characters.

States sharing the same cycle participation receive the same character.

A state outside all directed cycles receives the zero character.

An acyclic graph is rejected because no cycle-participation character
can be formed.

## Interpretation

Character can record more than membership in a mutual-return class.

It can encode the particular return structures available through a
state.

Two states may be mutually reachable while still carrying different
cycle-participation characters.

## Consequence

The character derivation chain is now:

    motion graph

    simple directed cycles

    canonical cycle coordinates

    state-by-cycle incidence

    derived binary character field

This reconnects the executable body pipeline with the earlier
cycle-space character work.

## Boundary

The current search enumerates all simple directed cycles, not an
independent cycle basis.

Character width may therefore be redundant and grow rapidly.

Cycle identity depends on relation names and normalized direction.

The zero character is currently allowed for states outside every cycle.

The construction records cycle participation, not signed cycle product,
switching class, or a linear cycle-space functional.

The exhaustive search is intended only for small graphs.

## Keeper

Return class says whether states can come back to one another.

Cycle participation says how return is locally carried.
