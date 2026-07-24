# Receipt 0038

## Title

The Event Carries Its Context

## Status

Research receipt.

## Result

A witness context can be reconstructed from a realized event record.

The event contributes:

    source state

    target state

    traversed relation

    boundary contacts

    cycle residue

From these, the system derives:

    boundary signature

    event character

    structural context address

Equivalent boundary-contact order produces the same normalized context.

Changing the relation or cycle residue changes the context.

Malformed event records are rejected.

## Interpretation

Context can arise from what happened rather than from what the event was
called.

The realized event preserves enough structure to address the
reliability history relevant to that occurrence.

## Consequence

The witness layer now supports:

    realized event

    execution-derived context

    context-specific closure history

    earned reliability

    weighted arbitration

This further reduces externally supplied metadata.

## Limitation

The event record remains supplied.

The transition system does not yet generate:

    source and target states

    traversed relation

    boundary contacts

    cycle residue

The event character remains a bounded toy encoding.

Cycle residue is recorded rather than derived from an executed closed
walk.

## Keeper

The event does not merely occur in a context.

Its trace can carry that context forward.
