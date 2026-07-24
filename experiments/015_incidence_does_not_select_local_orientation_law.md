# Experiment 015

## Title

Incidence Does Not Select the Local Orientation Law

## Status

Executable negative result.

## Question

Do direction, incidence, composition, and closure force local
orientation inversion?

## Construction

The same closed incidence structure was evaluated under two local
laws:

    PRESERVE

    INVERT

No change was made to the relations, endpoint equivalence, or closure.

## Result

For an odd closed chain:

    PRESERVE -> SAME

    INVERT   -> POLAR

For an even closed chain:

    PRESERVE -> SAME

    INVERT   -> SAME

The same incidence structure admits both laws.

## Interpretation

Local inversion is not derived from the currently earned structure.

Direction supplies source and target roles.

Incidence supplies junctions.

Composition supplies paths.

Closure admits return.

None of these selects whether local traversal preserves or reverses
orientation.

## Consequence

Experiment 014 remains conditional:

    if each local traversal inverts orientation,
    then odd closure returns polar

The inversion law requires an additional source.

## Next Question

What minimal local structure distinguishes PRESERVE from INVERT?

Candidates include:

    boundary side exchange

    port pairing

    local sheet transition

    traversal parity carried by the relation

None is promoted here.

## Boundary

This experiment does not reject local inversion.

It shows only that local inversion is not forced by the current
incidence model.
