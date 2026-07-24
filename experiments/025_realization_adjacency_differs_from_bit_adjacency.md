# Experiment 025

## Title

Realization Adjacency Differs From Bit Adjacency

## Status

Executable candidate.

## Question

Is adjacency in character space the same as reachability by one local
realization?

## Starting Result

Experiment 024 defined character adjacency as:

    exactly one cycle-space bit differs

That made adjacency derivable from minimal character distance.

Experiment 021 showed that one local edge-sign realization may change
several cycle-space bits.

## Construction

Two adjacency notions are compared.

Character adjacency:

    one cycle-space bit differs

Realization adjacency:

    one actual local edge-sign flip reaches the target character

## Result

A chord-edge flip can be both:

    character adjacent

    realization adjacent

A tree-edge flip can be:

    not character adjacent

    realization adjacent

because one local edge may participate in several independent cycles.

The current character state is adjacent to neither itself.

## Interpretation

Hamming distance one in cycle space is not the general law of one-step
reachability.

The true neighbourhood is induced by the available local
realizations.

Character distance is a useful coordinate description.

Realization adjacency is the mechanical relation.

## Consequence

Boundary should be built from reachable transitions, not from abstract
bit distance alone.

The possibility address space inherits adjacency from the realization
operators currently available.

## Boundary

This experiment assumes that every local edge-sign flip is an
available realization.

It does not yet derive admissibility restrictions on those flips.

It does not introduce resolution, selection, probability, agency,
time, energy, or physical motion.

## Keeper

One local act may move several character bits.

Reachability, not bit distance, defines the next address.
