# Experiment 014

## Title

Parity Generates Return Polarity

## Status

Executable conditional result.

## Question

Does global polarity emerge from the parity of locally identical
orientation inversions around a closed relation chain?

## Starting Result

Experiment 013 established that return alone does not force polarity.

Polarity appears only when the returned reading differs from the
departure reading.

The missing question was what lawful structure could produce that
difference.

## Local Rule

Experiment 014 introduces one uniform local rule:

    every traversed relation applies one orientation inversion

The rule is local and identical at every step.

No special global half-flip is added at closure.

## Construction

For a closed chain with n relations, the returned orientation is:

    invert applied n times

Therefore:

    even n -> SAME

    odd n  -> POLAR

## Tested Closures

    n = 3   -> POLAR

    n = 4   -> SAME

    n = 5   -> POLAR

    n = 15  -> POLAR

The result is independent of whether the departure reading begins as
FORWARD or REVERSED.

## Result

All nine focused parity tests passed.

Under the tested local inversion law:

    returned orientation = departure orientation times (-1)^n

## Interpretation

Global polarity can emerge from composition.

It need not be assigned by a special global flip at closure.

Under the tested law, the half-flip is the accumulated result of an
odd number of identical local inversions.

## Important Boundary

This experiment does not derive the local inversion law.

It proves only the conditional statement:

    if every traversed relation inverts orientation,
    then odd closure returns polar
    and even closure returns same

The next problem is whether local inversion follows from a more
primitive incidence, traversal, or boundary law.

## Boundary

This experiment does not derive A and B as intrinsic register values.

It does not establish physical orientation, geometry, motion, time,
agency, probability, witness, or character accumulation.
