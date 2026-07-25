"""Derive boundary contact from a registered boundary object.

A transition rule now contains only lawful motion:

    source state
    target state
    relation name

Boundary structure is registered separately.

During execution, the system derives whether the transition touches or
crosses the boundary.

This is a bounded boundary-contact scaffold.
"""

from dataclasses import dataclass
from typing import Tuple


StateName = str
RelationName = str
BoundaryName = str


@dataclass(frozen=True)
class MotionRule:
    source_state: StateName
    target_state: StateName
    relation_name: RelationName


@dataclass(frozen=True)
class Boundary:
    name: BoundaryName
    inside_states: Tuple[StateName, ...]
    boundary_relations: Tuple[RelationName, ...]


@dataclass(frozen=True)
class BoundaryContact:
    boundary_name: BoundaryName
    relation_name: RelationName
    source_inside: bool
    target_inside: bool
    touches_boundary: bool
    crosses_boundary: bool


def validate_motion_rule(
    rule: MotionRule,
) -> MotionRule:
    if not rule.source_state:
        raise ValueError("source state must not be empty")

    if not rule.target_state:
        raise ValueError("target state must not be empty")

    if not rule.relation_name:
        raise ValueError("relation name must not be empty")

    return rule


def validate_boundary(
    boundary: Boundary,
) -> Boundary:
    if not boundary.name:
        raise ValueError("boundary name must not be empty")

    if not boundary.inside_states:
        raise ValueError("boundary must contain inside states")

    if any(not state for state in boundary.inside_states):
        raise ValueError("inside state names must not be empty")

    if len(set(boundary.inside_states)) != len(
        boundary.inside_states
    ):
        raise ValueError("inside states must be unique")

    if any(not relation for relation in boundary.boundary_relations):
        raise ValueError("boundary relation names must not be empty")

    if len(set(boundary.boundary_relations)) != len(
        boundary.boundary_relations
    ):
        raise ValueError("boundary relations must be unique")

    return boundary


def derive_boundary_contact(
    rule: MotionRule,
    boundary: Boundary,
) -> BoundaryContact:
    validate_motion_rule(rule)
    validate_boundary(boundary)

    source_inside = rule.source_state in boundary.inside_states
    target_inside = rule.target_state in boundary.inside_states

    relation_marks_boundary = (
        rule.relation_name in boundary.boundary_relations
    )

    crosses_boundary = source_inside != target_inside

    touches_boundary = (
        relation_marks_boundary
        or crosses_boundary
    )

    return BoundaryContact(
        boundary_name=boundary.name,
        relation_name=rule.relation_name,
        source_inside=source_inside,
        target_inside=target_inside,
        touches_boundary=touches_boundary,
        crosses_boundary=crosses_boundary,
    )
