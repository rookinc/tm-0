# Experiment 070: Native G15 Cocycle Authentication Frontier

## Question

Can TM-0 authenticate the retained aligned G15 cocycle artifact as a
representative of the native G60-derived switching class while leaving
its original writer history unresolved?

## Starting Results

Experiment 067 established that the retained artifact is executable:

    source support
        G15

    directed records
        60

    undirected signed edges
        30

    switching character
        stable

Experiment 069 established that its signed double cover belongs
uniquely to the native Project 41 cover class.

The native cover match is not shared by:

    zero

    alternative

    all_one

The latest native-voltage comparison established:

    native G60 states
        60

    native G60 edges
        120

    native G15 quotient edges
        30

    G60 lifts per G15 edge
        4

    native voltage law
        native_bit =
        delta_coordinate_0 xor delta_coordinate_1

The retained aligned signing matches this independently derived native
voltage after:

    one G15 graph relabeling

    one local switching assignment

    switched vertices
        11

Therefore the retained signing and the native G60-derived signing
belong to the same switching class.

## Authentication Claim

The bounded authentication claim is:

    the retained aligned artifact is an authenticated representative
    of the native G60-derived G15 switching class

This claim concerns mathematical content.

It does not claim:

    original authorship

    exact historical writer

    exact historical generation script

    exact historical labeling path

    exact historical switching gauge

## Required Authentication Receipt

The authentication receipt must retain:

    aligned source artifact identity

    aligned source status

    aligned source hash

    native derivation certificate identity

    native derivation certificate hash

    native voltage law

    graph relabeling

    local switch assignment

    switch count

    edgewise verification count

    edgewise mismatch count after transport and switching

    native cover-class match

    exact boundary between mathematical authentication and historical
    provenance

## Edgewise Verification

For every aligned edge joining u and v, the receipt must verify:

    aligned_bit(u,v)
    xor switch(u)
    xor switch(v)

equals:

    native_bit(phi(u),phi(v))

where:

    phi
        is the authenticated G15 relabeling

    switch
        is the authenticated local gauge assignment

Required result:

    tested edges
        30

    matching edges
        30

    mismatching edges
        0

## Tamper Sensitivity

Authentication must fail if any retained cocycle bit is changed without
a compensating lawful relabeling and switching transformation.

A focused tamper test must:

    flip one aligned edge bit

    rerun the authenticated mapping and switch assignment

    detect at least one edgewise mismatch

This does not need to prove resistance to every possible forgery.

It proves that the receipt is checking signed content rather than only
file names or unsigned support.

## Exact Distinctions

Authentication is not:

    discovery

    authorship

    ownership

    historical reconstruction

    native writer recovery

    source-file sanctification

Authentication is:

    independent native derivation

    explicit mathematical correspondence

    complete edgewise verification

    retained evidence hashes

    explicit claim boundary

## Semantic Admission Result

No new broad semantic object is required.

The authentication uses:

    source artifact

    native derivation

    graph isomorphism

    switching gauge

    edgewise verification

    evidence hash

    receipt

The receipt records why the claim is trusted.

It does not create the mathematical identity it certifies.

## Falsification

Authentication fails if:

    the native derivation certificate does not pass

    the retained source cannot be loaded

    no graph relabeling exists

    no switching assignment exists

    any transported edge bit disagrees

    the aligned lift does not belong uniquely to the native cover class

    a one-bit tamper is not detected by the fixed authentication witness

## Classification

This is a bounded artifact-authentication frontier.

It is not yet an authentication receipt.

The mathematical identity is established.

The remaining task is to package the evidence into a stable,
tamper-sensitive receipt.

## Boundary

Historical writer identity remains open.

The authentication receipt will not claim that the retained aligned
artifact was originally generated from the native G60 law.

It will certify that the artifact's signed mathematical content is
equivalent to that law.

No physical interpretation is claimed.

## Keeper Candidate

Function proves that it works.

Authentication proves what it is.
