# Receipt 0044

## Title

The Graph Reveals the Region Boundary

## Status

Research receipt.

## Result

A boundary object can be derived from a connected state region of the
motion graph.

Given:

    registered states

    directed motion rules

    selected region states

the system derives:

    internal relations

    outgoing cut relations

    incoming cut relations

    boundary relations

Boundary relations are the union of incoming and outgoing cuts.

Disconnected, duplicate, and unknown region-state selections are
rejected.

## Interpretation

The region does not need an independently authored list of boundary
relations.

Once the region is selected, endpoint incidence in the motion graph
reveals where the region ends.

## Consequence

The boundary construction now supports:

    motion graph

    selected connected region

    derived graph cut

    derived boundary object

    runtime-derived contact

    boundary-aware execution

This removes authored boundary relations from the active construction.

## Limitation

The region-state set remains externally selected.

The system does not yet derive which connected region should count as a
body.

Connectivity is evaluated in the underlying undirected motion graph.

The motion graph itself remains supplied.

Region-boundary derivation is not yet integrated into the active
executor constructor.

## Keeper

The region supplies membership.

The graph supplies the edge of the region.
