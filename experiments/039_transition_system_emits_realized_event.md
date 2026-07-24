# Experiment 039

## Title

A Transition System Emits the Realized Event

## Status

Executable candidate.

## Question

Can a minimal transition system execute a lawful step and emit the
realized event record required by the witness-context layer?

## Starting Result

Experiment 038 reconstructed context from a realized event.

The event record was still supplied directly.

## Construction

A minimal transition system contains:

    registered states

    directed transition rules

Each rule records:

    source state

    target state

    relation name

    boundary contacts

    cycle residue

Execution begins from a current state and requests a named relation.

The step succeeds only when:

    the current state is registered

    the relation is registered

    the relation begins at the current state

A successful step returns:

    prior state

    next state

    selected rule

    realized event

## Result

A lawful transition executes.

Execution changes the current state according to the selected rule.

The transition emits a realized event containing the source, target,
relation, boundary contacts, and cycle residue.

A return transition can execute from the returned state.

Unknown states, unknown relations, and relations requested from the
wrong source state are rejected.

Malformed transition systems are rejected.

## Interpretation

The realized event can be produced by execution rather than prepared
as a separate input.

The transition rule supplies the lawful possibility.

Execution selects and realizes one permitted possibility.

The resulting trace can feed the context and witness layers.

## Consequence

The operational sequence is now:

    registered transition system

    current state

    requested lawful relation

    executed step

    realized event

    derived structural context

    context-specific reliability

    weighted arbitration

## Boundary

The transition rules are still authored directly.

Boundary contacts and cycle residue are stored on the rule rather than
derived from graph traversal or completed return.

The executor handles one step at a time.

It does not yet accumulate a path, detect closure, or compute cycle
residue from execution history.

## Keeper

Lawful possibility becomes an event when a permitted relation is
executed.
