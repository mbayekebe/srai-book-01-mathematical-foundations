import numpy as np
import pytest

from srai_math.algebra import (
    Vector,
    angle_between,
    cross,
    distance,
    gram_schmidt,
    l1_norm,
    l2_norm,
    linear_combination,
    linf_norm,
    normalize,
    project,
    reject,
)


def test_norms():
    x = [3, -4]
    assert l1_norm(x) == pytest.approx(7.0)
    assert l2_norm(x) == pytest.approx(5.0)
    assert linf_norm(x) == pytest.approx(4.0)


def test_distance():
    assert distance([1, 2], [4, 6]) == pytest.approx(5.0)


def test_normalize():
    u = normalize([3, 4])
    assert np.linalg.norm(u) == pytest.approx(1.0)


def test_angle():
    assert angle_between([1, 0], [0, 1]) == pytest.approx(np.pi / 2)


def test_projection_rejection():
    x = np.array([3.0, 4.0])
    u = np.array([1.0, 0.0])
    p = project(x, u)
    r = reject(x, u)
    assert np.allclose(p, [3.0, 0.0])
    assert np.allclose(r, [0.0, 4.0])
    assert np.dot(p, r) == pytest.approx(0.0)


def test_cross():
    assert np.allclose(cross([1, 0, 0], [0, 1, 0]), [0, 0, 1])


def test_linear_combination():
    result = linear_combination([2, -1], [[1, 2], [3, 4]])
    assert np.allclose(result, [-1, 0])


def test_gram_schmidt():
    basis = gram_schmidt([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
    Q = np.column_stack(basis)
    assert np.allclose(Q.T @ Q, np.eye(Q.shape[1]), atol=1e-12)


def test_vector_class():
    a = Vector.from_iterable([1, 2])
    b = Vector.from_iterable([3, 4])
    assert (a + b).values == (4.0, 6.0)
    assert (2 * a).values == (2.0, 4.0)
    assert a.dot(b) == pytest.approx(11.0)
