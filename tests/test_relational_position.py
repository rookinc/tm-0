import unittest

from tm0.carrier_register import InternalRegister
from tm0.continuity import begin_null_trace, extend_trace
from tm0.relational_position import RelationalProfile


class TestRelationalPosition(unittest.TestCase):
    def setUp(self):
        self.null_trace = begin_null_trace()
        self.characterized_trace = extend_trace(
            begin_null_trace(),
            InternalRegister.CHARACTERIZED,
        )
        self.returned_trace = extend_trace(
            self.characterized_trace,
            InternalRegister.NULL,
        )

    def test_identical_centers_with_different_degree_are_distinct(self):
        first = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[self.characterized_trace],
        )
        second = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[
                self.characterized_trace,
                self.returned_trace,
            ],
        )

        self.assertNotEqual(first, second)
        self.assertEqual(first.degree, 1)
        self.assertEqual(second.degree, 2)

    def test_identical_centers_with_equal_degree_but_different_neighbors_are_distinct(self):
        first = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[self.characterized_trace],
        )
        second = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[self.returned_trace],
        )

        self.assertEqual(first.degree, second.degree)
        self.assertNotEqual(first, second)

    def test_neighbor_order_does_not_create_false_identity(self):
        first = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[
                self.characterized_trace,
                self.returned_trace,
            ],
        )
        second = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[
                self.returned_trace,
                self.characterized_trace,
            ],
        )

        self.assertEqual(first, second)

    def test_perfect_duplicate_profiles_still_collapse(self):
        first = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[self.characterized_trace],
        )
        second = RelationalProfile.from_parts(
            center=begin_null_trace(),
            neighbors=[
                extend_trace(
                    begin_null_trace(),
                    InternalRegister.CHARACTERIZED,
                )
            ],
        )

        self.assertEqual(first, second)
        self.assertIsNot(first, second)

    def test_relation_distinguishes_without_intrinsic_center_identity(self):
        isolated = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[],
        )
        related = RelationalProfile.from_parts(
            center=self.null_trace,
            neighbors=[self.characterized_trace],
        )

        self.assertEqual(isolated.center, related.center)
        self.assertNotEqual(isolated, related)


if __name__ == "__main__":
    unittest.main()
