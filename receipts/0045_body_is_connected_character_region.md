# Receipt 0045

## Title

A Body Is a Connected Character Region

## Status

Research receipt.

## Result

TM-0 can derive body candidates from:

    motion graph

    state character assignment

    connected region search

    nonempty boundary cut

A passing region must be:

    connected

    internally character-preserving

    separated from an outside by at least one cut relation

The resulting body candidate carries:

    normalized region states

    preserved character

    derived boundary

Mixed-character and disconnected regions are rejected.

The whole graph is rejected when it has no outside cut.

## Interpretation

A body candidate is not merely a named collection of states.

Connectivity gives the region coherence.

Shared character gives it identity.

The graph cut gives it an outside.

## Consequence

The body stack now supports:

    motion graph

    state character field

    connected candidate region

    preserved internal character

    derived graph boundary

    boundary-aware execution

The earlier body definition is now partly executable.

## Limitation

State characters remain supplied.

Singleton regions currently qualify as body candidates.

The definition does not yet require internal motion, return capacity, or
a nontrivial cycle.

These are body candidates, not yet thalions.

The exhaustive region search is intended only for small graphs.

## Keeper

Connectivity gives the body coherence.

Character gives it identity.

The cut gives it an outside.
