import numpy as np
from srai_math.algebra import coordinates,reconstruct,projection_matrix,is_in_span,null_space_basis,change_of_basis_matrix
def test_coordinates():
    B=np.array([[1.,1.],[1.,-1.]])
    v=np.array([4.,2.])
    assert np.allclose(reconstruct(coordinates(v,B),B),v)
def test_projection():
    B=np.array([[1.],[1.],[0.]])
    P=projection_matrix(B)
    assert np.allclose(P,P.T) and np.allclose(P@P,P)
def test_span():
    B=np.array([[1.,0.],[0.,1.],[0.,0.]])
    assert is_in_span([2,3,0],B)
    assert not is_in_span([2,3,1],B)
def test_null():
    A=np.array([[1.,2.,3.],[2.,4.,6.]])
    assert np.allclose(A@null_space_basis(A),0,atol=1e-10)
def test_change():
    B=np.array([[1.,1.],[1.,-1.]])
    T=change_of_basis_matrix(np.eye(2),B)
    v=np.array([4.,2.])
    assert np.allclose(B@(T@v),v)
