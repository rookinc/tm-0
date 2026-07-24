# Experiment 011

## Title

Anonymous Endpoint Incidence

## Status

Executable candidate.

## Question

Does closure require named carriers, or can it be represented using
only relation-local endpoint positions and endpoint equivalence?

## Starting Result

Experiment 010 showed that local incoming and outgoing roles do not
determine closure.

A global incidence structure was required behind the projection.

## Construction

Each directed relation has two local endpoint positions:

    source

    target

For relation i, these are represented as:

    (i, source)

    (i, target)

The index identifies the relation occurrence inside the finite test
apparatus.

It does not name a carrier or vertex.

## Incidence

Two endpoint positions compose when they belong to the same
equivalence class.

For three relations:

    target(0) = source(1)

    target(1) = source(2)

produces an open composable chain.

Adding:

    target(2) = source(0)

produces closure.

## Expected Result

The open and closed constructions should differ by exactly one
endpoint-equivalence registration.

No named carrier is required.

## Interpretation

Closure does not require intrinsic carrier identity in the tested
model.

It requires a chain of incidence equalities among relation-local
ports.

This earns junction or endpoint equivalence as a candidate mechanism.

## Apparatus Boundary

Relation indices are local construction handles used to distinguish
relation occurrences.

They do not claim persistent carrier identity.

The experiment does not yet derive occurrence indexing from TM-0.

## Boundary

This experiment does not derive endpoint equivalence from a more
primitive operation.

It does not derive return registration, character, witness, geometry,
time, or a thalion.

It establishes only that named carriers are unnecessary for the
tested closure construction.
