# Experiment 019

## Title

Graph Cycle Rank Switching Normal Form

## Status

Executable candidate.

## Question

For a connected signed graph, does local switching reduce the sign
assignment to one invariant sign per independent cycle?

## Starting Result

Experiment 018 established that one connected cycle retains exactly
one switching-invariant return bit.

Experiment 019 extends the question to several cycles sharing
junctions.

## Construction

A connected signed graph is normalized by choosing a spanning tree.

Local vertex switches are selected so that every spanning-tree edge
becomes:

    PRESERVE

The edges outside the spanning tree are chords.

Their normalized signs remain.

## Tested Cases

A tree:

    all edges normalize to PRESERVE

    chord count = 0

One independent cycle:

    chord count = 1

Two independent cycles:

    chord count = 2

For a connected graph:

    chord count = edge count - vertex count + 1

## Result

All focused tests passed.

The normalization removes sign information from every spanning-tree
edge.

The remaining sign data lives on the chord edges.

The number of chord signs equals the cycle rank.

## Interpretation

A connected signed graph carries one switching-invariant return bit
per independent cycle in the tested normal form.

The graph has now emerged as the minimal incidence ledger for several
closed relations sharing junctions.

Vertices arise as junctions.

Edges arise as relation occurrences.

Cycle-space signs arise as invariant return receipts.

## Boundary

This experiment does not yet prove that the chord signs completely
classify switching classes on arbitrary connected graphs.

It does not derive the graph from an executable growth process.

It does not derive local signs, character accumulation, witness, or a
thalion.

## Keeper

A tree carries no closed return bit.

Each independent closure leaves one sign behind.
