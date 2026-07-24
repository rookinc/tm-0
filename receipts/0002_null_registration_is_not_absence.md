# Receipt 0002

## Title

Null Registration Is Not Absence

## Status

Research receipt.

## Registration

A carrier may exist while its register remains null.

The following are distinct:

    carrier absent

    carrier present with null registration

    carrier present with characterized registration

A null registration does not erase the carrier.

## Examples

A pencil-and-paper thalion may be drawn without writing any
registration.

A floating electronic node may exist without a committed logical
value.

Within a B32K address space, `.b32k` may denote an address with null
left-hand character, while `*.b32k` describes the wider possibility
address space.

## Executable Consequence

TM-0 now admits:

    ABSENT -> NULL

as a realization.

It rejects:

    NULL -> NULL

as an identity transition when no other state component changes.

## Boundary

The model does not yet prove that null, A, and B are sufficient.

It does not yet derive the thalion.

It does not yet model character, history, relation, closure, return,
or information.

## Keeper

Possibility is the address space.

Null is a lawful address within it.
