import unittest

from tm0.incidence_equivalence import (
    EndpointEquivalence,
    anonymous_relations,
    composition_equalities,
    is_closed,
)
from tm0.return_admissibility import (
    realize_return,
    receipt_confirms_return,
    return_is_admissible,
)


class TestReturnAdmissibility(unittest.TestCase):
    def setUp(self):
        self.relations = anonymous_relations(3)

        self.open_equalities = composition_equalities(
            self.relations
        )

        self.closed_equalities = self.open_equalities + (
            (
                self.relations[-1].target,
                self.relations[0].source,
            ),
        )

        self.open_incidence = EndpointEquivalence(
            self.open_equalities
        )

        self.closed_incidence = EndpointEquivalence(
            self.closed_equalities
        )

    def test_open_chain_does_not_admit_return(self):
        self.assertFalse(
            return_is_admissible(
                self.relations,
                self.open_incidence,
            )
        )

    def test_closed_chain_admits_return(self):
        self.assertTrue(
            return_is_admissible(
                self.relations,
                self.closed_incidence,
            )
        )

    def test_open_chain_cannot_realize_return(self):
        with self.assertRaisesRegex(
            ValueError,
            "return is not admissible without closure",
        ):
            realize_return(
                self.relations,
                self.open_incidence,
            )

    def test_closed_chain_can_realize_return(self):
        receipt = realize_return(
            self.relations,
            self.closed_incidence,
        )

        self.assertTrue(receipt.completed)
        self.assertEqual(
            receipt.relation_order,
            (0, 1, 2),
        )

    def test_return_receipt_ends_at_departure_junction(self):
        receipt = realize_return(
            self.relations,
            self.closed_incidence,
        )

        self.assertTrue(
            receipt_confirms_return(
                receipt,
                self.closed_incidence,
            )
        )

    def test_closure_is_unchanged_by_reading_admissibility(self):
        before = is_closed(
            self.relations,
            self.closed_incidence,
        )

        admissible = return_is_admissible(
            self.relations,
            self.closed_incidence,
        )

        after = is_closed(
            self.relations,
            self.closed_incidence,
        )

        self.assertTrue(admissible)
        self.assertEqual(before, after)

    def test_closure_and_return_receipt_are_different_types(self):
        closure = is_closed(
            self.relations,
            self.closed_incidence,
        )

        receipt = realize_return(
            self.relations,
            self.closed_incidence,
        )

        self.assertIsInstance(closure, bool)
        self.assertNotIsInstance(receipt, bool)

    def test_closure_does_not_automatically_create_a_receipt(self):
        receipts = []

        self.assertTrue(
            is_closed(
                self.relations,
                self.closed_incidence,
            )
        )
        self.assertEqual(receipts, [])

        receipts.append(
            realize_return(
                self.relations,
                self.closed_incidence,
            )
        )

        self.assertEqual(len(receipts), 1)


if __name__ == "__main__":
    unittest.main()
