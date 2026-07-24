import unittest

from tm0.closure_visibility import DirectedIncidenceFixture
from tm0.continuity import begin_null_trace


class TestClosureVisibility(unittest.TestCase):
    def setUp(self):
        trace = begin_null_trace()

        self.open_path = DirectedIncidenceFixture.from_edges(
            root="r",
            edges=[
                ("a", "r"),
                ("r", "b"),
                ("b", "c"),
            ],
            trace=trace,
        )

        self.closed_cycle = DirectedIncidenceFixture.from_edges(
            root="r",
            edges=[
                ("a", "r"),
                ("r", "b"),
                ("b", "a"),
            ],
            trace=trace,
        )

    def test_root_local_profiles_are_equal(self):
        self.assertEqual(
            self.open_path.local_profile(),
            self.closed_cycle.local_profile(),
        )

    def test_both_roots_have_one_incoming_and_one_outgoing_role(self):
        open_profile = self.open_path.local_profile()
        closed_profile = self.closed_cycle.local_profile()

        self.assertEqual(open_profile.indegree, 1)
        self.assertEqual(open_profile.outdegree, 1)
        self.assertEqual(closed_profile.indegree, 1)
        self.assertEqual(closed_profile.outdegree, 1)

    def test_open_path_has_no_return_to_root(self):
        self.assertFalse(
            self.open_path.root_has_nonempty_return()
        )

    def test_closed_cycle_has_return_to_root(self):
        self.assertTrue(
            self.closed_cycle.root_has_nonempty_return()
        )

    def test_local_role_cannot_determine_closure(self):
        self.assertEqual(
            self.open_path.local_profile(),
            self.closed_cycle.local_profile(),
        )
        self.assertNotEqual(
            self.open_path.root_has_nonempty_return(),
            self.closed_cycle.root_has_nonempty_return(),
        )

    def test_fixture_handles_do_not_appear_in_local_profile(self):
        profile_text = repr(self.closed_cycle.local_profile())

        for handle in ("r", "a", "b", "c"):
            self.assertNotIn(f"'{handle}'", profile_text)


if __name__ == "__main__":
    unittest.main()
