import pytest
from srai_math.algebra import cosine_similarity, dot, l2_norm

def test_dot():
    assert dot([1, 2], [3, 4]) == pytest.approx(11.0)

def test_norm():
    assert l2_norm([3, 4]) == pytest.approx(5.0)

def test_cosine():
    assert cosine_similarity([1, 2, 3], [1, 2, 3]) == pytest.approx(1.0)

def test_bad_shape():
    with pytest.raises(ValueError):
        dot([1, 2], [1, 2, 3])

def test_zero_vector():
    with pytest.raises(ValueError):
        cosine_similarity([0, 0], [1, 1])
