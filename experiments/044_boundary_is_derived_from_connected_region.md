# Experiment 044

## Title

Boundary Is Derived from a Connected Region

## Status

Executable candidate.

## Question

Can a boundary object be derived from a connected state region of the
motion graph rather than authored separately?

## Starting Result

Experiment 043 integrated runtime-derived boundary contact into active
execution.

The boundary object still supplied:

    inside states

    boundary relations

directly.

## Construction

A motion graph contains:

    registered states

    directed motion rules

A candidate region supplies only:

    region name

    selected states

The selected states must form a connected region in the underlying
undirected motion graph.

From the graph and region, the system derives:

    internal relations

    outgoing cut relations

    incoming cut relations

    boundary relations

Internal relations have both endpoints inside the region.

Outgoing cut relations begin inside and end outside.

Incoming cut relations begin outside and end inside.

Boundary relations are the union of incoming and outgoing cuts.

## Result

Connected regions are accepted.

Disconnected regions are rejected.

Internal relations are derived from endpoint membership.

Incoming and outgoing cut relations are derived separately.

Their union becomes the boundary-relation set.

Region-state order is normalized.

The derived structure converts directly into the boundary object used
by the boundary-aware executor.

Unknown and duplicate region states are rejected.

## Interpretation

A region does not need its boundary relations listed independently.

Once a connected state region is selected, the motion graph determines
which relations remain internal and which relations cross its cut.

The graph therefore supplies the relational surface of the region.

## Consequence

The boundary chain is now:

    registered motion graph

    selected connected region

    derived internal relations

    derived cut relations

    derived boundary object

    runtime-derived contact

    boundary-aware execution

This removes authored boundary relations from the active construction.

## Boundary

The region-state set is still selected externally.

The experiment does not yet derive which connected region should count
as a body.

Connectivity is evaluated in the underlying undirected motion graph.

The graph remains supplied directly.

The experiment does not yet integrate region-boundary derivation into
the boundary-aware executor constructor.

## Keeper

Select the region.

The graph reveals its boundary.
