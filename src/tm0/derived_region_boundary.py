"""Derive a boundary from a connected region of a motion graph.

The motion graph supplies:

    registered states
    directed motion rules

A selected region supplies only a set of states.

From those inputs, the system derives:

    internal relations
    outgoing cut relations
    incoming cut relations
    all boundary relations

The selected region must be connected in the underlying undirected
motion graph.

This is a bounded graph-derived boundary scaffold.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Set
from typing import Tuple

from .derived_boundary_contact import Boundary
from .derived_boundary_contact import MotionRule
from .derived_boundary_contact import validate_motion_rule


StateName = str
RelationName = str
RegionStates = Tuple[StateName, ...]


@dataclass(frozen=True)
class MotionGraph:
    states: Tuple[StateName, ...]
    rules: Tuple[MotionRule, ...]


@dataclass(frozen=True)
class DerivedRegionBoundary:
    region_name: str
    inside_states: RegionStates
    internal_relations: Tuple[RelationName, ...]
    outgoing_cut_relations: Tuple[RelationName, ...]
    incoming_cut_relations: Tuple[RelationName, ...]
    boundary_relations: Tuple[RelationName, ...]

    def as_boundary(self) -> Boundary:
        return Boundary(
            name=self.region_name,
            inside_states=self.inside_states,
            boundary_relations=self.boundary_relations,
        )


def validate_motion_graph(
    graph: MotionGraph,
) -> MotionGraph:
    if not graph.states:
        raise ValueError("motion graph must contain states")

    if any(not state for state in graph.states):
        raise ValueError("state names must not be empty")

    if len(set(graph.states)) != len(graph.states):
        raise ValueError("state names must be unique")

    if not graph.rules:
        raise ValueError("motion graph must contain rules")

    relation_names = tuple(
        rule.relation_name
        for rule in graph.rules
    )

    if len(set(relation_names)) != len(relation_names):
        raise ValueError("relation names must be unique")

    known_states = set(graph.states)

    for rule in graph.rules:
        validate_motion_rule(rule)

        if rule.source_state not in known_states:
            raise ValueError("rule source state is not registered")

        if rule.target_state not in known_states:
            raise ValueError("rule target state is not registered")

    return graph


def undirected_adjacency(
    graph: MotionGraph,
) -> Dict[StateName, Set[StateName]]:
    validate_motion_graph(graph)

    adjacency = {
        state: set()
        for state in graph.states
    }

    for rule in graph.rules:
        adjacency[rule.source_state].add(
            rule.target_state
        )
        adjacency[rule.target_state].add(
            rule.source_state
        )

    return adjacency


def region_is_connected(
    graph: MotionGraph,
    region_states: RegionStates,
) -> bool:
    validate_motion_graph(graph)

    if not region_states:
        return False

    region = set(region_states)

    if len(region) != len(region_states):
        return False

    if not region.issubset(set(graph.states)):
        return False

    adjacency = undirected_adjacency(graph)

    start = region_states[0]
    frontier = [start]
    visited = {start}

    while frontier:
        current = frontier.pop()

        for neighbor in adjacency[current]:
            if neighbor in region and neighbor not in visited:
                visited.add(neighbor)
                frontier.append(neighbor)

    return visited == region


def derive_region_boundary(
    graph: MotionGraph,
    region_name: str,
    region_states: RegionStates,
) -> DerivedRegionBoundary:
    validate_motion_graph(graph)

    if not region_name:
        raise ValueError("region name must not be empty")

    if not region_states:
        raise ValueError("region must contain states")

    if len(set(region_states)) != len(region_states):
        raise ValueError("region states must be unique")

    unknown_states = set(region_states) - set(graph.states)

    if unknown_states:
        raise ValueError("region contains unregistered states")

    if not region_is_connected(
        graph,
        region_states,
    ):
        raise ValueError("region must be connected")

    inside = set(region_states)

    internal = []
    outgoing = []
    incoming = []

    for rule in graph.rules:
        source_inside = rule.source_state in inside
        target_inside = rule.target_state in inside

        if source_inside and target_inside:
            internal.append(rule.relation_name)
        elif source_inside and not target_inside:
            outgoing.append(rule.relation_name)
        elif not source_inside and target_inside:
            incoming.append(rule.relation_name)

    boundary_relations = tuple(
        sorted(
            set(outgoing)
            | set(incoming)
        )
    )

    return DerivedRegionBoundary(
        region_name=region_name,
        inside_states=tuple(sorted(region_states)),
        internal_relations=tuple(sorted(internal)),
        outgoing_cut_relations=tuple(sorted(outgoing)),
        incoming_cut_relations=tuple(sorted(incoming)),
        boundary_relations=boundary_relations,
    )
