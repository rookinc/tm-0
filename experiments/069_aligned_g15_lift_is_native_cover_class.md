# Experiment 069: Aligned G15 Lift Is the Native Cover Class

## Question

Does the retained aligned G15 Z2 signing independently construct a
thirty-vertex signed double cover isomorphic to the Project 42
all-one carrier?

## Initial Result

No.

TM-0 independently constructed the signed double cover and compared it
with the Project 42 all-one carrier.

Both graphs have:

    vertices
        30

    edges
        60

    degree
        4

But they differ structurally:

    aligned G15 signed lift triangles
        20

    Project 42 all-one carrier triangles
        0

Therefore:

    aligned lift isomorphic to all-one
        false

This was a genuine falsification of the initial comparison target.

It was not a failure of the signed-double-cover constructor.

## Corrected Project 41 Context

Project 41 had already distinguished four S5-fixed G15 double-cover
classes:

    zero

    native

    alternative

    all_one

Their established profiles are:

    zero
        components
            15, 15
        triangles
            20
        automorphism order
            28800

    native
        components
            30
        triangles
            20
        automorphism order
            240

    alternative
        components
            30
        triangles
            0
        automorphism order
            240

    all_one
        components
            30
        triangles
            0
        automorphism order
            720

Project 41 also established that the all-one and native geometries are
distinct:

    all_one
        S5 / V4_even

    native central quotient
        S5 / V4_mixed

The initial comparison therefore tested the aligned lift against the
wrong member of the cover square.

## Generic Signed Double Cover

TM-0 now contains a dependency-free signed-double-cover constructor.

For each signed base edge joining u and v:

    PRESERVE
        connect (u,0) to (v,0)
        connect (u,1) to (v,1)

    INVERT
        connect (u,0) to (v,1)
        connect (u,1) to (v,0)

The constructor:

    creates two lift vertices per base vertex

    creates two lift edges per base edge

    retains base-edge and sign provenance

    distinguishes parallel and crossed lift edges

    rejects loops

    rejects incomplete sign assignments

    retains the canonical sheet-swap involution

The generic constructor passed:

    focused tests
        10

The full suite after its admission passed:

    tests
        521

## Aligned G15 Lift

Applied to the retained aligned G15 signing, TM-0 derives:

    base vertices
        15

    base edges
        30

    preserving base edges
        10

    inverting base edges
        20

    lift vertices
        30

    lift edges
        60

    degree profile
        4

    components
        1

    component size
        30

    sheet-swap orbits
        15

The canonical sheet swap preserves every lift edge.

The lift is therefore a genuine connected quartic two-sheet cover of
the aligned G15 support.

## Switching Compatibility

TM-0 applies a nontrivial local switching assignment on:

    vertices switched
        7

The switched signing produces a second signed double cover.

The original and switched covers are exactly isomorphic.

The explicit isomorphism has:

    mapped vertices
        30

Therefore the unsigned cover graph belongs to the switching class of
the signing, not to one local sign presentation.

The aligned lift layer passed:

    focused tests
        11

## Stable Cover-Square Certificate

Project 41 now exports a stable retained certificate:

    project42_invariant_cover_square_certificate_032

TM-0 retains it at:

    sources/project42/
    project42_invariant_cover_square_certificate_032.json

The certificate records:

    base graph
        G15

    cover classes
        4

    cover vertices per class
        30

    cover edges per class
        60

    triangle counts

    component sizes

    explicit cover edge sets

The certificate does not classify the aligned candidate.

It does not prove native cocycle origin.

## Exact Cover-Square Classification

TM-0 independently constructs the aligned lift and compares it by exact
graph isomorphism against all four certified cover classes.

Results:

    aligned lift isomorphic to zero
        false

    aligned lift isomorphic to native
        true

    aligned lift isomorphic to alternative
        false

    aligned lift isomorphic to all_one
        false

The native-class isomorphism returns an explicit bijection with:

    mapped vertices
        30

The set of matching classes is exactly:

    native

Therefore the aligned lift has unique membership in the native
Project 41 cover class.

The cover-square classification passed:

    focused tests
        8

The final full suite passed:

    tests
        540

## Exact Distinctions

The aligned signing has now earned:

    executable signed character

    switching-class invariance

    connected quartic double-cover construction

    unique native cover-class membership

It has not earned:

    strict source provenance

    a native G60 construction law for the cocycle bits

    uniqueness among every possible signing outside the certified
    invariant cover square

The statement:

    aligned lift belongs to native cover class

is not the same as:

    aligned cocycle was natively derived from G60

Cover-class identity is structural.

Cocycle origin is generative.

## Semantic Admission Result

No new broad semantic object was required.

The result uses:

    signed graph

    local sign

    switching class

    double cover

    sheet label

    deck involution

    graph isomorphism

    cover class

    provenance boundary

## Classification

This is an executable signed-cover classification result.

Experiment 068 is closed with a corrected target.

The initial all-one identification was falsified.

The aligned G15 signed lift is uniquely identified with the native
Project 41 cover class.

## Boundary

The aligned source remains:

    imported_from_aletheos_aligned_cocycle

Its provenance classification remains:

    aligned_imported_representative_native_origin_open

This result does not repair the missing strict cocycle writer.

It does not prove that the archived G30 is the native cover.

It does not identify the native cover with G60.

It does not identify the sheet swap with the external G900 half-flip.

It does not alter the Project 42 all-one theorem.

The all-one and native degree-30 geometries remain distinct.

No physical interpretation is claimed.

## Keeper

The sign determines how the sheets meet.

The native cover is the world this signing creates.

Its origin must still be earned.
