# Experiment 032

## Title

Third Witness Resolves Pair Disagreement

## Status

Executable candidate.

## Question

Is a third witness required to resolve disagreement between two
equally situated witness reports?

## Starting Result

Experiment 031 established that two states are sufficient for a
boundary-preserving return.

That did not establish stable witness.

## Construction

Witnesses report one of two registrations:

    SAME

    POLAR

The experiment compares:

    one report

    two equal reports

    two conflicting reports

    three reports with a strict majority

## Result

One report resolves only trivially.

Two equal reports reach consensus.

Two conflicting reports remain unresolved because neither witness has
earned priority.

Three reports can resolve disagreement by strict majority.

## Interpretation

The third witness is not required for return.

It is required in the tested model for arbitration when two equally
situated reports disagree.

This earns a bounded triadic role:

    report

    counter-report

    deciding witness

## Important Boundary

This is not yet a general witness theorem.

The strict-majority rule is supplied by the experiment.

The third witness may itself be wrong.

The experiment does not establish truth, independence, reliability, or
provenance.

It establishes only that a symmetric two-report conflict has no
internal resolution, while a third report can break the tie.

## Consequence

The triad first appears at the witness layer, not at the return layer.

Two states are enough to leave and come home.

Three reports are enough to resolve one binary disagreement under
strict majority.

## Keeper

Return needs two states.

Disagreement needs a third witness.
