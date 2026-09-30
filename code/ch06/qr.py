# QR factorisation: classical and modified Gram-Schmidt, and Householder (numpy)
import numpy as np


def qr_cgs(A):
    """Classical Gram-Schmidt: A = Q R, Q with orthonormal columns."""
    A = np.array(A, dtype=float)
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for k in range(n):
        v = A[:, k].copy()
        for j in range(k):
            R[j, k] = Q[:, j] @ A[:, k]       # project the ORIGINAL column
            v -= R[j, k] * Q[:, j]
        R[k, k] = np.linalg.norm(v)
        Q[:, k] = v / R[k, k]
    return Q, R


def qr_mgs(A):
    """Modified Gram-Schmidt: numerically much better than CGS."""
    V = np.array(A, dtype=float)
    m, n = V.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for k in range(n):
        R[k, k] = np.linalg.norm(V[:, k])
        Q[:, k] = V[:, k] / R[k, k]
        for j in range(k + 1, n):
            R[k, j] = Q[:, k] @ V[:, j]       # project the UPDATED column
            V[:, j] -= R[k, j] * Q[:, k]
    return Q, R


A = np.array([[1, -1, 4], [1, 4, -2], [1, 4, 2], [1, -1, 0]], dtype=float)
Q, R = qr_cgs(A)
print("Q =\n", Q, "\nR =\n", R)
print("Q^T Q =\n", np.round(Q.T @ Q, 12))
print("||A - QR|| =", np.linalg.norm(A - Q @ R))

# Solving a square system by QR:  R x = Q^T b
M = np.array([[1, 2, 6], [4, 8, -1], [-2, 3, 5]], dtype=float)
b = np.array([3, -13, -3], dtype=float)
Qm, Rm = np.linalg.qr(M)                     # Householder reflections (LAPACK)
print("QR solution:", np.linalg.solve(Rm, Qm.T @ b))

# Loss of orthogonality on an ill-conditioned matrix
print("\nloss of orthogonality ||I - Q^T Q|| for Hilbert matrices:")
for n in [4, 6, 8, 10, 12]:
    H = 1.0 / (np.arange(1, n + 1)[:, None] + np.arange(n)[None, :])
    errs = []
    for f in (qr_cgs, qr_mgs, np.linalg.qr):
        Qh = f(H)[0]
        errs.append(np.linalg.norm(np.eye(n) - Qh.T @ Qh))
    print(f"n = {n:2d}: CGS {errs[0]:.1e}   MGS {errs[1]:.1e}   Householder {errs[2]:.1e}")
