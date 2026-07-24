import unittest

from tm0.boundary_partition import AddressClass
from tm0.boundary_persistence import BoundaryCandidate
from tm0.boundary_persistence import partition_by_boundary_persistence
from tm0.boundary_persistence import partition_from_classes


class TestBoundaryPersistence(unittest.TestCase):
    def setUp(self):
        self.adjacency = (
            ("a", "b"),
            ("b", "c"),
            ("c", "d"),
        )

        self.current = partition_from_classes(
            {
                "a": AddressClass.ADMISSIBLE,
                "b": AddressClass.ADMISSIBLE,
                "c": AddressClass.STRUCTURED_ABSENCE,
                "d": AddressClass.STRUCTURED_ABSENCE,
            }
        )

    def test_candidate_preserving_boundary_is_admissible(self):
        candidate = BoundaryCandidate(
            address="preserve",
            resulting_partition=partition_from_classes(
                {
                    "a": AddressClass.ADMISSIBLE,
                    "b": AddressClass.ADMISSIBLE,
                    "c": AddressClass.STRUCTURED_ABSENCE,
                    "d": AddressClass.STRUCTURED_ABSENCE,
                }
            ),
        )

        result = partition_by_boundary_persistence(
            self.current,
            (candidate,),
            self.adjacency,
        )

        self.assertEqual(
            result.admissible,
            (candidate,),
        )

        self.assertEqual(
            result.structured_absence,
            (),
        )

    def test_candidate_moving_boundary_is_structured_absence(self):
        candidate = BoundaryCandidate(
            address="move",
            resulting_partition=partition_from_classes(
                {
                    "a": AddressClass.ADMISSIBLE,
                    "b": AddressClass.STRUCTURED_ABSENCE,
                    "c": AddressClass.STRUCTURED_ABSENCE,
                    "d": AddressClass.STRUCTURED_ABSENCE,
                }
            ),
        )

        result = partition_by_boundary_persistence(
            self.current,
            (candidate,),
            self.adjacency,
        )

        self.assertEqual(
            result.admissible,
            (),
        )

        self.assertEqual(
            result.structured_absence,
            (candidate,),
        )

    def test_mixed_candidates_partition_cleanly(self):
        preserve = BoundaryCandidate(
            address="preserve",
            resulting_partition=self.current,
        )

        move = BoundaryCandidate(
            address="move",
            resulting_partition=partition_from_classes(
                {
                    "a": AddressClass.ADMISSIBLE,
                    "b": AddressClass.STRUCTURED_ABSENCE,
                    "c": AddressClass.STRUCTURED_ABSENCE,
                    "d": AddressClass.STRUCTURED_ABSENCE,
                }
            ),
        )

        result = partition_by_boundary_persistence(
            self.current,
            (preserve, move),
            self.adjacency,
        )

        self.assertEqual(
            result.admissible,
            (preserve,),
        )

        self.assertEqual(
            result.structured_absence,
            (move,),
        )

    def test_same_class_change_can_preserve_boundary(self):
        candidate = BoundaryCandidate(
            address="internal-change",
            resulting_partition=partition_from_classes(
                {
                    "a": AddressClass.ADMISSIBLE,
                    "b": AddressClass.ADMISSIBLE,
                    "c": AddressClass.STRUCTURED_ABSENCE,
                    "d": AddressClass.STRUCTURED_ABSENCE,
                }
            ),
        )

        result = partition_by_boundary_persistence(
            self.current,
            (candidate,),
            self.adjacency,
        )

        self.assertEqual(
            len(result.admissible),
            1,
        )


if __name__ == "__main__":
    unittest.main()
