# Receipt 0043

## Title

Execution Joins Motion and Boundary

## Status

Research receipt.

## Result

The active executor now derives boundary contact at runtime.

A motion rule contains only:

    source state

    target state

    relation name

A separately registered boundary contributes:

    inside-state membership

    boundary-marked relations

Execution joins the rule and boundary to emit a boundary-aware step
event.

Internal motion can produce no contact.

Entry and exit motion produce crossings.

A marked internal relation can produce touching without crossing.

A completed path preserves the derived contacts in execution order.

## Interpretation

Lawful motion and boundary meaning remain distinct until execution.

The rule determines where motion may occur.

The boundary determines how that motion reads relative to the region.

The event carries the result of their encounter.

## Consequence

TM-0 now supports:

    registered motion

    registered boundary

    runtime-derived contact

    boundary-aware step trace

    path-earned return receipt

No authored contact field is required on the active motion rule.

## Limitation

The current system registers one boundary.

The boundary object remains authored directly.

Inside-state membership and boundary-marked relations are supplied.

Traversal residue remains relation parity.

The path request sequence remains externally supplied.

## Keeper

The rule supplies motion.

The boundary supplies meaning.

Execution joins them in trace.
