# Experiment 003

## Title

Character-Blind Register Quotient

## Status

Executable candidate.

## Question

Are named A/B polarities required to preserve the current TM-0
distinction between carrier absence, null registration, and non-null
registration?

## Construction

Experiment 002 used:

    ABSENT
    NULL
    A
    B

Experiment 003 applies the quotient:

    ABSENT -> ABSENT
    NULL   -> NULL
    A      -> CHARACTERIZED
    B      -> CHARACTERIZED

The quotient forgets which non-null character is present.

## Surviving Structure

The quotient preserves:

    ABSENT != NULL

    NULL != CHARACTERIZED

    ABSENT -> NULL

    NULL -> CHARACTERIZED

    CHARACTERIZED -> NULL

It therefore preserves the distinction between:

    carrier absence

    carrier presence with null registration

    carrier presence with non-null registration

## Lost Structure

The transitions:

    A -> B
    B -> A

become:

    CHARACTERIZED -> CHARACTERIZED

and are therefore identity transitions in the quotient.

## Interpretation

Named A/B polarity is not required for the current carrier/null
distinction.

A/B becomes necessary only when TM-0 needs to represent a change
between distinct non-null registrations.

## Boundary

This experiment does not derive A/B.

It does not establish that exactly two non-null characters exist.

It does not model return, comparison, character accumulation, history,
witness, graph structure, or physical polarity.
