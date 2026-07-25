# Experiment 058: Three Quotient Systems Admit Symmetry Action

## Question

Can TM-0 represent the certified symmetry action on the three lawful
quotient systems without collapsing them into one system or mutating
the underlying carrier?

## Authoritative Source

The source certificate is:

    Project 41
    project42_quotient_frame_orbit_certificate_004.json

The certificate records an action on:

    P0
    P1
    P2

with image:

    S3

The certified partition actions are:

    [0, 1, 2]
    [0, 2, 1]
    [1, 0, 2]
    [1, 2, 0]
    [2, 0, 1]
    [2, 1, 0]

The action is transitive on the three quotient systems.

## Current TM-0 Capability

TM-0 currently represents:

    one fixed carrier

    three registered equivalence systems

    one selected system

    preserved alternatives

It does not yet represent:

    a permutation acting on the registered system family

    transport of the selected system under that action

    the subgroup fixing one selected system

## Bounded Requirement

A minimal executable extension must represent:

    a finite family of named equivalence systems

    a permutation of that family

    application of the permutation to the selected system

    preservation of the underlying carrier

    preservation of the registered family

    distinction between:

        full family action

        selected-system stabilizer

## Required Executable Tests

The first implementation must verify:

1. all six certified permutations are valid actions on P0, P1, and P2

2. the six actions are distinct

3. the action image has order six

4. the action is transitive on the three systems

5. each certified involution fixes exactly one system

6. each certified involution swaps the other two systems

7. applying an action changes the selected system when the permutation
   moves it

8. applying an action does not change the carrier

9. applying an action does not delete any registered system

10. the identity action leaves the selected system unchanged

## Candidate Structure

The smallest candidate appears to require:

    selected equivalence

    family permutation

No broader concept is admitted yet.

Possible implementation names include:

    EquivalenceFamilyAction

    SelectedEquivalenceAction

These names remain provisional.

## Why Selection Alone Is Insufficient

Selection records which equivalence system is active.

It does not record how lawful symmetry moves one selection to another.

Without the family action, TM-0 cannot distinguish:

    alternatives merely stored together

from:

    alternatives related by certified symmetry

## Why Quotient Values Remain Insufficient

All three systems have the same block-size profile:

    fifteen pairs of size two

The symmetry acts on the identification systems themselves.

It does not require a change in quotient-value summary.

## Result Classification

This is a bounded symmetry-action scaffold.

It is not yet an executable result.

It does not admit a new permanent semantic object.

## Boundary

No action on the thirty carrier vertices is required in the first test.

No full automorphism group is required in the first test.

No quotient graph construction is required.

No covering-edge verification is required.

No global completeness claim is made beyond the certified natural orbit.

No claim is made that symmetry action is:

    execution

    context

    witness

    character

    observation

## Keeper Candidate

Selection chooses one lawful identification.

Symmetry moves among the lawful choices.
