# Experiment 050

## Title

Character Is Intrinsic Cycle-Rank Loss

## Status

Executable candidate.

## Question

Can TM-0 derive a basis-independent state character from intrinsic
cycle-space structure rather than from one selected fundamental cycle
basis?

## Starting Result

Experiment 049 derived compact character coordinates from a
deterministic fundamental cycle basis.

Those coordinates still depended on the chosen spanning forest.

## Construction

For each state, the system computes:

    total graph cycle rank

    cycle rank after deleting the state

    cycle-rank loss

A state carries cycle structure when deleting it reduces the graph
cycle rank.

The binary character is encoded as a prefix of ones whose length equals
the cycle-rank loss, followed by zeros up to the total cycle rank.

For example, in a rank-two graph:

    loss zero becomes 00

    loss one becomes 10

    loss two becomes 11

## Result

State deletion removes the state and all incident motion rules.

Cycle-rank loss is derived without choosing a spanning forest
coordinate system.

States whose deletion destroys more independent cycle structure receive
stronger intrinsic characters.

States outside the cycle core receive the zero character.

Character width equals the total cycle rank.

The resulting field remains binary and compatible with the body and
thalion pipeline.

## Interpretation

Basis coordinates describe where a state appears in one chosen cycle
basis.

Cycle-rank loss records how much independent return structure depends
on that state.

The second quantity is intrinsic to the graph rather than to one
coordinate choice.

## Consequence

The character pipeline can now use:

    motion graph

    total cycle rank

    state-deletion cycle rank

    intrinsic cycle-rank loss

    basis-independent binary character

    body search

    thalion search

This provides a basis-independent alternative to fundamental-cycle
participation.

## Boundary

Cycle-rank loss is coarser than full cycle-space support.

Different states can have the same rank loss while participating in
different cycle structures.

The prefix encoding preserves rank-loss magnitude but not a unique
cycle identity.

Directed motion rules are still treated as distinct undirected edges
for cycle-rank calculation.

State deletion is a perturbation probe, not yet a native execution
process.

## Keeper

A basis says where a state appears.

Rank loss says how much return structure depends on it.
