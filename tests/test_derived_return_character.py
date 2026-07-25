import unittest

from tm0.derived_boundary_contact import MotionRule
from tm0.derived_region_boundary import MotionGraph
from tm0.derived_return_character import derive_return_character_field
from tm0.derived_return_character import derive_return_classes
from tm0.derived_return_character import directed_adjacency
from tm0.derived_return_character import reverse_directed_adjacency


class TestDerivedReturnCharacter(unittest.TestCase):
    def setUp(self):
        self.graph = MotionGraph(
            states=("A", "B", "C", "D", "E"),
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
                    target_state="D",
                    relation_name="cd",
                ),
                MotionRule(
                    source_state="D",
                    target_state="C",
                    relation_name="dc",
                ),
                MotionRule(
                    source_state="D",
                    target_state="E",
                    relation_name="de",
                ),
            ),
        )

    def test_directed_adjacency_is_derived(self):
        adjacency = directed_adjacency(self.graph)

        self.assertEqual(adjacency["A"], ("B",))
        self.assertEqual(adjacency["B"], ("A", "C"))
        self.assertEqual(adjacency["E"], ())

    def test_reverse_adjacency_is_derived(self):
        adjacency = reverse_directed_adjacency(
            self.graph
        )

        self.assertEqual(adjacency["A"], ("B",))
        self.assertEqual(adjacency["C"], ("B", "D"))
        self.assertEqual(adjacency["E"], ("D",))

    def test_return_classes_are_strong_components(self):
        classes = derive_return_classes(self.graph)

        self.assertEqual(
            classes,
            (
                ("A", "B"),
                ("C", "D"),
                ("E",),
            ),
        )

    def test_same_return_class_gets_same_character(self):
        field = derive_return_character_field(
            self.graph
        )

        self.assertEqual(field["A"], field["B"])
        self.assertEqual(field["C"], field["D"])

    def test_different_return_classes_get_different_character(self):
        field = derive_return_character_field(
            self.graph
        )

        self.assertNotEqual(field["A"], field["C"])
        self.assertNotEqual(field["C"], field["E"])
        self.assertNotEqual(field["A"], field["E"])

    def test_characters_are_canonical_one_hot_values(self):
        field = derive_return_character_field(
            self.graph
        )

        self.assertEqual(field["A"], (1, 0, 0))
        self.assertEqual(field["B"], (1, 0, 0))
        self.assertEqual(field["C"], (0, 1, 0))
        self.assertEqual(field["D"], (0, 1, 0))
        self.assertEqual(field["E"], (0, 0, 1))

    def test_character_field_covers_all_states(self):
        field = derive_return_character_field(
            self.graph
        )

        self.assertEqual(
            set(field),
            set(self.graph.states),
        )

    def test_single_return_class_gets_one_bit_character(self):
        graph = MotionGraph(
            states=("A", "B"),
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
            ),
        )

        field = derive_return_character_field(graph)

        self.assertEqual(field["A"], (1,))
        self.assertEqual(field["B"], (1,))

    def test_one_way_pair_forms_two_return_classes(self):
        graph = MotionGraph(
            states=("A", "B"),
            rules=(
                MotionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="ab",
                ),
            ),
        )

        self.assertEqual(
            derive_return_classes(graph),
            (
                ("A",),
                ("B",),
            ),
        )


if __name__ == "__main__":
    unittest.main()
