# Vector and matrix norms, and the spectral radius
import numpy as np

x = np.array([-1.0, 1.0, 2.0])
print("x =", x)
print("||x||_1   =", np.linalg.norm(x, 1))
print("||x||_2   =", np.linalg.norm(x), "= sqrt(6) =", np.sqrt(6))
print("||x||_inf =", np.linalg.norm(x, np.inf))

xhat = np.array([1.2001, 0.9991, 0.9250])
xtrue = np.ones(3)
print("\n||x - xhat||_2   =", np.linalg.norm(xtrue - xhat))
print("||x - xhat||_inf =", np.linalg.norm(xtrue - xhat, np.inf))

A = np.array([[1, 2, -1], [0, 3, -1], [5, -1, 1]], dtype=float)
print("\nA =\n", A)
print("||A||_1   (max column sum) =", np.abs(A).sum(axis=0).max(), "  numpy:", np.linalg.norm(A, 1))
print("||A||_inf (max row sum)    =", np.abs(A).sum(axis=1).max(), "  numpy:", np.linalg.norm(A, np.inf))
rho_AtA = np.max(np.abs(np.linalg.eigvals(A.T @ A)))
print("||A||_2 = sqrt(rho(A^T A)) =", np.sqrt(rho_AtA), "  numpy:", np.linalg.norm(A, 2))
print("||A||_F (Frobenius)        =", np.linalg.norm(A, "fro"))
print("eigenvalues of A:", np.round(np.linalg.eigvals(A), 6))
print("spectral radius rho(A)     =", np.max(np.abs(np.linalg.eigvals(A))))

# rho(A) <= ||A|| for every induced norm, but ||A|| can be much larger than rho(A)
B = np.array([[0.5, 10.0], [0.0, 0.5]])
print("\nB = [[0.5, 10], [0, 0.5]]:  rho(B) =", 0.5, "  ||B||_inf =", np.linalg.norm(B, np.inf))
for k in [1, 5, 10, 20, 40, 80]:
    print(f"   ||B^{k:<2d}||_inf = {np.linalg.norm(np.linalg.matrix_power(B, k), np.inf):.4e}")
