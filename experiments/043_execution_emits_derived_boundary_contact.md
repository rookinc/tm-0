# Experiment 043

## Title

Execution Emits Derived Boundary Contact

## Status

Executable candidate.

## Question

Can the active executor derive boundary contact at runtime and emit it
as part of the realized step event?

## Starting Result

Experiment 042 derived boundary contact from a motion rule and a
separately registered boundary.

That derivation was not yet integrated into path execution.

## Construction

A boundary-aware system contains:

    registered states

    motion rules

    one registered boundary

Motion rules contain only:

    source state

    target state

    relation name

Execution performs:

    rule lookup

    source-state validation

    boundary-contact derivation

    boundary-aware step emission

The step event contains:

    source state

    target state

    traversed relation

    derived boundary contact

The path executor accumulates those step events and derives:

    visited states

    traversed relations

    return status

    traversal residue

## Result

Motion rules no longer carry authored boundary-contact fields.

Internal motion can derive no contact.

Exit and entry motion derive boundary crossings.

A boundary-marked internal relation can derive touching without
crossing.

A completed path accumulates the derived contacts in execution order.

Return status and traversal residue remain path-earned.

Systems with unknown boundary states or relations are rejected.

## Interpretation

Boundary meaning can now enter the active execution trace at runtime.

The rule contributes lawful movement.

The boundary contributes interpretation.

The executor joins them into a realized event.

## Consequence

The active execution chain is now:

    registered motion

    registered boundary

    lawful execution

    runtime-derived contact

    boundary-aware step event

    completed path receipt

No authored contact field is required on the motion rule.

## Boundary

The system currently registers one boundary.

The boundary object remains authored directly.

Inside-state membership and boundary-marked relations are supplied.

Traversal residue remains relation parity rather than a signed cycle
product or full cycle-space character.

The path request sequence remains externally supplied.

## Keeper

Execution realizes motion.

The boundary makes contact visible in the trace.
