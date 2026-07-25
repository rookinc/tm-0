# Receipt 0040

## Title

Return Residue Is Earned by the Path

## Status

Research receipt.

## Result

A transition path can be executed as an ordered sequence of lawful
relations.

The runner records:

    realized steps

    visited states

    traversed relations

    final state

Return is detected when the final state equals the initial state.

Traversal residue is derived from the executed relation history rather
than copied from one transition rule.

## Interpretation

A step does not carry a cycle by itself.

A cycle becomes available only after an executed path returns.

Residue belongs to the accumulated traversal history.

## Consequence

TM-0 now distinguishes:

    transition rule

    executed step

    realized path

    detected return

    derived residue

This removes one layer of prepared cycle metadata from the path result.

## Limitation

Transition rules still retain the older cycle_residue field because the
single-step executor currently requires it.

The path runner does not use that field when deriving traversal residue.

The current residue is relation traversal parity.

It is not yet a signed cycle product or a full cycle-space character.

The ordered relation path is still supplied externally.

## Keeper

The rule permits motion.

The returning path earns residue.
