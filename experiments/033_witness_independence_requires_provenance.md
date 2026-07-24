# Experiment 033

## Title

Witness Independence Requires Provenance

## Status

Executable candidate.

## Question

Does a third report resolve disagreement only when it carries
independent provenance?

## Starting Result

Experiment 032 showed that three reports can break a two-report tie
under strict majority.

That result did not distinguish an independent third witness from a
duplicate report.

## Construction

Each witness receipt contains:

    report

    source occurrence

    observation path

Two receipts are treated as independent only when they do not share:

    source occurrence

    observation path

## Result

Two independent conflicting receipts remain unresolved.

Three independent receipts can resolve by strict majority.

A duplicated source does not add an independent vote.

A duplicated observation path does not add an independent vote.

A copied third report does not break a tie.

## Interpretation

Witness count alone is insufficient.

The third witness must carry independent provenance.

The triad is therefore not merely:

    three reports

It is:

    three independently receipted observations

## Consequence

The witness layer now distinguishes:

    report multiplicity

from:

    independent witness multiplicity

Stable arbitration requires enough independent receipts, not merely
enough repeated claims.

## Boundary

The independence rule is bounded and supplied by the experiment.

Different source occurrence and observation path do not guarantee:

    truth

    reliability

    absence of coordination

    absence of shared hidden causes

The experiment does not yet derive witness trust or correctness.

## Keeper

A repeated claim is not another witness.

A witness earns weight through independent provenance.
