# LU factorisation with partial pivoting:  P A = L U
import numpy as np
import scipy.linalg as sla


def lu_pivot(A):
    """Return P, L, U with P A = L U (Doolittle form: L has unit diagonal)."""
    A = np.array(A, dtype=float)
    n = A.shape[0]
    perm = np.arange(n)
    for k in range(n - 1):
        p = k + np.argmax(np.abs(A[k:, k]))
        if p != k:
            A[[k, p]] = A[[p, k]]            # swap whole rows (including stored multipliers)
            perm[[k, p]] = perm[[p, k]]
        A[k + 1:, k] /= A[k, k]              # multipliers l_ik, stored below the diagonal
        A[k + 1:, k + 1:] -= np.outer(A[k + 1:, k], A[k, k + 1:])
    L = np.tril(A, -1) + np.eye(n)
    U = np.triu(A)
    P = np.eye(n)[perm]
    return P, L, U


def lu_solve(P, L, U, b):
    """Solve A x = b using P A = L U:  L z = P b, then U x = z."""
    z = sla.solve_triangular(L, P @ b, lower=True, unit_diagonal=True)
    return sla.solve_triangular(U, z)


A = np.array([[1, 2, 6], [4, 8, -1], [-2, 3, 5]], dtype=float)
b = np.array([3, -13, -3], dtype=float)
P, L, U = lu_pivot(A)
print("P =\n", P, "\nL =\n", L, "\nU =\n", U)
print("check ||PA - LU|| =", np.linalg.norm(P @ A - L @ U))
print("x =", lu_solve(P, L, U, b))
print("det A = det(P^T) * prod(diag U) =", np.linalg.det(P.T) * np.prod(np.diag(U)))

# The same with SciPy.  Note: scipy returns A = P L U, i.e. its P is our P^T.
P2, L2, U2 = sla.lu(A)
print("scipy U =\n", U2)
lu, piv = sla.lu_factor(A)        # factorise once ...
for rhs in ([3, -13, -3], [1, 0, 0]):
    print("solve with factors, b =", rhs, "->", sla.lu_solve((lu, piv), rhs))  # ... reuse
