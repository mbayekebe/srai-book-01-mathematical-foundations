import numpy as np


def as_matrix(a):
    m=np.asarray(a,dtype=float)
    if m.ndim!=2: raise ValueError("Expected a two-dimensional matrix.")
    return m
def rank(a,tol=None): return int(np.linalg.matrix_rank(as_matrix(a),tol=tol))


def matrix_add(a, b):
    a, b = as_matrix(a), as_matrix(b)
    if a.shape != b.shape:
        raise ValueError("Matrices must have identical shapes.")
    return a + b


def matrix_multiply(a, b):
    a, b = as_matrix(a), as_matrix(b)
    if a.shape[1] != b.shape[0]:
        raise ValueError("Inner matrix dimensions must agree.")
    return a @ b


def transpose(a):
    return as_matrix(a).T


def trace(a):
    matrix = as_matrix(a)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Trace requires a square matrix.")
    return float(np.trace(matrix))


def determinant_2x2(a):
    matrix = as_matrix(a)
    if matrix.shape != (2, 2):
        raise ValueError("A 2x2 matrix is required.")
    return float(matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0])


def gaussian_elimination(a, b, tol=None):
    """Solve a square system using elimination with partial pivoting."""
    matrix = as_matrix(a).copy()
    vector = np.asarray(b, dtype=float).copy()
    if matrix.shape[0] != matrix.shape[1] or vector.shape != (matrix.shape[0],):
        raise ValueError("Require a square matrix and a conformable vector.")
    n = matrix.shape[0]
    if tol is None:
        scale = max(1.0, float(np.linalg.norm(matrix, ord=np.inf)))
        tol = np.finfo(float).eps * n * scale

    for column in range(n - 1):
        pivot = column + int(np.argmax(np.abs(matrix[column:, column])))
        if abs(matrix[pivot, column]) <= tol:
            raise ValueError("Matrix is singular to working precision.")
        if pivot != column:
            matrix[[column, pivot]] = matrix[[pivot, column]]
            vector[[column, pivot]] = vector[[pivot, column]]
        factors = matrix[column + 1 :, column] / matrix[column, column]
        matrix[column + 1 :, column:] -= factors[:, None] * matrix[column, column:]
        vector[column + 1 :] -= factors * vector[column]

    if n and abs(matrix[-1, -1]) <= tol:
        raise ValueError("Matrix is singular to working precision.")

    solution = np.zeros(n, dtype=float)
    for row in range(n - 1, -1, -1):
        rhs = vector[row] - matrix[row, row + 1 :] @ solution[row + 1 :]
        solution[row] = rhs / matrix[row, row]
    return solution


def residual(a, x, b):
    return np.asarray(b, dtype=float) - as_matrix(a) @ np.asarray(x, dtype=float)


def condition_number(a):
    return float(np.linalg.cond(as_matrix(a)))
