# Experiment 061: Selected-System Stabilizer Frontier

## Question

What additional executable structure is required to distinguish:

    the full symmetry acting on the quotient-system family

from:

    the symmetry preserving one selected quotient system?

## Authoritative Source

The Project 42 certificate records:

    full automorphism order
        720

    partition-action image order
        6

    partition-action kernel order
        120

    selected-system stabilizer order
        240

For each selected quotient system, one certified involution fixes that
system and swaps the other two.

## Current TM-0 Capability

TM-0 currently represents:

    one fixed carrier

    three lawful equivalence systems

    one selected system

    the six family permutations

    three certified carrier involutions

    compatibility between carrier action and family action

TM-0 does not yet represent a group of carrier actions or derive a
stabilizer from that group.

## Bounded Requirement

A minimal executable stabilizer scaffold must represent:

    a finite set of carrier actions

    composition of those actions

    identity

    inverse

    induced family action

    the subset preserving one selected equivalence system

## Required Distinctions

The implementation must distinguish:

    carrier actions acting trivially on the family

from:

    carrier actions moving among family members

and:

    carrier actions preserving one selected family member

The selected-system stabilizer must be derived from action.

It must not be supplied only as the scalar value:

    240

## Required Executable Tests

A first bounded implementation must verify:

1. carrier actions compose

2. composition preserves the carrier permutation domain

3. the identity action exists

4. every registered action has an inverse

5. induced family actions compose compatibly

6. a selected-system stabilizer can be derived by filtering actions
   that fix the selected system

7. the three certified involutions belong to the stabilizers of P0,
   P1, and P2 respectively

8. each certified involution is excluded from the other two
   selected-system stabilizers

## Deferred Full Correspondence

The first scaffold need not enumerate all 720 automorphisms.

A later source-backed test must recover:

    full action count
        720

    partition-action kernel count
        120

    selected-system stabilizer count
        240

The scalar counts are correspondence targets.

They are not inputs to the derivation.

## Candidate Structure

The smallest candidate appears to require:

    finite carrier-action group

    induced family action

    stabilizer derived from selected equivalence

No broader semantic object is admitted.

## Result Classification

This is a bounded stabilizer frontier scaffold.

It is not an executable result.

It does not complete the three-quotient frontier.

## Boundary

A stabilizer is not treated as:

    witness

    context

    body

    character

    authority

No physical interpretation is claimed.

No global completeness is claimed without the full certified
automorphism set.

## Keeper Candidate

Selection does not only choose a lawful identification.

It also determines which symmetries remain internal to that choice.
