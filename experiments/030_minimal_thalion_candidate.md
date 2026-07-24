# Experiment 030

## Title

Minimal Thalion Candidate

## Status

Executable candidate.

## Question

What is the smallest finite body region that supports nontrivial
character change while preserving one boundary?

## Starting Result

Experiment 029 defined a body as a connected region of character states
reachable through boundary-preserving realizations.

A thalion candidate should be smaller and nontrivial.

## Candidate Conditions

A finite body region qualifies when it has:

    one persistent boundary

    at least two states

    at least two distinct character values

    at least one boundary-preserving transition

## Result

A one-state region does not qualify.

Two connected states with the same boundary and different character
values do qualify.

A boundary-changing transition does not enlarge the candidate.

Two connected states with identical character do not qualify.

The smallest candidate in the tested finite system has two states.

## Interpretation

The minimal executable thalion candidate is not one static state.

It is the smallest boundary-preserving region that can carry a genuine
character transition.

In the tested model:

    two character states

    one persistent boundary

    one internal realization

are sufficient.

## Important Boundary

This experiment identifies a candidate by supplied criteria.

It does not prove that these criteria are necessary in all TM systems.

It does not derive the boundary, transition system, or character space
from a more primitive generator.

It does not yet derive closure, return, polarity, or witness inside the
candidate itself.

## Keeper

A thalion candidate begins where one boundary can carry more than one
return character.
