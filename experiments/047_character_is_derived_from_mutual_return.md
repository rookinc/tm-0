# Experiment 047

## Title

Character Is Derived from Mutual Return

## Status

Executable candidate.

## Question

Can TM-0 derive the state character field from the directed return
structure of the motion graph rather than assign character values
externally?

## Starting Result

Experiment 046 derived thalion candidates from:

    motion graph

    state character field

    connected character-preserving body

    internal directed return

The state character field remained supplied.

## Construction

Two states belong to the same return class when:

    the first can reach the second

    the second can reach the first

These mutual-return classes are the strongly connected components of
the directed motion graph.

The system derives:

    directed adjacency

    reverse directed adjacency

    graph finishing order

    strongly connected return classes

Each return class receives a canonical one-hot character.

Every state in the same return class receives the same character.

Different return classes receive different characters.

## Result

Mutually returning states are grouped into one return class.

One-way reachable states remain in different return classes.

The derived return classes are canonical under state-name ordering.

Each class receives one one-hot character coordinate.

The resulting character field covers every registered state.

No external state-to-character assignment is required.

## Interpretation

Character can emerge from lawful return structure.

A state's character records which mutual-return class it inhabits.

States share character when each can leave its local position and still
return through the directed motion law.

## Consequence

The body and thalion derivation can now begin from:

    motion graph

and derive:

    mutual-return classes

    state character field

    connected character-preserving bodies

    internal return

    thalion candidates

This removes the largest prepared input from the current body selector.

## Boundary

The derived character identifies strongly connected components.

It is not yet a signed cycle character, switching class, or cycle-space
functional.

The one-hot coordinate assignment is canonical only relative to sorted
state names.

A strongly connected graph produces one shared one-bit character.

This scaffold derives return-class identity, not the richer character
structure developed in earlier cycle experiments.

## Keeper

States share character when the motion law lets them return to one
another.
