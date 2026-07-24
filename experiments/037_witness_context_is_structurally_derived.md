# Experiment 037

## Title

Witness Context Is Structurally Derived

## Status

Executable candidate.

## Question

Can witness context be derived from boundary and character data rather
than supplied as a free descriptive label?

## Starting Result

Experiment 036 showed that witness reliability can differ by context.

The context labels in that experiment were supplied externally.

## Construction

A witness context is constructed from:

    a normalized boundary signature

    a binary character

Boundary entries are treated as an unordered signature and sorted into
a canonical order.

Character coordinates remain ordered.

The resulting context key records both structures.

## Result

Equivalent boundary signatures produce the same context regardless of
input order.

Changing the boundary signature changes the context.

Changing the character changes the context.

Character order remains significant.

Empty or malformed structures are rejected.

## Interpretation

Context can be represented as a structural address derived from the
event itself.

The context is no longer only a human-readable category such as:

    same-boundary

    changed-boundary

It can instead be reconstructed from explicit boundary and character
data.

## Consequence

Contextual witness reliability can eventually be indexed by a derived
mechanical address.

The emerging sequence is:

    event structure

    derived context

    context-specific closure history

    earned reliability

    weighted arbitration

## Boundary

The boundary signature and character are still supplied as inputs.

This experiment does not yet derive either structure from a realized
transition, cycle, body, or observation path.

The string key is an encoding convenience, not a theorem object.

The experiment does not address graph isomorphism, gauge equivalence,
character-basis changes, or partial context similarity.

## Keeper

Context is not what the event is called.

Context is what the event structurally carries.
