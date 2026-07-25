# Receipt 0050

## Title

Character Records Cycle-Rank Dependence

## Status

Research receipt.

## Result

TM-0 can derive a basis-independent binary state character from
cycle-rank loss under state deletion.

For each state, the system computes:

    total graph cycle rank

    cycle rank after state deletion

    cycle-rank loss

A state whose deletion destroys independent cycle structure receives a
nonzero character.

A state outside the cycle core receives the zero character.

Character width equals the total graph cycle rank.

## Interpretation

Fundamental-cycle coordinates depend on a chosen basis.

Cycle-rank loss does not.

It records how much independent return structure depends on the state.

A state can therefore carry intrinsic cycle significance without being
described in one particular cycle basis.

## Consequence

The character stack now supports:

    motion graph

    intrinsic state perturbation

    cycle-rank loss

    basis-independent binary character

    body search

    thalion search

This gives TM-0 a coordinate-independent alternative to
basis-cycle participation.

## Limitation

Cycle-rank loss is coarser than full cycle-space support.

States with equal rank loss may participate in different return
structures.

The prefix encoding records magnitude rather than cycle identity.

Directed motion rules are treated as distinct undirected edges for
cycle-rank calculation.

State deletion is a structural probe, not an executed transition.

## Keeper

A basis records where a state appears.

Rank loss records how much return depends on it.
