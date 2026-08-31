import numpy as np
import pytest

from srai_math.algebra import gaussian_elimination, residual


def test_gaussian_elimination_matches_numpy():
    matrix = np.array([[3.0, 2.0, -1.0], [2.0, -2.0, 4.0], [-1.0, 0.5, -1.0]])
    vector = np.array([1.0, -2.0, 0.0])
    assert np.allclose(gaussian_elimination(matrix, vector), np.linalg.solve(matrix, vector))


def test_partial_pivoting_row_swap():
    matrix = np.array([[0.0, 2.0], [1.0, 1.0]])
    vector = np.array([4.0, 3.0])
    assert np.allclose(gaussian_elimination(matrix, vector), [1.0, 2.0])


def test_inputs_are_not_mutated():
    matrix = np.array([[2.0, 1.0], [1.0, 3.0]])
    vector = np.array([5.0, 7.0])
    matrix_before, vector_before = matrix.copy(), vector.copy()
    gaussian_elimination(matrix, vector)
    assert np.array_equal(matrix, matrix_before)
    assert np.array_equal(vector, vector_before)


def test_singular_system_is_rejected():
    with pytest.raises(ValueError, match="singular"):
        gaussian_elimination([[1.0, 2.0], [2.0, 4.0]], [3.0, 6.0])


def test_signed_residual_convention():
    matrix = np.array([[2.0, 0.0], [0.0, 3.0]])
    estimate = np.array([1.1, 1.9])
    vector = np.array([2.0, 6.0])
    assert np.allclose(residual(matrix, estimate, vector), [-0.2, 0.3])
