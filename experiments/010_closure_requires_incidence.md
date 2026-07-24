# Experiment 010

## Title

Closure Requires Incidence Beyond Local Directed Role

## Status

Executable candidate.

## Question

Can an anonymous local incoming/outgoing profile determine whether a
directed relation belongs to a closed return path?

## Starting Result

Experiment 009 earned directed relational polarity:

    incoming
    outgoing

It did not establish composition or closure.

## Construction

The experiment compares two rooted directed fixtures.

Open path:

    a -> r -> b -> c

Closed cycle:

    a -> r -> b -> a

At root r, both structures have:

    one incoming relation

    one outgoing relation

All participating carriers use the same anonymous null continuity
trace.

## Projection

The local TM-0 projection retains only:

    center trace

    incoming neighbor traces

    outgoing neighbor traces

It forgets endpoint incidence beyond the immediate neighborhood.

## Expected Result

The open path and closed cycle should have identical local directed
profiles.

Only the incidence structure should reveal that the closed fixture
contains a positive-length directed return to the root.

## Interpretation

Direction earns source and target roles.

Direction alone does not earn closure.

Closure requires enough incidence information to compose directed
relations into a path and determine whether that path returns.

## Apparatus Boundary

String handles are used only by the finite test apparatus to construct
and inspect edge incidence.

They are not included in the anonymous local projection.

They are not promoted as names, identities, coordinates, or TM-0
primitives.

## Boundary

This experiment does not derive incidence from more primitive
mechanics.

It does not prove that closure requires persistent intrinsic identity.

It does not yet derive return registration, character, witness,
geometry, or a thalion.
