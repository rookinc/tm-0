# Experiment 036

## Title

Witness Reliability Is Contextual

## Status

Executable candidate.

## Question

Can one witness earn different reliability histories in different
character or boundary contexts?

## Starting Result

Experiment 034 made reliability an accumulated result of later closure
comparison.

Experiment 035 used one global reliability weight per witness.

That global score may be too coarse.

## Construction

Reliability history is indexed by context.

Each context stores its own:

    confirmed count

    contradicted count

    net reliability

A report evaluated in one context does not update another context.

## Result

An unknown context begins with no earned reliability.

Confirmation updates only the active context.

Contradiction updates only the active context.

The same witness can be reliable in one context and unreliable in
another.

Repeated reports accumulate within their own context.

## Interpretation

Witness reliability is not necessarily global.

It may depend on the relational conditions under which the report was
made.

The witness is therefore better represented by a reliability field
over contexts than by one scalar.

## Consequence

Reliability-weighted arbitration should eventually use:

    witness

    current context

    context-specific history

rather than one universal score.

## Boundary

The context labels are supplied by the experiment.

The experiment does not yet derive context from cycle character,
boundary class, or provenance structure.

It does not model similarity between contexts, transfer of reliability,
uncertainty, decay, or forged receipts.

## Keeper

A witness may be reliable here and unearned there.
