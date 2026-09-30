# Jacobi and Gauss-Seidel iterations
import numpy as np


def jacobi(A, b, x0, tol=1e-10, max_iter=500):
    """Jacobi: every component of x^(k+1) uses only the OLD vector x^(k)."""
    n = len(b)
    x = np.array(x0, dtype=float)
    history = [x.copy()]
    for k in range(1, max_iter + 1):
        x_new = np.empty(n)
        for i in range(n):
            s = A[i, :i] @ x[:i] + A[i, i + 1:] @ x[i + 1:]
            x_new[i] = (b[i] - s) / A[i, i]
        history.append(x_new.copy())
        if np.linalg.norm(x_new - x, np.inf) < tol * np.linalg.norm(x_new, np.inf):
            return x_new, k, history
        x = x_new
    raise RuntimeError("Jacobi did not converge")


def gauss_seidel(A, b, x0, tol=1e-10, max_iter=500):
    """Gauss-Seidel: new components are used as soon as they are computed."""
    n = len(b)
    x = np.array(x0, dtype=float)
    history = [x.copy()]
    for k in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            s = A[i, :i] @ x[:i] + A[i, i + 1:] @ x_old[i + 1:]   # x[:i] already updated
            x[i] = (b[i] - s) / A[i, i]
        history.append(x.copy())
        if np.linalg.norm(x - x_old, np.inf) < tol * np.linalg.norm(x, np.inf):
            return x, k, history
    raise RuntimeError("Gauss-Seidel did not converge")


A = np.array([[4, 3, 0], [3, 4, -1], [0, -1, 4]], dtype=float)
b = np.array([24, 30, -24], dtype=float)
x0 = np.ones(3)
xs = np.array([3.0, 4.0, -5.0])

xj, kj, hj = jacobi(A, b, x0)
xg, kg, hg = gauss_seidel(A, b, x0)
print(" k        Jacobi x^(k)                    Gauss-Seidel x^(k)")
for k in range(6):
    print(f"{k:2d}  {np.array2string(hj[k], precision=4, floatmode='fixed')}"
          f"   {np.array2string(hg[k], precision=4, floatmode='fixed')}")
print(f"Jacobi      : {kj} iterations, x = {xj}")
print(f"Gauss-Seidel: {kg} iterations, x = {xg}")

# Iteration matrices from the splitting A = D - L - U
D = np.diag(np.diag(A))
L = -np.tril(A, -1)
U = -np.triu(A, 1)
TJ = np.linalg.solve(D, L + U)
TG = np.linalg.solve(D - L, U)
rho = lambda T: np.max(np.abs(np.linalg.eigvals(T)))
print(f"rho(T_J) = {rho(TJ):.6f},  rho(T_GS) = {rho(TG):.6f},  rho(T_J)^2 = {rho(TJ)**2:.6f}")
