# Experiment 062: Selected-System Stabilizer Is Derived

## Question

Can TM-0 derive the actions that preserve one selected equivalence
system from a finite carrier-action group?

## Implementation

The executable scaffold is:

    src/tm0/finite_carrier_action_group.py

It defines:

    CarrierFamilyAction

    FiniteCarrierActionGroup

    compose_permutations

    inverse_permutation

    finite_carrier_action_group

The scaffold represents actions on:

    one fixed carrier domain

    one fixed equivalence-family domain

## Executable Result

A finite carrier-action group can now derive:

    composition

    identity

    inverse

    selected-system stabilizer

The stabilizer is obtained by filtering registered actions whose induced
family permutation fixes the selected system.

The stabilizer is not supplied as a scalar count.

It is derived from the action.

## Focused Example

The focused scaffold uses the six permutations of a three-element
carrier and family.

For selected system P0, the derived stabilizer contains:

    identity

    the involution swapping P1 and P2

For selected system P1, the derived stabilizer contains:

    identity

    the involution swapping P0 and P2

For selected system P2, the derived stabilizer contains:

    identity

    the involution swapping P0 and P1

Each nonidentity involution belongs to exactly one selected-system
stabilizer.

## Focused Evidence

The focused suite verifies:

    permutations compose

    inverse permutations are derived

    the group identity is derived

    composition returns a registered action

    inverse returns a registered action

    the stabilizer of P0 is derived

    the stabilizer of P1 is derived

    the stabilizer of P2 is derived

    each involution belongs to exactly one stabilizer

    invalid system indices are rejected

    a registered group must contain an identity

Focused result:

    11 tests passed

Full-suite result:

    427 tests passed

## Interpretation

Selection does more than identify one active equivalence system.

Selection also determines which registered symmetries remain internal
to that choice.

The full action describes all lawful movement among the family.

The stabilizer describes the actions that preserve the selected member.

## Earned Distinction

TM-0 now distinguishes:

    full carrier-action group

    induced action on the equivalence family

    selected equivalence system

    selected-system stabilizer

The stabilizer is relationally derived.

It is not an externally assigned authority set.

## G60 Correspondence

The scaffold has the correct derivational shape for the Project 42
targets:

    full automorphism order
        720

    partition-action kernel order
        120

    selected-system stabilizer order
        240

Those counts have not yet been recovered from the full certified
carrier-action set.

The current focused example proves the mechanism, not the final counts.

## What Has Not Been Earned

The implementation does not yet load:

    all 720 carrier automorphisms

    the order-120 kernel of the partition action

    the order-240 stabilizer of one certified quotient system

It does not yet verify closure of the full Project 42 carrier-action
set.

It does not yet construct the quotient graph.

## Classification

This is an executable stabilizer result.

It is stronger than a frontier scaffold.

It is not yet a full G60 automorphism correspondence.

## Ontology Status

The executable distinction among:

    selected equivalence

    full family action

    selected-system stabilizer

is now real.

No broader semantic object is admitted.

The current group and stabilizer names retain their ordinary
mathematical meanings.

## Boundary

A stabilizer is not treated as:

    witness

    context

    body

    character

    authority

The stabilizer records symmetry preservation.

It does not grant permission.

No physical interpretation is claimed.

## Keeper

Selection determines which symmetries remain internal to the choice.
