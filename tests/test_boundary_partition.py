import unittest

from tm0.boundary_partition import AddressClass
from tm0.boundary_partition import boundary_addresses
from tm0.boundary_partition import classify_possibility


class TestBoundaryPartition(unittest.TestCase):
    def setUp(self):
        self.addresses = ("a", "b", "c", "d")

        self.partition = classify_possibility(
            self.addresses,
            lambda address: address in {"a", "b"},
        )

    def test_partition_separates_admissible_and_absent(self):
        self.assertEqual(
            set(self.partition.admissible),
            {"a", "b"},
        )

        self.assertEqual(
            set(self.partition.structured_absence),
            {"c", "d"},
        )

    def test_partition_exists_without_boundary_adjacency(self):
        self.assertEqual(
            boundary_addresses(self.partition, ()),
            (),
        )

    def test_cross_class_adjacency_creates_boundary(self):
        adjacency = (
            ("a", "b"),
            ("b", "c"),
            ("c", "d"),
        )

        self.assertEqual(
            set(boundary_addresses(self.partition, adjacency)),
            {"b", "c"},
        )

    def test_same_class_adjacency_is_not_boundary(self):
        adjacency = (
            ("a", "b"),
            ("c", "d"),
        )

        self.assertEqual(
            boundary_addresses(self.partition, adjacency),
            (),
        )

    def test_boundary_depends_on_adjacency(self):
        first = (
            ("a", "c"),
        )

        second = (
            ("b", "d"),
        )

        self.assertNotEqual(
            boundary_addresses(self.partition, first),
            boundary_addresses(self.partition, second),
        )

    def test_unknown_adjacency_address_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "adjacency address must belong to possibility",
        ):
            boundary_addresses(
                self.partition,
                (("a", "x"),),
            )

    def test_classifier_records_structured_absence(self):
        self.assertEqual(
            self.partition.classes["c"],
            AddressClass.STRUCTURED_ABSENCE,
        )


if __name__ == "__main__":
    unittest.main()
