# Experiment 034

## Title

Witness Reliability From Closure History

## Status

Executable candidate.

## Question

Can witness reliability emerge from repeated comparison with later
closure receipts rather than being assigned in advance?

## Starting Result

Experiment 033 showed that witness independence requires provenance.

Independent provenance does not guarantee that a witness is reliable.

## Construction

Each witness begins with an empty history:

    confirmed = 0

    contradicted = 0

A witness report is later compared with a closure receipt.

Agreement adds one confirmation.

Disagreement adds one contradiction.

The current toy reliability value is:

    confirmed - contradicted

## Result

Agreement increases reliability.

Disagreement decreases reliability.

Repeated closure receipts accumulate a witness history.

A witness with no evaluated receipts has no earned reliability.

Two witness histories can be compared by their accumulated net result.

## Interpretation

Reliability need not be primitive.

It can emerge from the history of how prior reports compare with later
closure.

The closure receipt becomes an accountability surface for witness.

## Consequence

The witness layer now contains:

    independent provenance

    report history

    later closure comparison

    accumulated reliability

Witness influence may eventually depend on earned reliability rather
than equal counting alone.

## Important Boundary

The net reliability score is a toy scaffold.

A later closure receipt is treated as the evaluation reference.

The experiment does not prove that every closure receipt is correct.

It does not model uncertainty, partial agreement, correlated error,
forgery, decay, or context dependence.

## Keeper

A witness is not trusted because it speaks.

A witness earns reliability when later closure agrees with its trace.
