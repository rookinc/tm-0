# Receipt 0051

## Title

Character Records Intrinsic Damage

## Status

Research receipt.

## Result

TM-0 can derive a refined basis-independent character from controlled
state deletion.

For each state, the system records:

    cycle-rank loss

    component gain

    surviving return-class count

    largest surviving return-class size

These values are encoded as equal-width binary characters across the
graph.

States that cause similar cycle-rank loss can still be distinguished by
how the remaining graph fragments and how much directed return survives.

## Interpretation

A state can matter in more than one structural way.

It can support independent cycles.

It can hold components together.

It can preserve or destroy large mutual-return regions.

The refined character records the kind of damage caused by removing the
state.

## Consequence

The intrinsic character stack now supports:

    motion graph

    controlled state deletion

    cycle-rank damage

    component damage

    surviving return structure

    fixed-width binary character

    body search

    thalion search

This increases structural resolution without choosing a cycle basis.

## Limitation

The character remains a perturbation signature rather than a native
execution trace.

The unary encoding is convenient but not uniquely required.

The selected damage fields do not form a complete graph invariant.

Different states may still share the same refined signature.

Directed rules are treated as undirected edges for rank and component
calculations.

## Keeper

Rank loss says how much return disappears.

The damage profile says what kind of structure survives.
