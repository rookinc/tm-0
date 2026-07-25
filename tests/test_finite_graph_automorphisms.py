import unittest

from tm0.finite_graph_automorphisms import (
    enumerate_graph_automorphisms,
    permutation_orbit,
    point_stabilizer,
)


class TestFiniteGraphAutomorphisms(unittest.TestCase):
    def test_path_on_three_vertices_has_two_automorphisms(self):
        automorphisms = enumerate_graph_automorphisms(
            vertices=(0, 1, 2),
            edges=(
                (0, 1),
                (1, 2),
            ),
        )

        self.assertEqual(
            set(automorphisms),
            {
                (0, 1, 2),
                (2, 1, 0),
            },
        )

    def test_triangle_has_six_automorphisms(self):
        automorphisms = enumerate_graph_automorphisms(
            vertices=(0, 1, 2),
            edges=(
                (0, 1),
                (1, 2),
                (2, 0),
            ),
        )

        self.assertEqual(
            len(automorphisms),
            6,
        )

    def test_asymmetric_degree_profile_restricts_action(self):
        automorphisms = enumerate_graph_automorphisms(
            vertices=(0, 1, 2, 3),
            edges=(
                (0, 1),
                (1, 2),
                (1, 3),
            ),
        )

        self.assertEqual(
            len(automorphisms),
            6,
        )

        for permutation in automorphisms:
            self.assertEqual(
                permutation[1],
                1,
            )

    def test_point_orbit_is_derived(self):
        automorphisms = enumerate_graph_automorphisms(
            vertices=(0, 1, 2),
            edges=(
                (0, 1),
                (1, 2),
                (2, 0),
            ),
        )

        self.assertEqual(
            permutation_orbit(
                0,
                automorphisms,
            ),
            (
                0,
                1,
                2,
            ),
        )

    def test_point_stabilizer_is_derived(self):
        automorphisms = enumerate_graph_automorphisms(
            vertices=(0, 1, 2),
            edges=(
                (0, 1),
                (1, 2),
                (2, 0),
            ),
        )

        stabilizer = point_stabilizer(
            0,
            automorphisms,
        )

        self.assertEqual(
            len(stabilizer),
            2,
        )

        self.assertTrue(
            all(
                permutation[0] == 0
                for permutation in stabilizer
            )
        )

    def test_duplicate_vertices_are_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "must be distinct",
        ):
            enumerate_graph_automorphisms(
                vertices=(0, 0, 1),
                edges=((0, 1),),
            )


if __name__ == "__main__":
    unittest.main()
