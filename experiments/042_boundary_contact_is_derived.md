# Experiment 042

## Title

Boundary Contact Is Derived

## Status

Executable candidate.

## Question

Can boundary contact be derived during execution from a registered
boundary object rather than stored directly on a transition rule?

## Starting Result

Experiment 041 separated step-local trace from path-earned return
receipt.

Step rules still carried boundary contacts as authored metadata.

## Construction

A motion rule now contains only:

    source state

    target state

    relation name

A boundary is registered separately with:

    boundary name

    inside states

    boundary-marked relations

For a motion rule and boundary, the system derives:

    whether the source is inside

    whether the target is inside

    whether the motion crosses the boundary

    whether the motion touches the boundary

Crossing occurs when source and target have different inside status.

Touching occurs when the motion crosses or uses a relation explicitly
marked by the boundary.

## Result

Inside-to-inside motion does not cross.

Inside-to-outside motion crosses.

Outside-to-inside motion crosses.

A marked relation can touch the boundary without crossing it.

Unmarked outside-to-outside motion has no contact.

Malformed boundaries are rejected.

## Interpretation

Boundary contact need not be authored onto each transition rule.

The motion rule describes lawful movement.

The boundary object determines how that movement reads relative to a
body or region.

## Consequence

The emerging execution chain is now:

    registered motion

    registered boundary

    executed relation

    derived boundary contact

    step event

    completed path receipt

This further separates motion law from environmental interpretation.

## Boundary

The boundary object is still authored directly.

Inside-state membership is explicit rather than derived from a graph
partition, connected region, or preserved character class.

Boundary-marked relations are also supplied.

The experiment derives contact for one boundary at a time.

It does not yet integrate the derived contact into the step event and
path receipt executor.

## Keeper

The rule says where motion may go.

The boundary says what that motion touches.
