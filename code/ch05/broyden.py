# Broyden's quasi-Newton method compared with Newton's method
import numpy as np


def F(v):
    x, y = v
    return np.array([x**2 + y**2 - 4, x * y - 1])


def J(v):
    x, y = v
    return np.array([[2 * x, 2 * y], [y, x]])


def newton(x, tol=1e-12):
    errs = []
    for k in range(50):
        dx = np.linalg.solve(J(x), -F(x))
        x = x + dx
        errs.append(np.linalg.norm(dx))
        if errs[-1] < tol:
            return x, errs
    return x, errs


def broyden(x, B, tol=1e-12):
    """Broyden's 'good' method: B approximates the Jacobian and is updated by a
    rank-one correction so that B_new (x_new - x) = F(x_new) - F(x)."""
    errs = []
    Fx = F(x)
    for k in range(100):
        s = np.linalg.solve(B, -Fx)
        x_new = x + s
        F_new = F(x_new)
        yv = F_new - Fx
        B = B + np.outer(yv - B @ s, s) / (s @ s)
        x, Fx = x_new, F_new
        errs.append(np.linalg.norm(s))
        if errs[-1] < tol:
            return x, errs
    return x, errs


x0 = np.array([2.0, 1.0])
xn, en = newton(x0)
xb, eb = broyden(x0, J(x0))       # start from the exact Jacobian at x0 only
print("Newton :", xn, f"{len(en)} iterations (each needs the Jacobian)")
print("Broyden:", xb, f"{len(eb)} iterations (Jacobian evaluated once)")
print("step sizes Newton :", " ".join(f"{e:.1e}" for e in en))
print("step sizes Broyden:", " ".join(f"{e:.1e}" for e in eb))
print("exact: x = sqrt(2+sqrt3) =", np.sqrt(2 + np.sqrt(3)), " y = 1/x =", 1 / np.sqrt(2 + np.sqrt(3)))
