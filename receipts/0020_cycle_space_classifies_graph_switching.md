# Receipt 0020

## Title

Cycle Space Classifies Graph Switching

## Status

Research receipt.

## Result

For the tested connected signed graph, local switching reduces the
edge-sign assignment to an ordered chord-sign signature.

The signature length is:

    edge count - vertex count + 1

This is the cycle rank.

Two tested sign assignments are switching-equivalent exactly when
their chord-sign signatures agree.

## Interpretation

Local edge signs contain gauge-like redundancy.

The switching-invariant content lives in cycle space.

Each independent cycle contributes one return bit:

    +1 = SAME

    -1 = POLAR

## Root Independence

The tested equivalence result remained unchanged when the spanning-tree
root changed.

The normal-form coordinates may change with the chosen tree or root.

The switching class does not.

## Consequence

A connected signed graph carries a cycle-space character vector.

This extends the one-cycle result:

    one cycle -> one invariant bit

to:

    cycle rank beta_1 -> beta_1 invariant bits

## Limitation

This is an executable result on the tested finite graph.

It is not yet a general theorem for every connected graph.

It does not derive the graph, local signs, realization law, witness,
character update, or thalion.

## Keeper

Local signs describe the reading.

Cycle space keeps the return character.
