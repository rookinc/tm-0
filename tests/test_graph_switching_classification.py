import unittest

from tm0.graph_switching_classification import graph_switching_equivalent
from tm0.graph_switching_classification import graph_switching_signature
from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign


class TestGraphSwitchingClassification(unittest.TestCase):
    def setUp(self):
        self.edges = (
            ("a", "b"),
            ("b", "c"),
            ("c", "a"),
            ("c", "d"),
            ("d", "a"),
        )

    def test_equivalent_signings_have_same_signature(self):
        source = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.INVERT,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        target = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
            canonical_edge("b", "c"): LocalSign.INVERT,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.INVERT,
        }

        self.assertEqual(
            graph_switching_signature(self.edges, source, "a"),
            graph_switching_signature(self.edges, target, "a"),
        )

        self.assertTrue(
            graph_switching_equivalent(
                self.edges,
                source,
                target,
                "a",
            )
        )

    def test_different_cycle_signatures_are_not_equivalent(self):
        source = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        target = dict(source)
        target[canonical_edge("c", "a")] = LocalSign.INVERT

        self.assertNotEqual(
            graph_switching_signature(self.edges, source, "a"),
            graph_switching_signature(self.edges, target, "a"),
        )

        self.assertFalse(
            graph_switching_equivalent(
                self.edges,
                source,
                target,
                "a",
            )
        )

    def test_signature_length_matches_cycle_rank(self):
        signs = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        signature = graph_switching_signature(
            self.edges,
            signs,
            "a",
        )

        self.assertEqual(len(signature), 2)

    def test_root_choice_preserves_equivalence_result(self):
        source = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.INVERT,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        target = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
            canonical_edge("b", "c"): LocalSign.INVERT,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.INVERT,
        }

        self.assertTrue(
            graph_switching_equivalent(
                self.edges,
                source,
                target,
                "a",
            )
        )

        self.assertTrue(
            graph_switching_equivalent(
                self.edges,
                source,
                target,
                "c",
            )
        )


if __name__ == "__main__":
    unittest.main()
