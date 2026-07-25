import unittest

from tm0.derived_body_candidate import derive_body_candidate
from tm0.derived_boundary_contact import MotionRule
from tm0.derived_region_boundary import MotionGraph
from tm0.derived_thalion_candidate import derive_thalion_candidate
from tm0.derived_thalion_candidate import enumerate_thalion_candidates
from tm0.derived_thalion_candidate import minimal_thalion_candidates


class TestDerivedThalionCandidate(unittest.TestCase):
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

    def test_two_state_returning_body_becomes_thalion(self):
        body = derive_body_candidate(
            graph=self.graph,
            region_states=("A", "B"),
            state_characters=self.characters,
            region_name="body-ab",
        )

        candidate = derive_thalion_candidate(
            self.graph,
            body,
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
            candidate.return_path_states,
            ("A", "B", "A"),
        )
        self.assertEqual(
            candidate.return_path_relations,
            ("ab", "ba"),
        )

    def test_second_two_state_returning_body_becomes_thalion(self):
        body = derive_body_candidate(
            graph=self.graph,
            region_states=("C", "D"),
            state_characters=self.characters,
            region_name="body-cd",
        )

        candidate = derive_thalion_candidate(
            self.graph,
            body,
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
            candidate.return_path_states,
            ("C", "D", "C"),
        )
        self.assertEqual(
            candidate.return_path_relations,
            ("cd", "dc"),
        )

    def test_singleton_body_is_rejected(self):
        body = derive_body_candidate(
            graph=self.graph,
            region_states=("A",),
            state_characters=self.characters,
            region_name="body-a",
        )

        with self.assertRaises(ValueError):
            derive_thalion_candidate(
                self.graph,
                body,
            )

    def test_nonreturning_two_state_body_is_rejected(self):
        graph = MotionGraph(
            states=("A", "B", "C"),
            rules=(
                MotionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="ab",
                ),
                MotionRule(
                    source_state="B",
                    target_state="C",
                    relation_name="bc",
                ),
            ),
        )

        characters = {
            "A": (0,),
            "B": (0,),
            "C": (1,),
        }

        body = derive_body_candidate(
            graph=graph,
            region_states=("A", "B"),
            state_characters=characters,
            region_name="body-ab",
        )

        with self.assertRaises(ValueError):
            derive_thalion_candidate(
                graph,
                body,
            )

    def test_enumeration_finds_both_returning_bodies(self):
        candidates = enumerate_thalion_candidates(
            self.graph,
            self.characters,
        )

        state_sets = {
            candidate.states
            for candidate in candidates
        }

        self.assertIn(("A", "B"), state_sets)
        self.assertIn(("C", "D"), state_sets)

    def test_minimal_thalions_have_two_states(self):
        candidates = minimal_thalion_candidates(
            self.graph,
            self.characters,
        )

        self.assertEqual(
            {
                candidate.states
                for candidate in candidates
            },
            {
                ("A", "B"),
                ("C", "D"),
            },
        )

        self.assertTrue(
            all(
                len(candidate.states) == 2
                for candidate in candidates
            )
        )

    def test_mixed_character_region_never_becomes_thalion(self):
        candidates = enumerate_thalion_candidates(
            self.graph,
            self.characters,
        )

        self.assertNotIn(
            ("B", "C"),
            {
                candidate.states
                for candidate in candidates
            },
        )


if __name__ == "__main__":
    unittest.main()
