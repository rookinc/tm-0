# Receipt 0062: Selected-System Stabilizer Is Derived

## Recorded Result

TM-0 can now derive the actions that preserve one selected equivalence
system from a finite carrier-action group.

The stabilizer is obtained by filtering registered actions whose induced
family permutation fixes the selected system.

It is not supplied as a scalar count.

## Executable Evidence

Implementation:

    src/tm0/finite_carrier_action_group.py

Focused tests:

    tests/test_finite_carrier_action_group.py

Focused result:

    11 tests passed

Full-suite result:

    427 tests passed

## Earned Structure

The executable scaffold derives:

    composition

    identity

    inverse

    induced family action

    selected-system stabilizer

For a three-system family:

    the stabilizer of P0 contains identity and the involution swapping
    P1 with P2

    the stabilizer of P1 contains identity and the involution swapping
    P0 with P2

    the stabilizer of P2 contains identity and the involution swapping
    P0 with P1

Each nonidentity involution belongs to exactly one selected-system
stabilizer.

## Earned Distinction

TM-0 now distinguishes:

    full carrier-action group

    action on the equivalence family

    selected equivalence system

    symmetries preserving the selected system

Selection therefore determines which registered symmetries remain
internal to the active identification law.

## G60 Relevance

The derivation has the correct shape for the Project 42 targets:

    full automorphism order
        720

    partition-action kernel order
        120

    selected-system stabilizer order
        240

Those counts have not yet been recovered from the complete certified
carrier-action set.

They remain correspondence targets.

## Classification

This is an executable stabilizer receipt.

It is stronger than a scaffold receipt.

It is not yet a complete G60 automorphism correspondence.

## Boundary

The current implementation does not load:

    all 720 carrier automorphisms

    the order-120 kernel of the partition action

    the order-240 selected-system stabilizer

It does not verify closure of the complete Project 42 action set.

It does not construct the quotient graph.

A stabilizer is not treated as:

    authority

    permission

    witness

    context

    body

    character

The stabilizer records symmetry preservation only.

No physical interpretation is claimed.

## Keeper

Selection determines which symmetries remain internal to the choice.
