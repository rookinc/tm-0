# Experiment 041

## Title

Step Trace and Path Receipt Are Distinct

## Status

Executable candidate.

## Question

Can TM-0 separate what belongs to one executed step from what can only
be earned by a completed path?

## Starting Result

Experiment 040 executed ordered paths and derived traversal residue from
path history.

The older transition rule still carried a cycle_residue field because
the single-step event schema required it.

## Construction

The transition layer is rebuilt around two distinct records.

A step rule contains:

    source state

    target state

    relation name

    boundary contacts

A step event contains:

    source state

    target state

    traversed relation

    boundary contacts

Neither record contains cycle residue.

A path receipt contains:

    initial state

    final state

    ordered step events

    visited states

    traversed relations

    return status

    path-derived traversal residue

## Result

Step rules no longer contain cycle residue.

Step events no longer contain cycle residue.

A lawful step emits only the trace of that step.

A completed path records the ordered event sequence.

Return status is derived from initial and final state.

Traversal residue is derived from the completed path history.

Repeated traversals can cancel to even residue.

Malformed systems and unlawful requests are rejected.

## Interpretation

Step-local facts and path-earned facts belong to different layers.

A single transition can report what happened locally.

It cannot honestly report a cycle residue before a path has been
executed and evaluated.

## Consequence

TM-0 now has an explicit receipt boundary:

    step event

records local execution.

    path receipt

records accumulated return structure.

Cycle residue now appears only on the path side of that boundary.

## Boundary

The current residue remains relation traversal parity.

It is not yet a signed cycle product or full graph cycle-space
character.

The path request sequence is still supplied externally.

Boundary contacts remain stored on rules rather than derived from a
separate boundary object.

The older executor modules remain in the repository as prior
experimental stages.

## Keeper

A step may leave a trace.

Only a path can earn a return receipt.
