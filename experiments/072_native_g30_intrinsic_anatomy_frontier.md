# Experiment 072: Native G30 Intrinsic Anatomy Frontier

## Question

What is the intrinsic group-theoretic and local combinatorial anatomy of

    G30_native
        =
    G30_historical
        =
    G60 / ker(chi)

where:

    chi(x,y) = x xor y

and:

    ker(chi) = {
        (0,0),
        (1,1)
    }?

## Starting Result

TM-0 has established the exact quotient tower:

    G60
        |
        | quotient by ker(chi), degree 2
        v
    G30_native
        |
        | residual C2 quotient, degree 2
        v
    G15 = L(Petersen)

The historical antipode classes and the parity-kernel classes are the
same thirty pairs of G60 states.

The native G30 graph has:

    vertices
        30

    edges
        60

    degree
        4

    components
        1

    triangles
        20

    automorphism order
        240

It is the native member of the Project 41 invariant cover square.

It is not:

    zero

    alternative

    all_one

## Primary Target

Derive the full automorphism group from the native G30 graph itself.

Required results:

    automorphism count
        240

    vertex transitive
        true

    vertex stabilizer order
        8

    center order

    derived subgroup order

    element-order profile

    candidate abstract group structure

The group structure must be supported by executable invariants.

It must not be assigned from order alone.

## Homogeneous-Space Target

Project 41 identifies the native central quotient with the mixed-V4
geometry:

    S5 / V4_mixed

TM-0 must recover this intrinsically from the G30 action.

Required checks:

    a transitive subgroup of order 120 exists

    its vertex stabilizer has order 4

    the stabilizer is a Klein four group

    the stabilizer lies in the mixed-V4 conjugacy class

    the thirty vertices form one coset action

    the residual central C2 accounts for the full order-240 extension

The target description is:

    V(G30_native) ~= S5 / V4_mixed

This must be derived from the action, not merely copied from a source
label.

## Triangle Anatomy Target

The native G30 graph contains exactly:

    triangles
        20

TM-0 must determine:

    triangles through each vertex

    triangles through each edge

    triangle orbit count under the full automorphism group

    whether the twenty triangles form one orbit

    how each triangle lifts back to G60

    whether each G30 triangle corresponds to one native G60 triangle
    pair, orbit, or quotient class

No geometric interpretation should be assumed before the incidence
counts are derived.

## Comparison Target

The native and alternative cover classes both have automorphism order:

    240

but differ in triangle count:

    native
        20

    alternative
        0

TM-0 should identify the first intrinsic invariant that distinguishes
their group actions or local stabilizer actions beyond ordinary
triangle count.

Possible candidates include:

    vertex-stabilizer action on four neighbors

    edge-orbit structure

    triangle incidence

    quotient-fiber action

    central involution position

## Bounded Work Order

The frontier should proceed in this order:

1. enumerate or retain the full native G30 automorphism group

2. verify order 240 and transitivity

3. derive stabilizer order and element-order profile

4. identify the order-120 subgroup acting as S5

5. derive the mixed-V4 stabilizer

6. classify the central C2 extension

7. derive the twenty-triangle incidence structure

8. compare native and alternative local actions

## Exact Distinctions

The intrinsic anatomy is not:

    the historical naming of G30

    the quotient construction alone

    the aligned cocycle artifact

    the all-one S5 x S3 action

The native G30 action is a property of the derived thirty-state graph.

Its group description must be earned from that action.

## Falsification

The proposed anatomy fails if:

    the full automorphism count is not 240

    the graph is not vertex transitive

    no order-120 transitive subgroup exists

    the vertex stabilizer is not V4

    the action does not realize S5 / V4_mixed

    the central extension structure does not close

    the twenty triangles do not admit the claimed orbit structure

## Semantic Admission Result

No new broad semantic object is currently required.

The frontier uses:

    finite graph

    automorphism group

    subgroup

    stabilizer

    orbit

    homogeneous space

    local incidence

    quotient provenance

## Classification

This is a bounded intrinsic-anatomy frontier.

It is not yet an executable result.

It does not make a physical claim.

## Boundary

The mixed-V4 label must be recovered from group action and conjugacy
data.

The abstract group structure must not be inferred from order alone.

The triangle layer must remain finite combinatorial incidence until a
later bridge earns a broader interpretation.

## Keeper Candidate

The quotient tells us which states became one.

The automorphism group tells us what the resulting world can no longer
distinguish.
