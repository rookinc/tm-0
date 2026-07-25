# Experiment 051

## Title

Character Is Refined Intrinsic Damage

## Status

Executable candidate.

## Question

Can TM-0 refine basis-independent cycle-rank character with additional
state-deletion damage information?

## Starting Result

Experiment 050 derived intrinsic character from cycle-rank loss under
state deletion.

That measure is basis-independent but coarse.

Two states can cause equal cycle-rank loss while damaging the graph in
different ways.

## Construction

For each state, the system deletes that state and all incident motion
rules.

It then derives:

    cycle-rank loss

    increase in undirected component count

    surviving directed return-class count

    largest surviving return-class size

Each scalar is encoded as a fixed-width unary binary block.

The blocks are concatenated into one binary character.

All states receive characters of equal width.

## Result

Cycle-core states, partial-cycle states, and states outside the cycle
core receive distinct perturbation profiles.

Bridge-like states can increase the number of surviving components.

Leaf deletion need not increase component count or reduce cycle rank.

The surviving return-class profile records how directed return structure
remains after deletion.

The refined field is binary and has equal width across all states.

States with similar cycle-rank loss can still be separated by other
damage fields.

## Interpretation

Intrinsic character can record more than how much cycle rank disappears.

It can also record how the remaining graph fragments and how much
mutual-return structure survives.

Character becomes a compact receipt of structural dependence under
controlled perturbation.

## Consequence

The intrinsic character pipeline is now:

    motion graph

    state deletion

    cycle-rank loss

    component damage

    surviving return-class profile

    fixed-width binary encoding

    refined intrinsic character

    body search

    thalion search

This preserves basis independence while increasing local resolution.

## Boundary

The character remains a perturbation signature rather than a native
execution trace.

The unary encoding is convenient but not uniquely required.

The chosen fields do not form a complete graph invariant.

Different states can still share the same refined signature.

Directed motion rules are treated as undirected edges for cycle-rank and
component calculations.

Return classes are computed from the surviving directed graph.

## Keeper

Rank loss says how much return disappears.

The damage profile says what kind of world remains.
