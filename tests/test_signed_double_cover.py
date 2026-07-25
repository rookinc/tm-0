import unittest

from tm0.local_sign_product import LocalSign
from tm0.signed_double_cover import (
    construct_signed_double_cover,
)


class TestSignedDoubleCover(unittest.TestCase):
    def test_preserve_edge_lifts_in_parallel(self):
        cover = construct_signed_double_cover(
            base_vertices=("a", "b"),
            base_edges=(("a", "b"),),
            signs={
                ("a", "b"): LocalSign.PRESERVE,
            },
        )

        self.assertEqual(
            set(cover.lift_edges),
            {
                (("a", 0), ("b", 0)),
                (("a", 1), ("b", 1)),
            },
        )

        self.assertEqual(
            {
                record.lift_type
                for record in cover.edge_records
            },
            {
                "parallel",
            },
        )

    def test_invert_edge_lifts_crossed(self):
        cover = construct_signed_double_cover(
            base_vertices=("a", "b"),
            base_edges=(("a", "b"),),
            signs={
                ("a", "b"): LocalSign.INVERT,
            },
        )

        self.assertEqual(
            set(cover.lift_edges),
            {
                (("a", 0), ("b", 1)),
                (("a", 1), ("b", 0)),
            },
        )

        self.assertEqual(
            {
                record.lift_type
                for record in cover.edge_records
            },
            {
                "crossed",
            },
        )

    def test_two_lift_vertices_per_base_vertex(self):
        cover = construct_signed_double_cover(
            base_vertices=("a", "b", "c"),
            base_edges=(
                ("a", "b"),
                ("b", "c"),
            ),
            signs={
                ("a", "b"): LocalSign.PRESERVE,
                ("b", "c"): LocalSign.INVERT,
            },
        )

        self.assertEqual(
            len(cover.lift_vertices),
            6,
        )

    def test_two_lift_edges_per_base_edge(self):
        cover = construct_signed_double_cover(
            base_vertices=("a", "b", "c"),
            base_edges=(
                ("a", "b"),
                ("b", "c"),
            ),
            signs={
                ("a", "b"): LocalSign.PRESERVE,
                ("b", "c"): LocalSign.INVERT,
            },
        )

        self.assertEqual(
            len(cover.lift_edges),
            4,
        )
        self.assertEqual(
            len(cover.edge_records),
            4,
        )

    def test_sheet_swap_is_involution(self):
        cover = construct_signed_double_cover(
            base_vertices=("a", "b"),
            base_edges=(("a", "b"),),
            signs={
                ("a", "b"): LocalSign.PRESERVE,
            },
        )

        for vertex in cover.lift_vertices:
            self.assertEqual(
                cover.sheet_swap(
                    cover.sheet_swap(vertex)
                ),
                vertex,
            )

    def test_sheet_swap_orbits_match_base_vertices(self):
        cover = construct_signed_double_cover(
            base_vertices=("a", "b", "c"),
            base_edges=(
                ("a", "b"),
                ("b", "c"),
            ),
            signs={
                ("a", "b"): LocalSign.PRESERVE,
                ("b", "c"): LocalSign.INVERT,
            },
        )

        self.assertEqual(
            cover.sheet_swap_orbits(),
            (
                (("a", 0), ("a", 1)),
                (("b", 0), ("b", 1)),
                (("c", 0), ("c", 1)),
            ),
        )

    def test_base_loop_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "does not support base loops",
        ):
            construct_signed_double_cover(
                base_vertices=("a",),
                base_edges=(("a", "a"),),
                signs={
                    ("a", "a"): LocalSign.PRESERVE,
                },
            )

    def test_unregistered_vertex_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "unregistered vertex",
        ):
            construct_signed_double_cover(
                base_vertices=("a", "b"),
                base_edges=(("a", "c"),),
                signs={
                    ("a", "c"): LocalSign.PRESERVE,
                },
            )

    def test_incomplete_sign_assignment_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "one sign is required per base edge",
        ):
            construct_signed_double_cover(
                base_vertices=("a", "b", "c"),
                base_edges=(
                    ("a", "b"),
                    ("b", "c"),
                ),
                signs={
                    ("a", "b"): LocalSign.PRESERVE,
                },
            )

    def test_edge_records_retain_source_sign(self):
        cover = construct_signed_double_cover(
            base_vertices=("a", "b", "c"),
            base_edges=(
                ("a", "b"),
                ("b", "c"),
            ),
            signs={
                ("a", "b"): LocalSign.PRESERVE,
                ("b", "c"): LocalSign.INVERT,
            },
        )

        for record in cover.edge_records:
            self.assertEqual(
                record.sign,
                cover.base_signs[record.base_edge],
            )


if __name__ == "__main__":
    unittest.main()
