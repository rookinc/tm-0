import unittest

from tm0.carrier_register import InternalRegister
from tm0.continuity import begin_null_trace, extend_trace
from tm0.directed_relation import DirectedRelationalProfile


class TestDirectedRelationalRole(unittest.TestCase):
    def setUp(self):
        self.center = begin_null_trace()
        self.neighbor = extend_trace(
            begin_null_trace(),
            InternalRegister.CHARACTERIZED,
        )

    def test_source_and_target_roles_are_distinct(self):
        source = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[],
            outgoing=[self.neighbor],
        )
        target = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[self.neighbor],
            outgoing=[],
        )

        self.assertNotEqual(source, target)
        self.assertEqual(source.outdegree, 1)
        self.assertEqual(source.indegree, 0)
        self.assertEqual(target.outdegree, 0)
        self.assertEqual(target.indegree, 1)

    def test_direction_is_lost_in_undirected_shadow(self):
        source = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[],
            outgoing=[self.neighbor],
        )
        target = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[self.neighbor],
            outgoing=[],
        )

        self.assertEqual(
            source.undirected_shadow,
            target.undirected_shadow,
        )
        self.assertNotEqual(source, target)

    def test_neighbor_order_does_not_create_false_distinction(self):
        returned = extend_trace(
            self.neighbor,
            InternalRegister.NULL,
        )

        first = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[self.neighbor, returned],
            outgoing=[],
        )
        second = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[returned, self.neighbor],
            outgoing=[],
        )

        self.assertEqual(first, second)

    def test_equal_in_and_out_counts_can_still_differ_by_content(self):
        returned = extend_trace(
            self.neighbor,
            InternalRegister.NULL,
        )

        first = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[self.neighbor],
            outgoing=[returned],
        )
        second = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[returned],
            outgoing=[self.neighbor],
        )

        self.assertEqual(first.indegree, second.indegree)
        self.assertEqual(first.outdegree, second.outdegree)
        self.assertNotEqual(first, second)

    def test_perfect_directed_duplicates_still_collapse(self):
        first = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[],
            outgoing=[self.neighbor],
        )
        second = DirectedRelationalProfile.from_parts(
            center=begin_null_trace(),
            incoming=[],
            outgoing=[
                extend_trace(
                    begin_null_trace(),
                    InternalRegister.CHARACTERIZED,
                )
            ],
        )

        self.assertEqual(first, second)
        self.assertIsNot(first, second)

    def test_direction_adds_role_without_intrinsic_polarity(self):
        source = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[],
            outgoing=[self.neighbor],
        )
        target = DirectedRelationalProfile.from_parts(
            center=self.center,
            incoming=[self.neighbor],
            outgoing=[],
        )

        self.assertEqual(source.center, target.center)
        self.assertNotEqual(source, target)


if __name__ == "__main__":
    unittest.main()
