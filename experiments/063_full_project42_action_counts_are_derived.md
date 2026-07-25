# Experiment 063: Full Project 42 Action Counts Are Derived

## Question

Can TM-0 derive the full Project 42 carrier-action, quotient-family,
kernel, and selected-system stabilizer counts from the retained
certified action universe?

## Authoritative Source

The retained certificate is:

    sources/project42/
    project42_full_carrier_action_certificate_031.json

It was exported from the stable Project 41 graph source.

The target counts were not supplied as construction inputs.

## Implementation

The certificate loader is:

    src/tm0/project42_full_action_certificate.py

It defines:

    load_certificate

    load_project42_action_group

    partition_action_image

    partition_action_kernel

    selected_system_stabilizers

The generic finite-action machinery is:

    src/tm0/finite_carrier_action_group.py

## Executable Result

TM-0 loads:

    720 distinct carrier actions

on:

    one thirty-element carrier domain

with induced action on:

    one three-element quotient-system family

The following values are derived from the loaded action rows:

    full carrier-action count
        720

    quotient-family action image count
        6

    partition-action kernel count
        120

    selected-system stabilizer counts
        240
        240
        240

## Structural Relations

The partition-action kernel is contained in every selected-system
stabilizer.

Each selected-system stabilizer has index three in the full action
group:

    720 / 240 = 3

The quotient-family action image contains all six permutations of the
three systems.

## Focused Evidence

The focused suite verifies:

    the certificate passes

    the carrier domain has thirty vertices

    the family domain has three systems

    the full group has 720 actions

    the identity is derived

    the quotient-family action image has order six

    the partition-action kernel has order 120

    all three selected-system stabilizers have order 240

    the kernel is contained in every stabilizer

    every stabilizer has index three

    retained certificate counts match independently derived counts

Focused result:

    11 tests passed

Full-suite result:

    438 tests passed

## Correspondence

The Project 42 certified relations:

    |Aut(X)| = 720

    partition-action image order = 6

    partition-action kernel order = 120

    selected-system stabilizer order = 240

are now represented and re-derived inside TM-0 from the complete
retained carrier-action certificate.

This is no longer only a scalar correspondence.

The complete action rows are present.

## What Has Been Earned

TM-0 now has a source-backed executable account of:

    fixed carrier

    three lawful equivalence systems

    selected equivalence

    carrier action

    induced quotient-family action

    partition-action kernel

    selected-system stabilizer

The full finite action universe is retained.

## What Has Not Been Earned

TM-0 does not yet derive:

    Aut(X) is isomorphic to S5 x S3

    the kernel is isomorphic to S5

    the selected-system stabilizer is isomorphic to S5 x C2

    every quotient graph is isomorphic to L(P)

    quotient covering-edge compatibility

These remain separate mathematical correspondences.

## Classification

This is a full source-backed executable count correspondence.

It closes the action-count and stabilizer-count requirements of the
three-quotient frontier.

It does not yet close the quotient-graph correspondence.

## Ontology Status

No new broad semantic object is required.

The existing mathematical objects suffice:

    equivalence family

    selected equivalence

    group action

    kernel

    stabilizer

The three-quotient phenomenon has not forced:

    viewpoint

    observer

    contextual quotient

    retention

or any other broader permanent TM-0 object.

## Boundary

The certificate covers the natural three-system orbit.

It does not establish global completeness over every conceivable
quotient system.

Group order does not by itself prove abstract group isomorphism.

Stabilizer order does not by itself prove stabilizer structure.

No physical interpretation is claimed.

## Keeper

The same carrier admits three lawful identifications.

The full symmetry moves among them.

Selection exposes the stabilizer that remains.
