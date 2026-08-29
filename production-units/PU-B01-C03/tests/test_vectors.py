import unittest

import numpy as np

from srai_math.algebra import (
    cosine_similarity,
    dot,
    gram_schmidt,
    l1_norm,
    l2_norm,
    linf_norm,
    normalize,
    project,
    reject,
)


class VectorFoundationTests(unittest.TestCase):
    def test_norms(self):
        vector = [3, -4]
        self.assertEqual(l1_norm(vector), 7.0)
        self.assertEqual(l2_norm(vector), 5.0)
        self.assertEqual(linf_norm(vector), 4.0)

    def test_projection_invariant(self):
        vector = [3, 4]
        direction = [1, 0]
        np.testing.assert_allclose(project(vector, direction), [3, 0])
        residual = reject(vector, direction)
        np.testing.assert_allclose(residual, [0, 4])
        self.assertTrue(np.isclose(dot(residual, direction), 0.0))

    def test_gram_schmidt_invariant(self):
        basis = gram_schmidt([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
        matrix = np.column_stack(basis)
        np.testing.assert_allclose(matrix.T @ matrix, np.eye(3), atol=1e-12)

    def test_zero_vector_guards(self):
        with self.assertRaises(ValueError):
            normalize([0, 0])
        with self.assertRaises(ValueError):
            cosine_similarity([0, 0], [1, 0])
        with self.assertRaises(ValueError):
            project([1, 2], [0, 0])


if __name__ == "__main__":
    unittest.main()
