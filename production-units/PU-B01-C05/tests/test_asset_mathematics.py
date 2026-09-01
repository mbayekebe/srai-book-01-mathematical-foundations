"""Numerical checks for the new worked solutions; no package installation."""
import unittest
import numpy as np


class AssetMathematics(unittest.TestCase):
    def test_coordinates(self):
        B = np.array([[1, 1], [1, -1.]])
        np.testing.assert_allclose(np.linalg.solve(B, [6, 2]), [4, 2])
        np.testing.assert_allclose(np.linalg.solve(B, [4, 2]), [3, 1])

    def test_rank_nullity(self):
        A = np.array([[1, 2, 3], [2, 4, 6.]])
        N = np.array([[-2, -3], [1, 0], [0, 1.]])
        self.assertEqual(np.linalg.matrix_rank(A), 1)
        self.assertEqual(np.linalg.matrix_rank(N), 2)
        np.testing.assert_allclose(A @ N, 0)

    def test_nonunique_coordinates(self):
        B = np.array([[1, 2], [2, 4.]])
        for t in [-4, 0, 1, 8]:
            np.testing.assert_allclose(B @ [3 - 2*t, t], [3, 6])

    def test_line_projection(self):
        P = np.full((2, 2), .5)
        p = P @ [2, 3]
        r = np.array([2, 3]) - p
        np.testing.assert_allclose(p, [2.5, 2.5])
        np.testing.assert_allclose(r, [-.5, .5])
        np.testing.assert_allclose(P @ P, P)
        self.assertAlmostEqual(p @ r, 0)
        self.assertAlmostEqual(p @ p + r @ r, 13)

    def test_plane_projection(self):
        P = np.diag([1., 1., 0.]); x = np.array([2., 3., 4.])
        p = P @ x; r = x-p
        np.testing.assert_allclose(p, [2, 3, 0])
        np.testing.assert_allclose(r, [0, 0, 4])
        self.assertAlmostEqual(x @ x, 29)
        self.assertAlmostEqual(p @ p, 13)
        self.assertAlmostEqual(r @ r, 16)

    def test_least_squares(self):
        A = np.array([[1., 0.], [1., 1.], [1., 2.]])
        b = np.array([1., 2., 2.]); beta = np.linalg.lstsq(A, b, rcond=None)[0]
        np.testing.assert_allclose(beta, [7/6, 1/2])
        np.testing.assert_allclose(A @ beta, [7/6, 5/3, 13/6])
        r = b-A @ beta
        np.testing.assert_allclose(r, [-1/6, 1/3, -1/6])
        np.testing.assert_allclose(A.T @ r, 0, atol=1e-12)
        self.assertAlmostEqual(r @ r, 1/6)

    def test_oblique_counterexample(self):
        H = np.array([[1., 1.], [0., 0.]])
        np.testing.assert_allclose(H @ H, H)
        self.assertFalse(np.allclose(H.T, H))
        x = np.array([0., 1.]); p = H @ x
        self.assertAlmostEqual(p @ (x-p), -1)

    def test_nonunique_fit(self):
        A = np.ones((2, 2)); b = np.array([1., 3.])
        beta = np.linalg.lstsq(A, b, rcond=None)[0]
        np.testing.assert_allclose(beta, [1, 1])
        np.testing.assert_allclose(A @ beta, [2, 2])
        for t in [-3, -1, 0, 2]:
            c = np.array([1+t, 1-t])
            np.testing.assert_allclose(A @ c, [2, 2])
            self.assertAlmostEqual(c @ c, 2+2*t*t)

    def test_policy_gram_and_coefficients(self):
        B = np.array([[1., .2], [.2, 1.], [.6, .6]])
        x = np.array([.9, .7, .1])
        np.testing.assert_allclose(B.T @ B, [[7/5, 19/25], [19/25, 7/5]])
        np.testing.assert_allclose(B.T @ x, [11/10, 47/50])
        c = np.linalg.lstsq(B, x, rcond=None)[0]
        np.testing.assert_allclose(c, [43/72, 25/72])
        self.assertAlmostEqual(c.sum(), 17/18)
        np.testing.assert_allclose(B @ c, [2/3, 7/15, 17/30])
        r = x-B @ c
        np.testing.assert_allclose(r, [7/30, 7/30, -7/15])
        np.testing.assert_allclose(B.T @ r, 0, atol=1e-12)


if __name__ == '__main__':
    unittest.main()
