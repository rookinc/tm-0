# Receipt 0054: Quotient Value Loses System Selection

## Recorded Result

The current TM-0 quotient-register scaffold represents one fixed
forgetful map:

    AddressedState
    ->
    QuotientState

It records:

    what survives the quotient

It does not record:

    which lawful equivalence relation produced the quotient

## Demonstrated Collision

Two executions may share:

    the same underlying body

    the same quotient-state values

while selecting different lawful quotient systems:

    Q1

    Q2

The current TM-0 description identifies these situations.

The distinction cannot be recovered from `QuotientState`.

## G60 Requirement

The three lawful quotient systems determine different partitions of the
same underlying vertex set.

Selecting one system determines:

    which vertices are identified

    which two-fold quotient map is active

    which stabilizer preserves the selection

The underlying body remains unchanged.

## Expressive Gap

TM-0 currently lacks an executable way to bind:

    a fixed body

to:

    one selected lawful equivalence relation

while preserving:

    alternative equivalent selections

    the full symmetry relating them

    the stabilizer of the selected system

## Classification

This is an expressive-gap receipt.

It does not admit a new semantic object.

It records insufficiency in the current quotient-register scaffold.

## Unresolved Candidate

The smallest adequate abstraction remains open.

Possible candidates include:

    quotient system

    equivalence relation

    reduction law

    selected registration

No candidate is admitted by this receipt.

## Boundary

The quotient systems are not declared to be:

    contexts

    witnesses

    bodies

    observers

    memories

Selection does not mutate the underlying body.

Equivalence under full symmetry does not erase the distinction between
selected systems.

## Keeper

A quotient value says what remains.

A quotient system says what was identified.
