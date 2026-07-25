# Receipt 0046

## Title

A Thalion Is a Returning Body

## Status

Research receipt.

## Result

TM-0 can derive thalion candidates by adding nontrivial internal return
to the body-candidate definition.

A passing thalion candidate must:

    contain at least two states

    preserve one character

    remain connected

    have a nonempty boundary cut

    support an internal directed return path

Singleton bodies are rejected.

Bodies with only one-way internal motion are rejected.

In the current graph, the minimal thalion candidates contain two states
joined by reciprocal internal relations.

## Interpretation

A body may possess coherence, identity, and an outside without
supporting internal return.

A thalion requires the additional capacity to move internally and come
back without abandoning its preserved character.

## Consequence

The derivation stack now supports:

    motion graph

    state character field

    connected character-preserving body

    derived boundary

    internal directed return

    thalion candidate

The distinction between body and thalion is now executable.

## Limitation

The state character field remains supplied.

The return test detects a directed cycle but does not yet require a
signed cycle product or full cycle-space character.

A reciprocal two-state relation is sufficient in the current scaffold.

The result derives thalion candidates, not one uniquely selected native
thalion.

## Keeper

A body holds together.

A thalion moves within itself and returns.
