import unittest

from tm0.occurrence import (
    instantiate_occurrence,
    occurrence_ledger,
    resulting_carrier_catalogue,
)


class TestAnonymousOccurrencePlurality(unittest.TestCase):
    def test_one_occurrence_has_ledger_size_one(self):
        event = instantiate_occurrence()

        ledger = occurrence_ledger([event])

        self.assertEqual(len(ledger), 1)

    def test_two_occurrences_have_ledger_size_two(self):
        first = instantiate_occurrence()
        second = instantiate_occurrence()

        ledger = occurrence_ledger([first, second])

        self.assertEqual(len(ledger), 2)

    def test_occurrences_have_equal_resulting_carrier_state(self):
        first = instantiate_occurrence()
        second = instantiate_occurrence()

        self.assertEqual(first.result, second.result)

    def test_two_occurrences_collapse_to_one_carrier_description(self):
        first = instantiate_occurrence()
        second = instantiate_occurrence()

        catalogue = resulting_carrier_catalogue([first, second])

        self.assertEqual(len(catalogue), 1)
        self.assertEqual(catalogue[0], first.result)

    def test_plurality_lives_in_ledger_not_carrier_state(self):
        first = instantiate_occurrence()
        second = instantiate_occurrence()

        ledger = occurrence_ledger([first, second])
        catalogue = resulting_carrier_catalogue([first, second])

        self.assertEqual(len(ledger), 2)
        self.assertEqual(len(catalogue), 1)

    def test_reusing_one_occurrence_still_preserves_multiplicity(self):
        event = instantiate_occurrence()

        ledger = occurrence_ledger([event, event])

        self.assertEqual(len(ledger), 2)


if __name__ == "__main__":
    unittest.main()
