# Receipt 0035

## Title

Reliability Can Outweigh Headcount

## Status

Research receipt.

## Result

Witness arbitration can be weighted by reliability earned from prior
closure history.

Equal total reliability remains unresolved.

A more reliable report can resolve disagreement.

One strongly receipted dissenting witness can outweigh two weak
reports.

A witness with no evaluated history contributes zero weight.

## Interpretation

Report count and witness weight are different quantities.

Headcount measures how many reports were made.

Reliability history measures what those reports have earned through
later closure.

## Consequence

The witness layer now supports:

    independent provenance

    accumulated closure history

    earned reliability

    reliability-weighted arbitration

A majority of weak reports is not automatically stronger than one
well-receipted dissent.

## Limitation

The current weight is:

    confirmed - contradicted

This remains a toy scaffold.

The experiment does not establish the correct treatment of:

    negative reliability

    context dependence

    uncertainty

    coordinated error

    forged receipts

    reliability decay

## Keeper

Headcount records how many spoke.

Closure history records how much their witness has earned.
