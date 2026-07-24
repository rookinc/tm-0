# Experiment 027

## Title

Character Conditions Admissibility

## Status

Executable candidate.

## Question

Can the current cycle-space character itself partition the possibility
frontier into admissible realizations and structured absence?

## Starting Result

Experiment 026 showed that constraint can structure absence without
deleting possibility.

The tested constraint was external to character.

## Toy Character Law

Experiment 027 uses one character-conditioned scaffold:

    a candidate is admissible when it does not reduce
    the number of POLAR cycle bits

The rule is not proposed as a universal TM law.

Its purpose is to test whether present character can determine the
status of future possibilities.

## Construction

For every candidate realization:

1. Count POLAR bits in the current character.
2. Count POLAR bits in the resulting character.
3. Admit the candidate when the count does not decrease.
4. Place all other candidates in structured absence.

## Result

An all-PRESERVE character admits every tested local sign flip.

A character containing POLAR return bits excludes at least one
candidate that would reduce the POLAR count.

The excluded candidate remains addressable in the full possibility
frontier.

The admissible and absent subsets are disjoint and complete.

## Interpretation

Character can act as constraint.

The current return character does not merely describe the body.

It can classify what may become next.

## Consequence

The executable loop now contains:

    realization
        ->
    character
        ->
    character-conditioned constraint
        ->
    admissible frontier
        ->
    structured absence

This closes a first toy version of the proposed TM cycle.

## Boundary

The monotone POLAR-count rule remains assumed.

The experiment does not establish that increasing or preserving POLAR
count is physically, mathematically, or ethically privileged.

It does not select or execute a candidate.

It does not introduce agency, preference, probability, time, energy,
geometry, or physical motion.

## Keeper

Character does not only remember return.

Character can shape what return may happen next.
