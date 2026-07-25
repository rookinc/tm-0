"""Derive a compact character from a fundamental cycle basis.

The directed motion rules are treated as distinct undirected edges for
the purpose of cycle-space construction.

A deterministic spanning forest is built from relation-name order.

Each non-tree relation closes one fundamental cycle with the unique
tree path between its endpoints.

The fundamental cycles form independent cycle coordinates.

A state's binary character records participation in each basis cycle.

This is a bounded cycle-basis scaffold for small motion graphs.
"""

from dataclasses import dataclass
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

from .derived_body_candidate import StateCharacterMap
from .derived_boundary_contact import MotionRule
from .derived_region_boundary import MotionGraph
from .derived_region_boundary import validate_motion_graph


StateName = str
RelationName = str


@dataclass(frozen=True)
class FundamentalCycle:
    states: Tuple[StateName, ...]
    tree_relations: Tuple[RelationName, ...]
    closing_relation: RelationName

    @property
    def relations(self) -> Tuple[RelationName, ...]:
        return (
            *self.tree_relations,
            self.closing_relation,
        )

    @property
    def length(self) -> int:
        return len(self.relations)


@dataclass(frozen=True)
class SpanningForest:
    tree_relations: Tuple[RelationName, ...]
    non_tree_relations: Tuple[RelationName, ...]
    component_count: int


def sorted_rules(
    graph: MotionGraph,
) -> Tuple[MotionRule, ...]:
    validate_motion_graph(graph)

    return tuple(
        sorted(
            graph.rules,
            key=lambda rule: (
                rule.relation_name,
                rule.source_state,
                rule.target_state,
            ),
        )
    )


def derive_spanning_forest(
    graph: MotionGraph,
) -> SpanningForest:
    validate_motion_graph(graph)

    parent = {
        state: state
        for state in graph.states
    }

    rank = {
        state: 0
        for state in graph.states
    }

    def find(state: StateName) -> StateName:
        while parent[state] != state:
            parent[state] = parent[parent[state]]
            state = parent[state]

        return state

    def union(
        left: StateName,
        right: StateName,
    ) -> bool:
        left_root = find(left)
        right_root = find(right)

        if left_root == right_root:
            return False

        if rank[left_root] < rank[right_root]:
            left_root, right_root = right_root, left_root

        parent[right_root] = left_root

        if rank[left_root] == rank[right_root]:
            rank[left_root] += 1

        return True

    tree_relations = []
    non_tree_relations = []

    for rule in sorted_rules(graph):
        if union(
            rule.source_state,
            rule.target_state,
        ):
            tree_relations.append(
                rule.relation_name
            )
        else:
            non_tree_relations.append(
                rule.relation_name
            )

    component_count = len(
        {
            find(state)
            for state in graph.states
        }
    )

    return SpanningForest(
        tree_relations=tuple(tree_relations),
        non_tree_relations=tuple(non_tree_relations),
        component_count=component_count,
    )


def rule_map(
    graph: MotionGraph,
) -> Dict[RelationName, MotionRule]:
    validate_motion_graph(graph)

    return {
        rule.relation_name: rule
        for rule in graph.rules
    }


def tree_adjacency(
    graph: MotionGraph,
    forest: SpanningForest,
):
    rules = rule_map(graph)

    adjacency = {
        state: []
        for state in graph.states
    }

    for relation_name in forest.tree_relations:
        rule = rules[relation_name]

        adjacency[rule.source_state].append(
            (
                rule.target_state,
                relation_name,
            )
        )

        adjacency[rule.target_state].append(
            (
                rule.source_state,
                relation_name,
            )
        )

    return {
        state: tuple(
            sorted(
                neighbors,
                key=lambda item: (
                    item[1],
                    item[0],
                ),
            )
        )
        for state, neighbors in adjacency.items()
    }


def find_tree_path(
    graph: MotionGraph,
    forest: SpanningForest,
    source_state: StateName,
    target_state: StateName,
) -> Tuple[
    Tuple[StateName, ...],
    Tuple[RelationName, ...],
]:
    adjacency = tree_adjacency(
        graph,
        forest,
    )

    frontier = [
        (
            source_state,
            (source_state,),
            (),
        )
    ]

    visited: Set[StateName] = {
        source_state
    }

    while frontier:
        current, states, relations = frontier.pop(0)

        if current == target_state:
            return states, relations

        for neighbor, relation_name in adjacency[current]:
            if neighbor in visited:
                continue

            visited.add(neighbor)

            frontier.append(
                (
                    neighbor,
                    (
                        *states,
                        neighbor,
                    ),
                    (
                        *relations,
                        relation_name,
                    ),
                )
            )

    raise ValueError(
        "tree path does not exist between relation endpoints"
    )


def derive_fundamental_cycles(
    graph: MotionGraph,
) -> Tuple[FundamentalCycle, ...]:
    forest = derive_spanning_forest(graph)
    rules = rule_map(graph)
    cycles: List[FundamentalCycle] = []

    for relation_name in forest.non_tree_relations:
        closing_rule = rules[relation_name]

        states, tree_relations = find_tree_path(
            graph=graph,
            forest=forest,
            source_state=closing_rule.source_state,
            target_state=closing_rule.target_state,
        )

        cycles.append(
            FundamentalCycle(
                states=states,
                tree_relations=tree_relations,
                closing_relation=relation_name,
            )
        )

    return tuple(cycles)


def undirected_cycle_rank(
    graph: MotionGraph,
) -> int:
    forest = derive_spanning_forest(graph)

    return (
        len(graph.rules)
        - len(graph.states)
        + forest.component_count
    )


def derive_fundamental_cycle_character_field(
    graph: MotionGraph,
) -> StateCharacterMap:
    cycles = derive_fundamental_cycles(graph)

    if not cycles:
        raise ValueError(
            "motion graph has zero undirected cycle rank"
        )

    field: StateCharacterMap = {}

    for state in graph.states:
        field[state] = tuple(
            int(state in cycle.states)
            for cycle in cycles
        )

    return field


def states_without_basis_cycle_participation(
    graph: MotionGraph,
) -> Tuple[StateName, ...]:
    field = derive_fundamental_cycle_character_field(
        graph
    )

    return tuple(
        sorted(
            state
            for state, character in field.items()
            if not any(character)
        )
    )
