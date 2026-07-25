# Receipt 0060: Carrier Action Induces Family Action

## Recorded Result

The certified quotient-family action is induced by explicit
permutations of the fixed thirty-element carrier.

The carrier involutions:

    tau0
    tau1
    tau2

transport the three certified partitions:

    P0
    P1
    P2

according to their certified family actions.

## Executable Evidence

Implementation:

    src/tm0/g60_quotient_carrier_action.py

Focused tests:

    tests/test_g60_quotient_carrier_action.py

Focused result:

    9 tests passed

Full-suite result:

    416 tests passed

## Certified Action

    tau0 fixes P0 and swaps P1 with P2

    tau1 fixes P1 and swaps P0 with P2

    tau2 fixes P2 and swaps P0 with P1

Each carrier action is an involution.

Each preserves the same carrier vertex set.

## Earned Chain

TM-0 now represents:

    carrier action
    ->
    transported equivalence partition
    ->
    induced family action
    ->
    moved selected equivalence

The family action is therefore grounded in the carrier.

It is not an independent relabeling imposed above it.

## Selected-System Preservation

Each certified involution preserves one quotient system.

This earns an explicit carrier action that fixes one selected
equivalence system.

It does not yet construct the complete selected-system stabilizer.

## Classification

This is a source-backed executable correspondence receipt.

It joins the carrier surface to the quotient-family surface.

It does not yet complete the three-quotient frontier.

## Boundary

The implementation does not yet represent:

    all 720 carrier automorphisms

    the order-120 kernel of the partition action

    the full order-240 stabilizer of one quotient system

    group composition on the carrier actions

    quotient graph construction

    verification that each quotient is L(P)

Carrier action is not claimed to be physical motion.

Transporting an equivalence partition does not mutate the carrier.

The source certificate establishes only the natural three-system orbit.

## Keeper

The family action is not imposed above the carrier.

It is induced from within it.
