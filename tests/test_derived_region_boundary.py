import unittest

from tm0.derived_boundary_contact import MotionRule
from tm0.derived_region_boundary import MotionGraph
from tm0.derived_region_boundary import derive_region_boundary
from tm0.derived_region_boundary import region_is_connected
from tm0.derived_region_boundary import validate_motion_graph


class TestDerivedRegionBoundary(unittest.TestCase):
    def setUp(self):
        self.graph = MotionGraph(
            states=("A", "B", "C", "D"),
            rules=(
                MotionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="ab",
                ),
                MotionRule(
                    source_state="B",
                    target_state="A",
                    relation_name="ba",
                ),
                MotionRule(
                    source_state="B",
                    target_state="C",
                    relation_name="bc",
                ),
                MotionRule(
                    source_state="C",
                    target_state="B",
                    relation_name="cb",
                ),
                MotionRule(
                    source_state="C",
                    target_state="D",
                    relation_name="cd",
                ),
                MotionRule(
                    source_state="D",
                    target_state="C",
                    relation_name="dc",
                ),
            ),
        )

    def test_graph_validates(self):
        self.assertEqual(
            validate_motion_graph(self.graph),
            self.graph,
        )

    def test_connected_region_is_accepted(self):
        self.assertTrue(
            region_is_connected(
                self.graph,
                ("A", "B"),
            )
        )

    def test_disconnected_region_is_rejected(self):
        self.assertFalse(
            region_is_connected(
                self.graph,
                ("A", "D"),
            )
        )

    def test_internal_relations_are_derived(self):
        boundary = derive_region_boundary(
            graph=self.graph,
            region_name="body-ab",
            region_states=("A", "B"),
        )

        self.assertEqual(
            boundary.internal_relations,
            ("ab", "ba"),
        )

    def test_outgoing_cut_relations_are_derived(self):
        boundary = derive_region_boundary(
            graph=self.graph,
            region_name="body-ab",
            region_states=("A", "B"),
        )

        self.assertEqual(
            boundary.outgoing_cut_relations,
            ("bc",),
        )

    def test_incoming_cut_relations_are_derived(self):
        boundary = derive_region_boundary(
            graph=self.graph,
            region_name="body-ab",
            region_states=("A", "B"),
        )

        self.assertEqual(
            boundary.incoming_cut_relations,
            ("cb",),
        )

    def test_boundary_relations_are_cut_union(self):
        boundary = derive_region_boundary(
            graph=self.graph,
            region_name="body-ab",
            region_states=("A", "B"),
        )

        self.assertEqual(
            boundary.boundary_relations,
            ("bc", "cb"),
        )

    def test_inside_states_are_normalized(self):
        boundary = derive_region_boundary(
            graph=self.graph,
            region_name="body-ab",
            region_states=("B", "A"),
        )

        self.assertEqual(
            boundary.inside_states,
            ("A", "B"),
        )

    def test_derived_boundary_converts_to_boundary_object(self):
        derived = derive_region_boundary(
            graph=self.graph,
            region_name="body-ab",
            region_states=("A", "B"),
        )

        boundary = derived.as_boundary()

        self.assertEqual(boundary.name, "body-ab")
        self.assertEqual(
            boundary.inside_states,
            ("A", "B"),
        )
        self.assertEqual(
            boundary.boundary_relations,
            ("bc", "cb"),
        )

    def test_single_state_region_is_connected(self):
        self.assertTrue(
            region_is_connected(
                self.graph,
                ("A",),
            )
        )

    def test_unknown_region_state_is_rejected(self):
        with self.assertRaises(ValueError):
            derive_region_boundary(
                graph=self.graph,
                region_name="bad",
                region_states=("A", "X"),
            )

    def test_duplicate_region_state_is_rejected(self):
        with self.assertRaises(ValueError):
            derive_region_boundary(
                graph=self.graph,
                region_name="bad",
                region_states=("A", "A"),
            )

    def test_disconnected_region_derivation_is_rejected(self):
        with self.assertRaises(ValueError):
            derive_region_boundary(
                graph=self.graph,
                region_name="bad",
                region_states=("A", "D"),
            )


if __name__ == "__main__":
    unittest.main()
