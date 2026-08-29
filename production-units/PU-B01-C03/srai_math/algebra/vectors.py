"""Validated vector operations for Chapter 3."""

from dataclasses import dataclass

import numpy as np


def as_vector(x):
    vector = np.asarray(x, dtype=float)
    if vector.ndim != 1:
        raise ValueError("Expected a one-dimensional vector.")
    return vector


def dot(x, y):
    x, y = as_vector(x), as_vector(y)
    if x.shape != y.shape:
        raise ValueError("Vectors must have identical shapes.")
    return float(np.dot(x, y))


def l1_norm(x):
    return float(np.linalg.norm(as_vector(x), 1))


def l2_norm(x):
    return float(np.linalg.norm(as_vector(x)))


def linf_norm(x):
    return float(np.linalg.norm(as_vector(x), np.inf))


def distance(x, y):
    return l2_norm(as_vector(x) - as_vector(y))


def cosine_similarity(x, y):
    x, y = as_vector(x), as_vector(y)
    denominator = l2_norm(x) * l2_norm(y)
    if np.isclose(denominator, 0.0):
        raise ValueError("Cosine similarity is undefined for a zero vector.")
    return float(np.clip(dot(x, y) / denominator, -1.0, 1.0))


def angle_between(x, y):
    return float(np.arccos(cosine_similarity(x, y)))


def project(x, direction):
    x, direction = as_vector(x), as_vector(direction)
    denominator = dot(direction, direction)
    if np.isclose(denominator, 0.0):
        raise ValueError("Cannot project onto the zero vector.")
    return (dot(x, direction) / denominator) * direction


def reject(x, direction):
    return as_vector(x) - project(x, direction)


def cross(x, y):
    x, y = as_vector(x), as_vector(y)
    if x.size != 3 or y.size != 3:
        raise ValueError("Cross product requires three-dimensional vectors.")
    return np.cross(x, y)


def linear_combination(coefficients, vectors):
    coefficients = as_vector(coefficients)
    matrix = np.asarray(vectors, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != coefficients.size:
        raise ValueError("One coefficient is required for each vector.")
    return coefficients @ matrix


def gram_schmidt(vectors, tol=1e-12):
    basis = []
    for vector in [as_vector(value).copy() for value in vectors]:
        for direction in basis:
            vector -= dot(vector, direction) * direction
        norm = l2_norm(vector)
        if norm > tol:
            basis.append(vector / norm)
    return basis


def normalize(x):
    vector = as_vector(x)
    norm = l2_norm(vector)
    if np.isclose(norm, 0.0):
        raise ValueError("Cannot normalize the zero vector.")
    return vector / norm


@dataclass(frozen=True)
class Vector:
    values: tuple[float, ...]

    @classmethod
    def from_iterable(cls, values):
        return cls(tuple(float(value) for value in values))

    def __array__(self, dtype=None):
        return np.asarray(self.values, dtype=dtype)

    def __iter__(self):
        return iter(self.values)

    def __add__(self, other):
        return Vector.from_iterable(np.asarray(self) + np.asarray(other))

    def __mul__(self, scalar):
        return Vector.from_iterable(np.asarray(self) * scalar)

    __rmul__ = __mul__

    def dot(self, other):
        return dot(self, other)
