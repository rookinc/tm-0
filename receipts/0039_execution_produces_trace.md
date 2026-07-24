# Receipt 0039

## Title

Execution Produces the Trace

## Status

Research receipt.

## Result

A minimal transition system can execute a lawful relation and emit the
realized event required by the witness-context layer.

A successful step records:

    prior state

    next state

    traversed relation

    boundary contacts

    cycle residue

The event is produced by execution rather than supplied separately.

Unknown states, unknown relations, unlawful source-state requests, and
malformed transition systems are rejected.

## Interpretation

A transition rule describes lawful possibility.

Execution selects one lawful possibility and turns it into an event.

The event preserves a trace that can be used to reconstruct context and
evaluate later witness reliability.

## Consequence

The operational chain now contains:

    registered states

    lawful transition rules

    executed relation

    realized event

    derived context

    context-specific reliability

    weighted arbitration

TM-0 now produces the event record consumed by the witness layer.

## Limitation

Transition rules remain authored directly.

Boundary contacts and cycle residue remain stored on each rule.

They are not yet derived from an accumulated path or completed return.

The executor handles one step and does not yet detect closure.

## Keeper

Possibility is registered by the rule.

Trace begins when the rule is executed.
