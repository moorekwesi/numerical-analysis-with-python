# Steepest descent and conjugate gradients for a symmetric positive definite system
import numpy as np
import matplotlib.pyplot as plt


def steepest_descent(A, b, x0, tol=1e-10, max_iter=10000):
    x = np.array(x0, dtype=float)
    path = [x.copy()]
    for k in range(1, max_iter + 1):
        r = b - A @ x                     # residual = -gradient of phi
        t = (r @ r) / (r @ (A @ r))       # exact line search
        x = x + t * r
        path.append(x.copy())
        if np.linalg.norm(r) < tol * np.linalg.norm(b):
            break
    return x, k, np.array(path)


def conjugate_gradient(A, b, x0, tol=1e-10, max_iter=None):
    """Hestenes-Stiefel conjugate gradient method."""
    x = np.array(x0, dtype=float)
    r = b - A @ x
    p = r.copy()
    rr = r @ r
    path = [x.copy()]
    max_iter = max_iter or 10 * len(b)
    for k in range(1, max_iter + 1):
        Ap = A @ p
        alpha = rr / (p @ Ap)             # step length
        x = x + alpha * p
        r = r - alpha * Ap
        path.append(x.copy())
        rr_new = r @ r
        if np.sqrt(rr_new) < tol * np.linalg.norm(b):
            break
        p = r + (rr_new / rr) * p         # new direction, A-conjugate to the old ones
        rr = rr_new
    return x, k, np.array(path)


A = np.array([[4.0, 1.0], [1.0, 3.0]])
b = np.array([1.0, 2.0])
x0 = np.array([2.0, 1.0])
xs, ks, ps = steepest_descent(A, b, x0)
xc, kc, pc = conjugate_gradient(A, b, x0)
print("exact solution    :", np.linalg.solve(A, b))
print(f"steepest descent  : {xs}  ({ks} iterations)")
print(f"conjugate gradient: {xc}  ({kc} iterations)")
lam = np.linalg.eigvalsh(A)
kappa = lam[-1] / lam[0]
print(f"kappa = {kappa:.4f},  SD rate (kappa-1)/(kappa+1) = {(kappa - 1) / (kappa + 1):.4f}")

# picture: contours of phi(x) = x^T A x / 2 - b^T x and the two paths
X, Y = np.meshgrid(np.linspace(-0.6, 2.2, 200), np.linspace(-0.2, 1.4, 200))
P = 0.5 * (A[0, 0] * X**2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y**2) - b[0] * X - b[1] * Y
plt.figure(figsize=(6, 3.6))
plt.contour(X, Y, P, levels=20, colors="lightgray")
plt.plot(ps[:12, 0], ps[:12, 1], "o-", ms=3, label="steepest descent")
plt.plot(pc[:, 0], pc[:, 1], "s-", ms=4, label="conjugate gradient")
plt.gca().set_aspect("equal")
plt.legend()
plt.title(r"Minimising $\phi(x)=\frac{1}{2} x^TAx-b^Tx$")
plt.tight_layout()
plt.savefig("ch07_sd_cg.pdf")
