# Experiment 068: Aligned G15 Signed Double Cover Frontier

## Question

Does the retained aligned G15 Z2 signing independently construct a
thirty-vertex signed double cover isomorphic to the Project 42 carrier?

## Starting Results

Experiment 065 established the Project 42 carrier as:

    vertices
        30

    edges
        60

    degree
        4

    quotient systems
        3

Each quotient system produces a graph isomorphic to L(P).

Experiment 067 established the aligned G15 signing as:

    base vertices
        15

    base edges
        30

    preserving edges
        10

    inverting edges
        20

    cycle rank
        16

    switching character
        executable and invariant

Its native G60 origin remains open.

## Candidate Lift Rule

For each signed base edge joining u and v:

    PRESERVE
        connect (u,0) to (v,0)
        connect (u,1) to (v,1)

    INVERT
        connect (u,0) to (v,1)
        connect (u,1) to (v,0)

This rule must be implemented independently inside TM-0.

The retained phase2b lift artifact may be used only as later
certification evidence.

It must not be used as the construction input.

## Bounded Requirement

A minimal signed-double-cover constructor must:

1. accept one finite signed simple graph

2. create two lift vertices for each base vertex

3. create two lift edges for each base edge

4. use parallel lift edges for PRESERVE

5. use crossed lift edges for INVERT

6. reject loops and incomplete sign assignments

7. record the base edge and sign behind every lift edge

8. retain the canonical sheet-swap involution

9. verify that sheet swap preserves the lift graph

10. verify that the sheet-swap orbits recover the base graph

## Source-Backed Application

Applied to the aligned G15 candidate, TM-0 must derive:

    lift vertices
        30

    lift edges
        60

    degree
        4

    components
        1

    parallel base edges
        10

    crossed base edges
        20

    sheet-swap orbits
        15

    quotient by sheet swap
        G15 support

## Project 42 Comparison

The independently constructed lift must then be compared with the
retained Project 42 carrier.

Required result:

    aligned G15 signed lift isomorphic to Project 42 carrier

The comparison must return an explicit thirty-vertex bijection.

Exact graph isomorphism does not by itself identify the signing as
native.

## Switching Compatibility

A switched representative of the same G15 signing must produce an
isomorphic double cover.

The expected lift isomorphism is induced by changing sheet labels at
the switched base vertices.

Therefore TM-0 must verify:

    local switching changes the edge-sign presentation

    local switching preserves the switching character

    the switched signing produces an isomorphic lift

## Exact Distinctions

The signed double cover is not:

    the unsigned G15 base graph

    the cocycle edge table

    the Project 42 quotient partition

    the external G900 half-flip

    G60

The sheet-swap involution is an automorphism of the signed double cover.

It is not thereby the external G900 half-flip.

The constructed cover may be isomorphic to the Project 42 carrier
without the source signing being natively derived.

## Falsification

The frontier fails if:

    the lift has the wrong vertex count

    the lift has the wrong edge count

    the lift is not quartic

    the lift is disconnected

    sheet swap is not a graph automorphism

    quotienting by sheet swap does not recover the base support

    the lift is not isomorphic to the Project 42 carrier

    switching-equivalent signings produce nonisomorphic lifts

## Semantic Admission Result

No new broad semantic object is currently required.

The candidate requires only:

    signed graph

    double cover

    sheet label

    deck involution

    quotient

    graph isomorphism

    provenance boundary

## Classification

This is a bounded signed-double-cover frontier.

It is not yet an executable result.

It does not establish native G60 cocycle origin.

It does not establish that the Project 42 carrier is G60.

## Boundary

The aligned cocycle remains an imported representative.

The lift may certify a structural bridge from the candidate signing to
the Project 42 carrier.

That structural bridge does not repair the missing strict source
writer.

The historical G30 naming remains outside this frontier.

No physical interpretation is claimed.

## Keeper Candidate

The sign determines how the sheets meet.

The cover records the world that meeting creates.
