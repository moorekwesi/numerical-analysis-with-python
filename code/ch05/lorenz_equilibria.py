# Equilibria of the Lorenz system with Newton's method and a finite-difference Jacobian
import numpy as np

sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0


def lorenz(v):
    x, y, z = v
    return np.array([sigma * (y - x),
                     rho * x - y - x * z,
                     x * y - beta * z])


def jacobian_exact(v):
    x, y, z = v
    return np.array([[-sigma, sigma, 0.0],
                     [rho - z, -1.0, -x],
                     [y, x, -beta]])


def jacobian_fd(F, x, h=1e-7):
    """Forward-difference approximation of the Jacobian: column j is
    (F(x + h e_j) - F(x)) / h."""
    n = len(x)
    Fx = F(x)
    Jm = np.zeros((n, n))
    for j in range(n):
        xh = x.copy()
        step = h * max(1.0, abs(x[j]))
        xh[j] += step
        Jm[:, j] = (F(xh) - Fx) / step
    return Jm


def newton(F, x0, jac=None, tol=1e-12, max_iter=50):
    x = np.array(x0, dtype=float)
    for k in range(1, max_iter + 1):
        Jm = jac(x) if jac is not None else jacobian_fd(F, x)
        dx = np.linalg.solve(Jm, -F(x))
        x += dx
        if np.linalg.norm(dx) < tol * (1 + np.linalg.norm(x)):
            return x, k
    raise RuntimeError("no convergence")


x0 = np.array([-1.0, 0.0, 1.05])
print("difference between exact and FD Jacobian at x0:",
      np.max(np.abs(jacobian_exact(x0) - jacobian_fd(lorenz, x0))))
for start in ([-1.0, 0.0, 1.05], [5.0, 5.0, 20.0], [-5.0, -5.0, 20.0]):
    xe, k = newton(lorenz, start, jacobian_exact)
    xf, kf = newton(lorenz, start)          # finite-difference Jacobian
    print(f"start {start}: exact J -> {np.round(xe, 10)} ({k} its), "
          f"FD J -> {kf} its")
c = np.sqrt(beta * (rho - 1))
print(f"theory: (0,0,0) and (+-{c:.10f}, +-{c:.10f}, {rho - 1})")
