import numpy as np
import pytest
from srai_math.algebra import (
    condition_number, determinant_2x2, gaussian_elimination, matrix_add,
    matrix_multiply, rank, residual, trace, transpose,
)
def test_matrix_add():
    assert np.allclose(matrix_add([[1,2]],[[3,4]]),[[4,6]])
def test_matrix_multiply():
    A=np.array([[1,2],[3,4]],float); B=np.array([[5,6],[7,8]],float)
    assert np.allclose(matrix_multiply(A,B),A@B)
def test_transpose_trace_determinant():
    A=[[1,2],[3,4]]
    assert np.allclose(transpose(A),[[1,3],[2,4]])
    assert trace(A)==pytest.approx(5)
    assert determinant_2x2(A)==pytest.approx(-2)
def test_gaussian_elimination():
    A=[[2,1],[1,3]]; b=[5,7]
    x=gaussian_elimination(A,b)
    assert np.allclose(x,[1.6,1.8])
    assert np.allclose(residual(A,x,b),[0,0])
def test_singular():
    with pytest.raises(ValueError):
        gaussian_elimination([[1,2],[2,4]],[3,6])
def test_rank_condition():
    assert rank([[1,2],[2,4]])==1
    assert condition_number(np.eye(2))==pytest.approx(1)
