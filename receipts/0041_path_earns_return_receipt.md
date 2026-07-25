# Receipt 0041

## Title

The Path Earns the Return Receipt

## Status

Research receipt.

## Result

Step-local trace and path-earned return structure are now represented
by different records.

A step rule contains:

    source state

    target state

    relation name

    boundary contacts

A step event records one realized transition.

Neither carries cycle residue.

A path receipt records:

    ordered step events

    visited states

    final state

    return status

    path-derived traversal residue

## Interpretation

A single step can preserve local execution facts.

It cannot honestly claim a cycle residue before a path has returned.

Return structure belongs to accumulated history.

## Consequence

TM-0 now separates:

    local transition trace

from:

    completed path receipt

Cycle residue appears only after path execution and return evaluation.

## Limitation

The current residue remains relation traversal parity.

It is not yet a signed cycle product or full cycle-space character.

The relation request sequence remains externally supplied.

Boundary contacts remain stored on transition rules.

Earlier executor modules remain as historical experimental stages.

## Keeper

A step records motion.

A path earns return.
