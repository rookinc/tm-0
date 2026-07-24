# Receipt 0037

## Title

Context Is a Structural Address

## Status

Research receipt.

## Result

Witness context can be encoded from explicit boundary and character
data rather than supplied only as a descriptive label.

Equivalent boundary signatures normalize to the same context.

Changing the boundary changes the context.

Changing the ordered character changes the context.

Malformed boundary or character inputs are rejected.

## Interpretation

Context can be carried by the event as structure.

It need not exist only as an external name assigned by an observer.

A contextual reliability record can therefore be addressed by:

    normalized boundary signature

    ordered character

## Consequence

The witness layer now supports the sequence:

    event structure

    derived context address

    context-specific closure history

    earned reliability

    weighted arbitration

This reduces one source of free metadata in the reliability system.

## Limitation

The boundary signature and character remain supplied inputs.

The experiment does not yet derive them from a realized transition,
cycle, body, or observation path.

The serialized context key is an implementation convenience.

Gauge equivalence, basis changes, graph isomorphism, and similarity
between nearby contexts remain unresolved.

## Keeper

Context is not merely assigned to an event.

It can be reconstructed from what the event carries.
