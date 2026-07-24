# Receipt 0019

## Title

Cycle Rank Counts Return Bits

## Status

Research receipt.

## Result

A connected signed graph can be switched into a normal form where:

    every spanning-tree edge is PRESERVE

    every remaining chord carries one residual sign

The number of chord signs is:

    edge count - vertex count + 1

This is the cycle rank of a connected graph.

## Interpretation

A tree carries no switching-invariant return sign.

Each independent cycle contributes one residual sign in the tested
normal form.

The signed graph therefore compresses to:

    incidence structure

    plus one return bit per independent cycle

## Emergence

The graph was not assumed at the start of TM-0.

It appeared when the earned mechanics required:

    several relation occurrences

    shared junctions

    composition

    multiple independent closures

Vertices are junction classes.

Edges are relation occurrences.

Cycle signs are invariant return receipts.

## Limitation

The experiment has not yet proved complete switching classification
for every connected graph.

It has established a spanning-tree normal form and the correct count
of residual chord signs.

## Consequence

The next question is whether two signed assignments on the same
connected graph are switching-equivalent exactly when their
fundamental-cycle return signs agree.

## Keeper

A tree remembers no return.

Each independent closure leaves one bit.
