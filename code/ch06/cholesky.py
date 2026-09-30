# Cholesky factorisation A = L L^T of a symmetric positive definite matrix
import numpy as np


def cholesky(A):
    """Return lower triangular L with A = L L^T (A symmetric positive definite)."""
    A = np.array(A, dtype=float)
    n = A.shape[0]
    L = np.zeros((n, n))
    for k in range(n):
        s = A[k, k] - L[k, :k] @ L[k, :k]
        if s <= 0:
            raise ValueError("matrix is not positive definite")
        L[k, k] = np.sqrt(s)
        for i in range(k + 1, n):
            L[i, k] = (A[i, k] - L[i, :k] @ L[k, :k]) / L[k, k]
    return L


A = np.array([[4, -1, 1], [-1, 4.25, 2.75], [1, 2.75, 3.5]])
L = cholesky(A)
print("L =\n", L)
print("||A - L L^T|| =", np.linalg.norm(A - L @ L.T))
print("numpy cholesky agrees:", np.allclose(L, np.linalg.cholesky(A)))

# solve A x = b:  L z = b (forward),  L^T x = z (backward)
b = np.array([4.0, 6.0, 7.25])
z = np.linalg.solve(L, b)
x = np.linalg.solve(L.T, z)
print("solution x =", x)

# Tests for positive definiteness of B
B = np.array([[10, -2, -1], [-2, 8, -3], [-1, -3, 6]], dtype=float)
minors = [np.linalg.det(B[:k, :k]) for k in range(1, 4)]
print("leading principal minors of B:", np.round(minors, 6))
print("eigenvalues of B:", np.round(np.linalg.eigvalsh(B), 6))
C = np.array([[1, 2], [2, 1]], dtype=float)
try:
    cholesky(C)
except ValueError as err:
    print("C =", C.tolist(), "->", err)
