# Receipt 0004

## Title

Absence Is Not an Address

## Status

Research receipt.

## Result

The current internal register mechanics can be represented without an
ABSENT register value.

The internal address space of an existing carrier contains:

    NULL
    CHARACTERIZED

Carrier absence is represented outside that address space.

## Construction

Before carrier instantiation:

    no carrier

After carrier instantiation:

    Carrier(NULL)

After characterization:

    Carrier(CHARACTERIZED)

## Registration

The transition:

    no carrier -> Carrier(NULL)

creates an addressable carrier without assigning non-null character.

The transition:

    Carrier(NULL) -> Carrier(CHARACTERIZED)

changes the internal registration.

These are distinct operations.

## Consequence

ABSENT has not earned status as an internal TM-0 address.

NULL remains a lawful address.

CHARACTERIZED remains a lawful address class.

The carrier now becomes an explicit candidate for the next squeeze.

## Keeper

Absence is not an address.

Null is the first address of a present carrier.
