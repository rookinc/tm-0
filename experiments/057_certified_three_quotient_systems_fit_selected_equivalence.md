# Experiment 057: Certified Three Quotient Systems Fit Selected Equivalence

## Question

Can the certified three quotient systems from Project 42 be represented
by the selected-equivalence scaffold without mutating the carrier or
erasing the alternative systems?

## Authoritative Source

The source certificate is:

    Project 41
    project42_quotient_frame_orbit_certificate_004.json

The certificate records:

    one 30-vertex carrier

    three partitions P0, P1, and P2

    fifteen unordered pairs in each partition

    pairwise-disjoint pair sets

    forty-five distinct pairs in their union

    an S3 action on the three partitions

    one order-two element fixing each partition

The current TM-0 fixture copies the three explicit pair lists from the
certificate.

It does not regenerate them from descriptive prose.

## Implementation

The source-backed fixture is:

    src/tm0/g60_three_quotient_systems.py

It supplies:

    G60_QUOTIENT_CARRIER

    G60_QUOTIENT_SYSTEMS

    P0_BLOCKS

    P1_BLOCKS

    P2_BLOCKS

    select_g60_quotient_system

## Executable Result

The selected-equivalence scaffold accepts all three certified systems.

For each selection:

    the carrier contains the same thirty vertices

    the active partition contains fifteen pairs

    the other two systems remain registered

    the active partition differs from the alternatives

All three systems have the same block-size profile:

    fifteen classes of size two

The matching profile does not erase which system is selected.

## Focused Evidence

The focused suite verifies:

    the carrier has thirty distinct vertices

    exactly three systems are registered

    each system contains fifteen pairs

    each system partitions the same carrier

    the pair sets are pairwise disjoint

    their union contains forty-five pairs

    each system can be selected

    each selection preserves two alternatives

    all selections preserve the same carrier

    matching pair-size profiles do not erase selection

Focused result:

    10 tests passed

Full-suite result:

    395 tests passed

## Correspondence

The Project 42 mathematical structure:

    fixed 30-vertex graph
    +
    three lawful fifteen-pair partitions
    +
    selected quotient frame

fits the TM-0 candidate structure:

    fixed carrier
    +
    preserved equivalence family
    +
    selected equivalence

This correspondence is exact at the partition-selection level.

## What Has Been Earned

The selected-equivalence candidate is no longer supported only by a
synthetic four-element example.

It now hosts the certified three-system quotient-frame data that exposed
the original semantic gap.

## What Has Not Been Earned

The current fixture does not yet represent:

    the S3 action on the three systems

    the order-two element fixing each selected system

    the full automorphism group

    the selected-system stabilizer

    the quotient graph L(P)

    covering-edge certification

Those remain independent extensions.

## Classification

This is a source-backed executable correspondence.

It is stronger than a generic candidate result.

It does not yet complete the three-quotient frontier.

## Ontology Status

The executable distinction is now G60-backed:

    lawful equivalence family

    selected equivalence

The final ontology name remains open until the symmetry and stabilizer
requirements are tested.

## Boundary

The certificate establishes the natural three-partition orbit.

It does not claim global completeness over every conceivable quotient
system.

The fixture does not claim that the thirty-vertex carrier is G60 itself.

The fixture does not claim that quotient selection is:

    context

    viewpoint

    observation

    witness

    character

The underlying carrier remains unchanged by selection.

## Keeper

The same carrier supports three lawful identifications.

Selection chooses one without erasing the other two.
