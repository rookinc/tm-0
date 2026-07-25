import unittest

from tm0.derived_body_candidate import derive_body_candidate
from tm0.derived_body_candidate import enumerate_body_candidates
from tm0.derived_body_candidate import minimal_body_candidates
from tm0.derived_body_candidate import region_character
from tm0.derived_body_candidate import validate_state_characters
from tm0.derived_boundary_contact import MotionRule
from tm0.derived_region_boundary import MotionGraph


class TestDerivedBodyCandidate(unittest.TestCase):
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

        self.characters = {
            "A": (0,),
            "B": (0,),
            "C": (1,),
            "D": (1,),
        }

    def test_character_map_validates(self):
        self.assertEqual(
            validate_state_characters(
                self.graph,
                self.characters,
            ),
            self.characters,
        )

    def test_connected_preserved_region_becomes_body(self):
        candidate = derive_body_candidate(
            graph=self.graph,
            region_states=("A", "B"),
            state_characters=self.characters,
            region_name="body-ab",
        )

        self.assertEqual(
            candidate.states,
            ("A", "B"),
        )
        self.assertEqual(
            candidate.character,
            (0,),
        )
        self.assertEqual(
            candidate.boundary.boundary_relations,
            ("bc", "cb"),
        )

    def test_second_character_region_becomes_body(self):
        candidate = derive_body_candidate(
            graph=self.graph,
            region_states=("C", "D"),
            state_characters=self.characters,
            region_name="body-cd",
        )

        self.assertEqual(
            candidate.states,
            ("C", "D"),
        )
        self.assertEqual(
            candidate.character,
            (1,),
        )
        self.assertEqual(
            candidate.boundary.boundary_relations,
            ("bc", "cb"),
        )

    def test_mixed_character_region_is_rejected(self):
        with self.assertRaises(ValueError):
            derive_body_candidate(
                graph=self.graph,
                region_states=("B", "C"),
                state_characters=self.characters,
            )

    def test_disconnected_region_is_rejected(self):
        with self.assertRaises(ValueError):
            derive_body_candidate(
                graph=self.graph,
                region_states=("A", "D"),
                state_characters=self.characters,
            )

    def test_whole_graph_is_rejected_without_boundary(self):
        with self.assertRaises(ValueError):
            derive_body_candidate(
                graph=self.graph,
                region_states=("A", "B", "C", "D"),
                state_characters=self.characters,
            )

    def test_region_character_is_preserved_value(self):
        self.assertEqual(
            region_character(
                ("A", "B"),
                self.characters,
            ),
            (0,),
        )

    def test_region_character_rejects_mixed_values(self):
        with self.assertRaises(ValueError):
            region_character(
                ("B", "C"),
                self.characters,
            )

    def test_enumeration_finds_character_regions(self):
        candidates = enumerate_body_candidates(
            self.graph,
            self.characters,
        )

        state_sets = {
            candidate.states
            for candidate in candidates
        }

        self.assertIn(("A", "B"), state_sets)
        self.assertIn(("C", "D"), state_sets)
        self.assertNotIn(("B", "C"), state_sets)

    def test_minimal_candidates_are_singletons(self):
        candidates = minimal_body_candidates(
            self.graph,
            self.characters,
        )

        self.assertEqual(
            {
                candidate.states
                for candidate in candidates
            },
            {
                ("A",),
                ("B",),
                ("C",),
                ("D",),
            },
        )

    def test_missing_character_state_is_rejected(self):
        characters = {
            "A": (0,),
            "B": (0,),
            "C": (1,),
        }

        with self.assertRaises(ValueError):
            validate_state_characters(
                self.graph,
                characters,
            )

    def test_nonbinary_character_is_rejected(self):
        characters = {
            "A": (0,),
            "B": (0,),
            "C": (2,),
            "D": (1,),
        }

        with self.assertRaises(ValueError):
            validate_state_characters(
                self.graph,
                characters,
            )

    def test_character_lengths_must_match(self):
        characters = {
            "A": (0,),
            "B": (0,),
            "C": (1, 0),
            "D": (1, 0),
        }

        with self.assertRaises(ValueError):
            validate_state_characters(
                self.graph,
                characters,
            )


if __name__ == "__main__":
    unittest.main()
