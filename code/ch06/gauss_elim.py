# Triangular solves and Gaussian elimination with partial pivoting
import numpy as np


def back_substitution(U, c):
    """Solve U x = c for upper triangular U (about n^2 flops)."""
    n = len(c)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (c[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]
    return x


def forward_substitution(L, c):
    """Solve L z = c for lower triangular L."""
    n = len(c)
    z = np.zeros(n)
    for i in range(n):
        z[i] = (c[i] - L[i, :i] @ z[:i]) / L[i, i]
    return z


def gauss_solve(A, b, verbose=False):
    """Solve A x = b by Gaussian elimination with partial pivoting."""
    A = np.array(A, dtype=float)          # work on copies
    b = np.array(b, dtype=float)
    n = len(b)
    for k in range(n - 1):
        p = k + np.argmax(np.abs(A[k:, k]))      # row of the largest pivot candidate
        if A[p, k] == 0:
            raise ValueError("matrix is singular")
        if p != k:                               # swap rows k and p
            A[[k, p]] = A[[p, k]]
            b[[k, p]] = b[[p, k]]
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]                # multiplier
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
        if verbose:
            print(f"after step {k + 1} (pivot row {p + 1}):")
            print(np.column_stack([A, b]))
    return back_substitution(A, b)


A = np.array([[1, 2, 6], [4, 8, -1], [-2, 3, 5]], dtype=float)
b = np.array([3, -13, -3], dtype=float)
x = gauss_solve(A, b, verbose=True)
print("x =", x)
print("residual b - A x =", b - A @ x)
print("numpy.linalg.solve:", np.linalg.solve(A, b))
