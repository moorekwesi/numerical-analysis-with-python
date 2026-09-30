# Successive over-relaxation (SOR) and the choice of the relaxation parameter omega
import numpy as np
import matplotlib.pyplot as plt


def sor(A, b, omega, x0, tol=1e-10, max_iter=1000):
    """SOR: x_i <- (1 - omega) x_i + omega * (Gauss-Seidel value of x_i)."""
    n = len(b)
    x = np.array(x0, dtype=float)
    for k in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            gs = (b[i] - A[i, :i] @ x[:i] - A[i, i + 1:] @ x_old[i + 1:]) / A[i, i]
            x[i] = (1 - omega) * x_old[i] + omega * gs
        if np.linalg.norm(x - x_old, np.inf) < tol * np.linalg.norm(x, np.inf):
            return x, k
    return x, max_iter


A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]], dtype=float)
b = np.array([24, 30, -24], dtype=float)

D = np.diag(np.diag(A))
L = -np.tril(A, -1)
U = -np.triu(A, 1)


def rho_sor(omega):
    T = np.linalg.solve(D - omega * L, (1 - omega) * D + omega * U)
    return np.max(np.abs(np.linalg.eigvals(T)))


for omega in [0.8, 1.0, 1.1, 1.2, 1.24, 1.25, 1.3, 1.5, 1.8, 1.95]:
    x, k = sor(A, b, omega, np.ones(3))
    print(f"omega = {omega:4.2f}: {k:3d} iterations, rho(T_omega) = {rho_sor(omega):.4f}")

rhoJ = np.max(np.abs(np.linalg.eigvals(np.linalg.solve(D, L + U))))
w_opt = 2 / (1 + np.sqrt(1 - rhoJ**2))
print(f"optimal omega = 2/(1+sqrt(1-rho_J^2)) = {w_opt:.6f}, rho = {rho_sor(w_opt):.6f}")

w = np.linspace(0.01, 1.99, 400)
plt.figure(figsize=(5.5, 3.3))
plt.plot(w, [rho_sor(t) for t in w])
plt.axvline(w_opt, ls="--", color="gray")
plt.xlabel(r"$\omega$")
plt.ylabel(r"$\rho(T_\omega)$")
plt.title("Spectral radius of the SOR iteration matrix")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch07_sor_rho.pdf")
