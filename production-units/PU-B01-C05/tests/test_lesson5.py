import unittest
import numpy as np
from srai_math.algebra import (projection_matrix, project_onto_subspace, coordinates,
                               reconstruct, change_of_basis_matrix, null_space_basis,
                               column_space_basis, row_space_basis)


class Lesson5Tests(unittest.TestCase):
    def test_zero_leading_column(self):
        np.testing.assert_allclose(projection_matrix([[0, 0], [0, 1]]), [[0, 0], [0, 1]])

    def test_dependent_leading_columns(self):
        b = np.array([[1, 2, 0], [0, 0, 0], [0, 0, 1.]])
        np.testing.assert_allclose(projection_matrix(b), np.diag([1, 0, 1]), atol=1e-12)

    def test_zero_space(self):
        np.testing.assert_allclose(projection_matrix(np.zeros((3, 2))), np.zeros((3, 3)))

    def test_empty_basis(self):
        np.testing.assert_allclose(projection_matrix(np.empty((3, 0))), np.zeros((3, 3)))

    def test_projection_identities(self):
        b = np.array([[1, 2], [3, 4], [5, 6.]])
        p = projection_matrix(b)
        np.testing.assert_allclose(p.T, p, atol=1e-12)
        np.testing.assert_allclose(p @ p, p, atol=1e-12)
        np.testing.assert_allclose(p @ b, b, atol=1e-12)

    def test_projection_column_order_invariance(self):
        b = np.array([[0, 1, 2], [0, 0, 0], [1, 0, 0.]])
        np.testing.assert_allclose(projection_matrix(b), projection_matrix(b[:, ::-1]), atol=1e-12)

    def test_coordinates(self):
        b = np.array([[1, 1], [1, -1.]])
        np.testing.assert_allclose(coordinates([4, 2], b), [3, 1])
        np.testing.assert_allclose(reconstruct([3, 1], b), [4, 2])
        np.testing.assert_allclose(change_of_basis_matrix(np.eye(2), b) @ [4, 2], [3, 1])

    def test_nonunique_coordinates_rejected(self):
        with self.assertRaises(ValueError):
            coordinates([2, 4], [[1, 2], [2, 4]])

    def test_fundamental_spaces(self):
        a = np.array([[1, 2, 3], [2, 4, 6.]])
        n = null_space_basis(a)
        self.assertEqual(n.shape, (3, 2))
        self.assertEqual(column_space_basis(a).shape, (2, 1))
        self.assertEqual(row_space_basis(a).shape, (1, 3))
        np.testing.assert_allclose(a @ n, 0, atol=1e-12)

    def test_least_squares(self):
        a = np.array([[1, 0], [1, 1], [1, 2.]])
        b = np.array([1, 2, 2.])
        beta = np.linalg.lstsq(a, b, rcond=None)[0]
        np.testing.assert_allclose(beta, [7/6, 1/2])
        np.testing.assert_allclose(b - a @ beta, [-1/6, 1/3, -1/6])

    def test_policy_decomposition(self):
        b = np.array([[1, .2], [.2, 1], [.6, .6]])
        proposal = np.array([.9, .7, .1])
        fitted = project_onto_subspace(proposal, b)
        np.testing.assert_allclose(fitted, [2/3, 7/15, 17/30])
        np.testing.assert_allclose(np.linalg.lstsq(b, proposal, rcond=None)[0], [43/72, 25/72])
        np.testing.assert_allclose(b.T @ (proposal - fitted), 0, atol=1e-12)


if __name__ == '__main__':
    unittest.main()
