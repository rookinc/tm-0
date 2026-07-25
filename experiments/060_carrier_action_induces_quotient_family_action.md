# Experiment 060: Carrier Action Induces Quotient Family Action

## Question

Do the certified permutations of the thirty-element carrier induce the
certified action on the three quotient systems?

## Authoritative Source

The source certificate is:

    Project 41
    project42_quotient_frame_orbit_certificate_004.json

It records the carrier involutions:

    tau0
    tau1
    tau2

and their actions on the quotient systems:

    tau0
        [0, 2, 1]

    tau1
        [2, 1, 0]

    tau2
        [1, 0, 2]

## Implementation

The certified carrier-action fixture is:

    src/tm0/g60_quotient_carrier_action.py

It defines:

    CertifiedCarrierAction

    TAU0

    TAU1

    TAU2

    CERTIFIED_CARRIER_ACTIONS

Each action contains:

    one permutation of the thirty carrier vertices

    one certified permutation of P0, P1, and P2

## Executable Result

Each certified carrier action is an involution.

For every certified action:

    the thirty-element carrier is preserved

    each pair partition is transported by the carrier permutation

    the transported partition equals the partition named by the
    certified family permutation

Specifically:

    tau0 fixes P0 and swaps P1 with P2

    tau1 fixes P1 and swaps P0 with P2

    tau2 fixes P2 and swaps P0 with P1

The family action is therefore induced by an explicit action on the
carrier.

It is not merely an independent relabeling of system names.

## Focused Evidence

The focused suite verifies:

    three certified carrier actions are registered

    each carrier action is an involution

    tau0 induces its certified family action

    tau1 induces its certified family action

    tau2 induces its certified family action

    each action fixes its certified partition

    each action swaps the other two partitions

    the carrier vertex set is preserved

    unknown carrier vertices are rejected

Focused result:

    9 tests passed

Full-suite result:

    416 tests passed

## Interpretation

The quotient-family symmetry is grounded in the carrier.

A lawful transformation of the fixed carrier transports one
identification system to another.

The carrier remains the same carrier set.

The active identification law may change under the carrier symmetry.

## Earned Correspondence

TM-0 now represents the chain:

    carrier action
    ->
    transported equivalence partition
    ->
    quotient-family action
    ->
    moved selected equivalence

This joins the previously separate:

    carrier surface

and:

    quotient-family surface

## Selected-System Stabilizer

Each certified involution fixes exactly one quotient system.

At the current bounded level, this earns:

    an action that preserves one selected equivalence system

It does not yet construct the complete stabilizer subgroup.

## What Has Not Been Earned

The current implementation does not yet represent:

    all 720 carrier automorphisms

    the order-120 kernel of the partition action

    the full order-240 stabilizer of one quotient system

    composition of carrier actions as a group object

    quotient graph construction

    verification that every quotient is L(P)

These remain separate requirements.

## Classification

This is a source-backed executable correspondence.

It proves compatibility between the certified carrier actions and the
certified quotient-family actions.

It does not yet complete the automorphism-group correspondence.

## Ontology Status

The distinction among:

    carrier

    equivalence family

    selected equivalence

    action on the carrier

    induced action on the family

is now executable and G60-backed.

No broader concept is admitted.

## Boundary

Carrier action is not treated as physical motion.

Transport of a partition does not mutate the carrier set.

Fixing one quotient system under one involution does not by itself
establish the full selected-system stabilizer.

The certificate establishes the natural three-system orbit only.

## Keeper

The family action is not imposed above the carrier.

It is induced from within it.
