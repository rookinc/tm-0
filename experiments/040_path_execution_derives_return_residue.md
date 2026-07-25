# Experiment 040

## Title

Path Execution Derives Return Residue

## Status

Executable candidate.

## Question

Can a transition system execute an ordered path, detect return, and
derive a residue from the realized traversal history?

## Starting Result

Experiment 039 executed one lawful transition and emitted one realized
event.

Cycle residue was still stored directly on each transition rule.

## Construction

A path runner accepts:

    transition system

    initial state

    ordered relation requests

Each requested relation is executed in sequence.

The runner records:

    initial state

    realized steps

    visited states

    traversed relations

    final state

    return status

Traversal residue is derived after execution.

For each registered relation, the residue records traversal parity:

    zero for even traversal count

    one for odd traversal count

## Result

A one-step path can leave the initial state without returning.

A lawful two-step path can return to the initial state.

The runner preserves the full visited-state and relation sequence.

Return is detected from equality of initial and final state.

Traversal residue is computed from the realized path.

Repeating each relation twice produces even residue.

Empty paths, unknown states, unknown relations, and unlawful relation
sequences are rejected.

## Interpretation

A cycle is not stored on a step.

It is recognized from an executed path that returns.

Residue can therefore be computed from accumulated traversal rather
than copied from a single transition rule.

## Consequence

The operational sequence is now:

    lawful transition system

    ordered relation requests

    executed event sequence

    visited-state path

    return detection

    path-derived traversal residue

This separates:

    transition data

from:

    path history

and:

    return residue

## Boundary

The transition rules still contain their older cycle_residue field
because the existing executor requires it.

The path runner does not use that field when deriving traversal
residue.

Traversal parity is a bounded toy residue and is not yet the signed
cycle product or graph cycle-space character used elsewhere in TM-0.

The path is supplied as an ordered request sequence rather than selected
by an internal policy.

## Keeper

A step changes state.

A cycle is earned when executed steps return.
