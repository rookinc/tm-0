# Receipt 0042

## Title

The Boundary Interprets Motion

## Status

Research receipt.

## Result

Boundary contact can be derived from a motion rule and a separately
registered boundary object.

A motion rule contains only:

    source state

    target state

    relation name

The boundary determines:

    source inside status

    target inside status

    crossing

    touching

Inside-to-outside and outside-to-inside motion cross the boundary.

A boundary-marked relation can touch without crossing.

Unmarked outside motion can remain unrelated to the boundary.

## Interpretation

Motion law and boundary interpretation are distinct.

The transition rule says which motion is lawful.

The boundary says how that motion reads relative to a body or region.

## Consequence

TM-0 now supports:

    registered motion

    registered boundary

    derived boundary contact

    step-local trace

    path-earned return receipt

Boundary contact no longer needs to be copied onto each motion rule.

## Limitation

The boundary object remains authored directly.

Inside-state membership and boundary-marked relations are supplied.

Contact is derived for one boundary at a time.

The derived contact is not yet emitted by the step executor.

## Keeper

Motion does not carry its boundary meaning alone.

The boundary gives motion its contact.
