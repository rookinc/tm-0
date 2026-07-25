# Experiment 046

## Title

A Thalion Is a Nontrivial Returning Body

## Status

Executable candidate.

## Question

Can TM-0 derive thalion candidates by adding nontrivial internal return
to the body-candidate definition?

## Starting Result

Experiment 045 derived body candidates as connected
character-preserving regions with nonempty boundary cuts.

Singleton regions qualified as minimal body candidates.

A singleton cannot support a nontrivial internal return path.

## Construction

A thalion candidate begins as a valid body candidate.

It must additionally:

    contain at least two states

    contain an internal directed return path

The return path must:

    remain within the body states

    use internal motion rules

    begin and end at the same state

The system searches internal directed relations for such a path.

It then enumerates all body candidates and retains only those that pass
the return test.

## Result

Two-state bodies with reciprocal internal relations become thalion
candidates.

Singleton bodies are rejected.

Two-state bodies with only one-way internal motion are rejected.

Mixed-character regions never become thalion candidates because they
fail the body test first.

The minimal passing candidates in the current graph contain exactly two
states.

Each candidate carries:

    body structure

    preserved character

    derived boundary

    internal return-state path

    internal return-relation path

## Interpretation

A body can be coherent and bounded without supporting return.

A thalion candidate requires more.

It must preserve identity while admitting nontrivial internal motion
that comes back.

## Consequence

The derivation chain is now:

    motion graph

    state character field

    connected character-preserving body

    nonempty boundary cut

    nontrivial internal return

    thalion candidate

This makes the distinction executable:

    body candidate

is not automatically:

    thalion candidate

## Boundary

The state character field remains supplied.

The return test detects a directed cycle but does not yet require a
particular cycle-space character or signed residue.

A reciprocal two-state relation is sufficient in the current scaffold.

The exhaustive search is intended only for small graphs.

The result defines thalion candidates, not a unique native thalion.

## Keeper

A body holds together.

A thalion can move within itself and return.
