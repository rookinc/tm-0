import unittest

from tm0.aligned_g15_cocycle import (
    bit_to_local_sign,
    ingest_aligned_g15_cocycle,
    load_source,
)
from tm0.local_sign_product import LocalSign


class TestAlignedG15Cocycle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = load_source()
        cls.cocycle = ingest_aligned_g15_cocycle()

    def test_source_identity_is_preserved(self):
        self.assertEqual(
            self.cocycle.source_name,
            "transport_cocycle_edges",
        )
        self.assertEqual(
            self.cocycle.source_status,
            "imported_from_aletheos_aligned_cocycle",
        )
        self.assertEqual(
            self.cocycle.base_graph,
            "G15",
        )
        self.assertEqual(
            self.cocycle.source_graph,
            "G15",
        )

    def test_provenance_boundary_is_explicit(self):
        self.assertEqual(
            self.cocycle.provenance_classification,
            "aligned_imported_representative_native_origin_open",
        )

    def test_sixty_directed_records_are_ingested(self):
        self.assertEqual(
            self.cocycle.directed_record_count,
            60,
        )

    def test_thirty_undirected_edges_are_derived(self):
        self.assertEqual(
            len(self.cocycle.edges),
            30,
        )
        self.assertEqual(
            len(self.cocycle.signs),
            30,
        )
        self.assertEqual(
            len(self.cocycle.cocycle_bits),
            30,
        )

    def test_fifteen_vertices_are_derived(self):
        self.assertEqual(
            len(self.cocycle.vertices),
            15,
        )

    def test_each_edge_has_two_directed_records(self):
        self.assertEqual(
            set(
                self.cocycle.directed_records_per_edge.values()
            ),
            {
                2,
            },
        )

    def test_bit_zero_maps_to_preserve(self):
        self.assertIs(
            bit_to_local_sign(0),
            LocalSign.PRESERVE,
        )

    def test_bit_one_maps_to_invert(self):
        self.assertIs(
            bit_to_local_sign(1),
            LocalSign.INVERT,
        )

    def test_invalid_bit_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "must be 0 or 1",
        ):
            bit_to_local_sign(2)

    def test_bit_and_sign_counts_cover_all_edges(self):
        self.assertEqual(
            sum(self.cocycle.bit_counts.values()),
            30,
        )
        self.assertEqual(
            sum(self.cocycle.sign_counts.values()),
            30,
        )

    def test_bit_and_sign_counts_agree(self):
        self.assertEqual(
            self.cocycle.bit_counts.get(0, 0),
            self.cocycle.sign_counts.get(1, 0),
        )
        self.assertEqual(
            self.cocycle.bit_counts.get(1, 0),
            self.cocycle.sign_counts.get(-1, 0),
        )

    def test_source_artifact_path_is_retained(self):
        self.assertEqual(
            self.cocycle.source_artifact,
            self.source["source_artifact"],
        )


if __name__ == "__main__":
    unittest.main()
