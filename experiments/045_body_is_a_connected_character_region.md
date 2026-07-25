# Experiment 045

## Title

A Body Is a Connected Character Region

## Status

Executable candidate.

## Question

Can TM-0 derive body candidates from graph connectivity, preserved
character, and a nonempty boundary cut?

## Starting Result

Experiment 044 derived a boundary from a selected connected region.

The region itself was still selected externally.

Earlier experiments defined a body as a connected
boundary-preserving character region.

## Construction

A motion graph contains:

    registered states

    directed motion rules

Each state carries a binary character value.

A body candidate must be:

    nonempty

    connected

    internally character-preserving

    bounded by at least one graph cut

Internal character preservation requires all states in the region to
carry the same character.

The system enumerates connected state subsets and derives a boundary
for each passing region.

## Result

Connected same-character regions become body candidates.

Mixed-character regions are rejected.

Disconnected regions are rejected.

The full graph is rejected when it has no nonempty boundary cut.

The body candidate carries:

    normalized region states

    preserved character

    derived region boundary

Enumeration recovers all passing regions.

Minimal passing candidates are single states in the current graph.

## Interpretation

The body definition is now partly executable.

A body candidate is not merely a named set of states.

It is a connected region whose internal membership preserves one
character and whose graph cut distinguishes it from an outside.

## Consequence

The body-construction chain is now:

    motion graph

    state character field

    connected region search

    internal character-preservation test

    nonempty boundary-cut test

    derived body candidate

    derived boundary

    boundary-aware execution

## Boundary

The character assignment to states remains supplied.

The current definition admits singleton body candidates.

It does not yet require internal motion, return capacity, or more than
one state.

It therefore derives body candidates, not yet thalions.

The search is exhaustive over state subsets and is intended only for
small graphs.

Character preservation is tested by equality of state character values,
not by a transition-induced character law.

## Keeper

Connectivity gives the region coherence.

Character gives it identity.

The cut gives it an outside.
