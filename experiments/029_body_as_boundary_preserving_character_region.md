# Experiment 029

## Title

Body as a Boundary-Preserving Character Region

## Status

Executable candidate.

## Question

Can a body be represented as the maximal connected region of character
states reachable through boundary-preserving realizations?

## Starting Result

Experiment 028 established that character may change while boundary
remains stable.

This suggested that a body may be more than one frozen character state.

## Construction

A finite transition system contains:

    character states

    transitions between states

    a boundary signature for each state

Transitions are retained when the boundary signature is unchanged.

The body region of a seed state is the connected component reachable
through those boundary-preserving transitions.

## Result

States connected through boundary-preserving transitions belong to one
body region.

A state reached only through boundary change lies outside that region.

A seed in a different boundary class defines a different region.

## Interpretation

A body can be represented as a family of changing character states
held together by one persistent boundary.

The body is not one state.

The body is the connected region of lawful internal variation that
preserves the same inside/outside distinction.

## Consequence

This gives a first executable candidate definition:

    body
        =
    connected boundary-preserving character region

Character may evolve internally without destroying body continuity.

Boundary change moves the system outside the current body region.

## Boundary

The experiment operates on a supplied finite transition system.

It does not yet derive maximality over the full possibility address
space.

It does not classify boundary change as growth, division, merger,
repair, decay, or failure.

It does not derive the thalion.

## Keeper

A body is not one character state.

A body is the region in which character may change without losing its
boundary.
