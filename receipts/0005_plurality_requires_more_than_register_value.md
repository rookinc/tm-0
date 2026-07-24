# Receipt 0005

## Title

Plurality Requires More Than Register Value

## Status

Research receipt.

## Result

Two independently instantiated carriers with identical null
registration are equal under the current lawful description.

The extensional catalogue collapses:

    Carrier(NULL)
    Carrier(NULL)

to:

    Carrier(NULL)

## Interpretation

Register value alone does not distinguish carrier plurality.

Python object identity can distinguish two allocations, but TM-0 has
not earned implementation identity as mechanical structure.

## Consequence

The current model can express:

    a null carrier description

It cannot yet express:

    two distinct null carriers

without adding further structure.

## Candidate Missing Structures

One or more of the following may eventually be required:

    occurrence
    relation
    boundary
    history
    position
    provenance

None is promoted by this experiment.

## Keeper

Two instances are not yet two thalions.

Plurality must be registered somewhere.
