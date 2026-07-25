import unittest

from tm0.project42_invariant_cover_square import (
    classify_aligned_lift_in_cover_square,
    load_cover_square_certificate,
)


class TestProject42InvariantCoverSquare(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = load_cover_square_certificate()
        cls.receipt = classify_aligned_lift_in_cover_square()

    def test_certificate_passed(self):
        self.assertTrue(
            self.certificate["audit_pass"]
        )
        self.assertTrue(
            self.receipt["certificate_audit_pass"]
        )

    def test_four_cover_classes_are_present(self):
        self.assertEqual(
            tuple(
                row["class_id"]
                for row in self.certificate["classes"]
            ),
            (
                "zero",
                "native",
                "alternative",
                "all_one",
            ),
        )

    def test_aligned_lift_counts_are_preserved(self):
        self.assertEqual(
            self.receipt["aligned_lift_vertex_count"],
            30,
        )
        self.assertEqual(
            self.receipt["aligned_lift_edge_count"],
            60,
        )

    def test_only_native_class_matches(self):
        self.assertEqual(
            self.receipt["matching_classes"],
            (
                "native",
            ),
        )
        self.assertEqual(
            self.receipt["unique_matching_class"],
            "native",
        )
        self.assertTrue(
            self.receipt["aligned_lift_is_native_class"]
        )

    def test_native_mapping_is_explicit_bijection(self):
        native = next(
            row
            for row in self.receipt["class_results"]
            if row["class_id"] == "native"
        )

        self.assertTrue(native["isomorphic"])
        self.assertEqual(
            native["mapping_size"],
            30,
        )
        self.assertIsNotNone(native["mapping"])
        self.assertEqual(
            len(native["mapping"]),
            30,
        )
        self.assertEqual(
            len(set(native["mapping"].values())),
            30,
        )

    def test_other_classes_do_not_match(self):
        non_native = {
            row["class_id"]: row["isomorphic"]
            for row in self.receipt["class_results"]
            if row["class_id"] != "native"
        }

        self.assertEqual(
            non_native,
            {
                "zero": False,
                "alternative": False,
                "all_one": False,
            },
        )

    def test_triangle_and_component_profiles_are_retained(self):
        profiles = {
            row["class_id"]: (
                row["triangle_count"],
                row["component_sizes"],
            )
            for row in self.receipt["class_results"]
        }

        self.assertEqual(
            profiles,
            {
                "zero": (
                    20,
                    (15, 15),
                ),
                "native": (
                    20,
                    (30,),
                ),
                "alternative": (
                    0,
                    (30,),
                ),
                "all_one": (
                    0,
                    (30,),
                ),
            },
        )

    def test_native_origin_remains_open(self):
        self.assertFalse(
            self.receipt["native_origin_proved"]
        )
        self.assertEqual(
            self.receipt["provenance_classification"],
            "aligned_imported_representative_native_origin_open",
        )


if __name__ == "__main__":
    unittest.main()
