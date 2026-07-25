# Experiment 059: Equivalence Family Action Preserves Carrier

## Question

Can TM-0 represent the certified action on the three quotient systems
while preserving the fixed carrier and the complete registered family?

## Implementation

The executable scaffold is:

    src/tm0/equivalence_family_action.py

It defines:

    EquivalenceFamilyAction

    act_on_selection

The source-backed quotient family is:

    src/tm0/g60_three_quotient_systems.py

## Executable Result

TM-0 now represents a permutation acting on the registered equivalence
systems:

    P0
    P1
    P2

The six certified permutations are accepted:

    [0, 1, 2]
    [0, 2, 1]
    [1, 0, 2]
    [1, 2, 0]
    [2, 0, 1]
    [2, 1, 0]

Their image contains six distinct actions.

The action is transitive on the three systems.

Each certified involution:

    fixes one system

    swaps the other two systems

Applying an action may move the selected system.

It preserves:

    the thirty-element carrier

    the three registered systems

    the unselected alternatives

## Focused Evidence

The focused suite verifies:

    all six certified actions are valid

    all six actions are distinct

    the action image has order six

    the action is transitive

    each involution fixes one system

    each involution swaps the other two systems

    an action can move the selected system

    the carrier remains fixed

    the registered family remains fixed

    the identity preserves the selected system

    invalid permutations are rejected

    the action domain must match the registered family

Focused result:

    12 tests passed

Full-suite result:

    407 tests passed

## Interpretation

The registered equivalence systems are not merely stored alternatives.

They form a family related by lawful action.

Selection identifies the active equivalence system.

Symmetry can move that selection to another lawful system without
changing the carrier or deleting alternatives.

## What Has Been Earned

TM-0 can now distinguish:

    preserved lawful family

from:

    active selected member

and:

    lawful action on the family

The candidate structure now contains:

    fixed carrier

    equivalence-system family

    selected system

    family action

## What Has Not Been Earned

The current action operates only on system names.

It does not yet represent:

    the certified permutation on the thirty carrier vertices

    compatibility between carrier action and partition action

    the full automorphism group

    the kernel of the partition action

    the selected-system stabilizer as a subgroup object

    quotient graph construction

## G60 Correspondence

At the quotient-family level, the certified image:

    S3

is represented exactly by the six family permutations.

The action preserves the same three certified pair partitions and moves
among them transitively.

The carrier-level action remains to be joined.

## Classification

This is a source-backed executable symmetry result.

It is not yet a complete automorphism correspondence.

It does not yet close the three-quotient frontier.

## Ontology Status

The executable distinction now includes:

    selected equivalence

    equivalence-family action

The final permanent ontology name remains open.

The current implementation names are candidate names.

## Boundary

No claim is made that a family action is physical motion.

No claim is made that changing selection changes the underlying body.

No claim is made that symmetry action is:

    context

    witness

    observation

    character

No global completeness claim is made beyond the certified natural
three-system orbit.

## Keeper

Selection chooses one lawful identification.

Symmetry moves the choice without moving the carrier.
