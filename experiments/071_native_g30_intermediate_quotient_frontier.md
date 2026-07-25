# Experiment 071: Native G30 Intermediate Quotient Frontier

## Question

Is the native thirty-vertex signed G15 cover exactly the intermediate
quotient of G60 by the order-two kernel of the native V4 parity
character?

## Starting Result

The native G15 voltage is derived from native G60 transport.

For every G15 edge, the four G60 lifts carry one common V4 translation:

    delta = (delta_0, delta_1)

The native voltage is:

    native_bit = delta_0 xor delta_1

This defines the character:

    chi(x,y) = x xor y

Its kernel is:

    ker(chi) = {
        (0,0),
        (1,1)
    }

The signed double cover defined by this voltage is uniquely the native
Project 41 cover class.

## Candidate Intermediate Quotient

Each native G15 fiber contains four V4-coordinate states:

    (0,0)
    (0,1)
    (1,0)
    (1,1)

Quotienting by ker(chi) should form two pairs:

    {
        (0,0),
        (1,1)
    }

    {
        (0,1),
        (1,0)
    }

Across fifteen G15 fibers, this should produce:

    quotient vertices
        30

The expected quotient tower is:

    G60
        |
        | degree 2
        | kernel ker(chi)
        v
    G30_native
        |
        | degree 2
        | residual V4 / ker(chi)
        v
    G15

The composite quotient has:

    degree
        4

    deck group
        V4

## Bounded Requirement

TM-0 must:

1. retain the native sixty-state G60 edge source

2. retain the native V4 coordinate chart

3. construct the kernel action

4. derive its thirty two-state orbits

5. construct the quotient graph from native G60 edges

6. reject quotient loops

7. retain G60-edge to quotient-edge provenance

8. verify two G60 edges above every quotient edge

9. derive the residual two-state quotient to G15

10. verify that the composite quotient agrees with the native V4
    quotient

11. compare the thirty-state quotient with the certified native cover
    class

## Required Results

The expected intermediate quotient has:

    G60 vertices
        60

    G60 edges
        120

    kernel orbits
        30

    states per kernel orbit
        2

    quotient vertices
        30

    quotient edges
        60

    degree
        4

    components
        1

    triangles
        20

    isomorphic to native cover class
        true

    residual quotient vertices
        15

    residual quotient edges
        30

    residual quotient isomorphic to L(P)
        true

## Exact Distinctions

The native intermediate quotient is not:

    G60

    G15

    the all-one Project 42 carrier

    the alternative invariant cover

    the aligned source artifact

The aligned source is one representative of the voltage switching
class.

The intermediate quotient is a graph derived directly from native G60
and the kernel of its V4 character.

## Falsification

The frontier fails if:

    the character kernel does not form thirty two-state orbits

    a native G60 edge collapses to a loop

    the quotient has the wrong vertex or edge count

    the quotient is disconnected

    the quotient is not quartic

    the quotient is not the native cover class

    the residual quotient does not recover G15

    the quotient square does not commute

## Classification

This is a bounded intermediate-quotient frontier.

It is not yet an executable result.

It does not identify the historical archived G30 unless an independent
comparison is later performed.

## Boundary

The result will concern finite graph quotients and native deck
structure.

It will not identify the kernel involution with the external G900
half-flip.

It will not make a physical claim.

## Keeper Candidate

The sign is the character of a hidden quotient.

Its cover is the world between G60 and G15.
