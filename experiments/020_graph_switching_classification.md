# Experiment 020

## Title

Graph Switching Classification

## Status

Executable candidate.

## Question

For one connected signed graph, are two sign assignments
switching-equivalent exactly when their fundamental-cycle signatures
agree?

## Starting Result

Experiment 019 established a spanning-tree normal form.

Every tree edge can be switched to:

    PRESERVE

The remaining chord signs count the independent cycles.

## Construction

For a fixed connected graph:

1. Choose a root.
2. Normalize the signed graph along a spanning tree.
3. Read the normalized signs on the chord edges.
4. Use that ordered chord-sign list as the switching signature.

Two sign assignments are declared switching-equivalent when their
signatures agree.

## Result

Equivalent signings produced the same chord-sign signature.

Changing one independent cycle sign changed the signature and broke
equivalence.

The signature length matched the cycle rank.

The tested equivalence result did not depend on the selected root.

## Interpretation

For the tested connected graph, the complete switching-invariant
character is a bit vector of length:

    edge count - vertex count + 1

Each bit records one independent cycle return sign.

## Consequence

The one-cycle result now extends to a connected graph in the tested
normal form.

Local edge-sign detail reduces to cycle-space return character.

## Boundary

This experiment tests one finite connected graph family.

It does not yet provide a general proof for every connected graph.

It does not derive the graph, local signs, witness, character update,
or thalion.

## Keeper

A connected graph remembers its signed return character in cycle
space.
