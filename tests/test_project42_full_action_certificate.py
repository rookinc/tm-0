import unittest

from tm0.project42_full_action_certificate import (
    load_certificate,
    load_project42_action_group,
    partition_action_image,
    partition_action_kernel,
    selected_system_stabilizers,
)


class TestProject42FullActionCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = load_certificate()
        cls.group = load_project42_action_group()

    def test_certificate_passes(self):
        self.assertTrue(
            self.certificate["audit_pass"]
        )

    def test_full_group_has_720_actions(self):
        self.assertEqual(
            len(self.group.actions),
            720,
        )

    def test_carrier_domain_has_30_vertices(self):
        self.assertEqual(
            self.group.carrier_size,
            30,
        )

    def test_family_domain_has_three_systems(self):
        self.assertEqual(
            self.group.family_size,
            3,
        )

    def test_identity_is_derived(self):
        identity = self.group.identity

        self.assertEqual(
            identity.carrier_permutation,
            tuple(range(30)),
        )
        self.assertEqual(
            identity.family_permutation,
            (0, 1, 2),
        )

    def test_partition_action_image_has_order_six(self):
        image = partition_action_image(
            self.group
        )

        self.assertEqual(
            len(image),
            6,
        )
        self.assertEqual(
            set(image),
            {
                (0, 1, 2),
                (0, 2, 1),
                (1, 0, 2),
                (1, 2, 0),
                (2, 0, 1),
                (2, 1, 0),
            },
        )

    def test_partition_action_kernel_has_order_120(self):
        kernel = partition_action_kernel(
            self.group
        )

        self.assertEqual(
            len(kernel),
            120,
        )

    def test_selected_system_stabilizers_have_order_240(self):
        stabilizers = selected_system_stabilizers(
            self.group
        )

        self.assertEqual(
            tuple(
                len(stabilizer)
                for stabilizer in stabilizers
            ),
            (
                240,
                240,
                240,
            ),
        )

    def test_kernel_is_contained_in_each_stabilizer(self):
        kernel = set(
            partition_action_kernel(
                self.group
            )
        )

        for stabilizer in selected_system_stabilizers(
            self.group
        ):
            self.assertTrue(
                kernel <= set(stabilizer)
            )

    def test_each_stabilizer_has_index_three(self):
        for stabilizer in selected_system_stabilizers(
            self.group
        ):
            self.assertEqual(
                len(self.group.actions)
                // len(stabilizer),
                3,
            )

    def test_certificate_counts_match_derived_counts(self):
        derived = self.certificate["derived"]

        self.assertEqual(
            derived["automorphism_count"],
            len(self.group.actions),
        )
        self.assertEqual(
            derived["partition_action_image_count"],
            len(
                partition_action_image(
                    self.group
                )
            ),
        )
        self.assertEqual(
            derived["partition_action_kernel_count"],
            len(
                partition_action_kernel(
                    self.group
                )
            ),
        )
        self.assertEqual(
            tuple(
                derived[
                    "selected_system_stabilizer_counts"
                ]
            ),
            tuple(
                len(stabilizer)
                for stabilizer in (
                    selected_system_stabilizers(
                        self.group
                    )
                )
            ),
        )


if __name__ == "__main__":
    unittest.main()
