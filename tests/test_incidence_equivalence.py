import unittest

from tm0.incidence_equivalence import (
    EndpointEquivalence,
    anonymous_relations,
    composition_equalities,
    is_closed,
    is_composable,
)


class TestAnonymousEndpointIncidence(unittest.TestCase):
    def setUp(self):
        self.relations = anonymous_relations(3)
        self.open_equalities = composition_equalities(self.relations)
        self.closed_equalities = self.open_equalities + (
            (
                self.relations[-1].target,
                self.relations[0].source,
            ),
        )

    def test_relation_ports_are_local_positions(self):
        first = self.relations[0]

        self.assertEqual(first.source, (0, "source"))
        self.assertEqual(first.target, (0, "target"))

    def test_open_chain_is_composable(self):
        incidence = EndpointEquivalence(self.open_equalities)

        self.assertTrue(
            is_composable(self.relations, incidence)
        )

    def test_open_chain_is_not_closed(self):
        incidence = EndpointEquivalence(self.open_equalities)

        self.assertFalse(
            is_closed(self.relations, incidence)
        )

    def test_closed_chain_is_composable(self):
        incidence = EndpointEquivalence(self.closed_equalities)

        self.assertTrue(
            is_composable(self.relations, incidence)
        )

    def test_closed_chain_returns_to_first_source_port(self):
        incidence = EndpointEquivalence(self.closed_equalities)

        self.assertTrue(
            incidence.equivalent(
                self.relations[-1].target,
                self.relations[0].source,
            )
        )

    def test_closed_chain_is_closed(self):
        incidence = EndpointEquivalence(self.closed_equalities)

        self.assertTrue(
            is_closed(self.relations, incidence)
        )

    def test_closure_difference_is_one_endpoint_equality(self):
        self.assertEqual(
            len(self.closed_equalities),
            len(self.open_equalities) + 1,
        )

    def test_no_carrier_name_is_required(self):
        for relation in self.relations:
            self.assertFalse(hasattr(relation, "carrier"))
            self.assertFalse(hasattr(relation, "vertex"))
            self.assertFalse(hasattr(relation, "name"))
            self.assertFalse(hasattr(relation, "identity"))

    def test_equivalence_is_transitive(self):
        first = self.relations[0]
        second = self.relations[1]
        third = self.relations[2]

        incidence = EndpointEquivalence(
            (
                (first.target, second.source),
                (second.source, third.source),
            )
        )

        self.assertTrue(
            incidence.equivalent(
                first.target,
                third.source,
            )
        )

    def test_zero_relations_are_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "at least one relation is required",
        ):
            anonymous_relations(0)


if __name__ == "__main__":
    unittest.main()
