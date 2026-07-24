# Experiment 022

## Title

Character Defines a Possibility Frontier

## Status

Executable candidate.

## Question

Can the current cycle-space character define an address space of local
realizations without selecting one?

## Starting Result

Experiment 021 established that flipping one local relation sign can
change the switching-invariant cycle-space character while preserving
the relational body.

## Construction

For each relation address in the current signed graph:

1. Keep the incidence structure fixed.
2. Flip the local sign at that address.
3. Compute the resulting cycle-space character.
4. Record the addressed candidate realization.

The complete set of addressed candidates is the possibility frontier.

## Result

The frontier contains one candidate realization per relation address.

Every candidate shares the same current character.

Every candidate produces a changed character in the tested graph.

Distinct relation addresses may produce the same resulting character.

The frontier contains several candidates and selects none.

## Interpretation

Possibility is now executable as an address space over lawful candidate
realizations.

A possibility contains:

    an address

    a current character

    a resulting character

Possibility does not imply selection.

Possibility does not imply execution.

## Consequence

The TM-0 cycle now has an executable partial form:

    character
        ->
    possibility frontier
        ->
    unresolved candidate realizations

The next missing operation is resolution or selection.

That operation must remain outside the possibility frontier itself.

## Boundary

This experiment assumes that every single-edge sign flip is a lawful
candidate realization.

It does not yet derive admissibility constraints among candidates.

It does not select, rank, weight, or execute any possibility.

It does not introduce agency, probability, time, energy, or physical
motion.

## Keeper

Character shapes the address space of what may happen next.
