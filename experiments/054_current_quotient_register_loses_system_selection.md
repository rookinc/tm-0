# Experiment 054: Current Quotient Register Loses System Selection

## Question

Can the current TM-0 quotient-register scaffold represent the selection
of one among several equivalent lawful quotient systems on the same
underlying body?

## Evidence Source

The current implementation is:

    src/tm0/quotient_register.py

Its central map is:

    forget_polarity(state)

with codomain:

    ABSENT
    NULL
    CHARACTERIZED

The associated realization records only:

    before quotient state
    after quotient state

## Current Capability

The scaffold can represent one fixed forgetful operation:

    AddressedState
    ->
    QuotientState

It preserves:

    absence

    null registration

    presence of non-null character

It forgets:

    A versus B polarity

This is a valid quotient operation for the original experiment.

## G60 Frontier Requirement

The three-quotient frontier requires representation of:

    one fixed underlying body

    three lawful quotient systems

    equivalent quotient systems under full symmetry

    selection of one quotient system

    a stabilizer preserving the selected system

    no mutation of the underlying body

## Expressive Test

Consider two executions with the same underlying body and the same
quotient-state values.

Execution A selects quotient system Q1.

Execution B selects quotient system Q2.

Assume Q1 and Q2 are distinct but equivalent under a symmetry of the
body.

The current quotient-register output contains only:

    before
    after

It contains no field for:

    quotient system

    quotient map

    selected pair partition

    equivalence action

    stabilizer

Therefore Execution A and Execution B produce the same current TM-0
description whenever their quotient-state values agree.

## Demonstrated Gap

The current scaffold cannot distinguish:

    same body
    plus selected quotient system Q1

from:

    same body
    plus selected quotient system Q2

The distinction is not recoverable from `QuotientState`.

The current quotient value records what distinctions were forgotten.

It does not record which lawful forgetting relation was used.

## Why the Distinction Matters

The three quotient systems are not merely three names for one map.

Each system consists of a different partition of the same vertex set
into fifteen disjoint pairs.

Selecting one system determines:

    which vertices are identified

    which two-fold quotient map is active

    which subgroup preserves that selection

The full graph remains unchanged.

The selected identification law changes.

## Existing Ontology Test

### Body

Body is insufficient by itself.

The underlying body remains fixed across all three selections.

### Character

Quotient-state character is insufficient.

The same quotient values may occur under different quotient systems.

### Boundary

No boundary crossing is required.

The distinction exists even before execution crosses a cut.

### Context

Context may eventually carry the selection.

Current TM-0 context is derived from realized event structure and does
not yet define a lawful quotient-system selector.

### Witness

A Witness could report the selected system only if that distinction
already existed in the executable semantics.

Witness does not create the missing distinction.

### Arbitration

Arbitration may compare reports about quotient selection.

It does not define quotient selection.

## Result Classification

This is an expressive-gap result.

It is not a new semantic admission.

It demonstrates that the current quotient-register scaffold is
insufficient for the three-quotient frontier.

## Exact Missing Capability

TM-0 currently lacks an executable way to bind:

    a fixed body

to:

    one selected lawful equivalence relation

while preserving:

    the body itself

    the existence of alternative equivalent selections

    the distinction between full symmetry and selected-system
    stabilizer

## Candidate Space

Possible future candidates may involve:

    quotient system

    equivalence relation

    reduction law

    selected registration

    contextual selector

No candidate is admitted here.

The smallest adequate abstraction remains unresolved.

## Boundary

This experiment does not claim that quotient selection is context.

It does not claim that quotient selection is witness.

It does not claim that quotient selection is character.

It does not claim that the three systems are physically different
observers.

It does not generalize beyond the demonstrated requirement.

## Keeper

A quotient value says what remains.

A quotient system says what was identified.
