# The Thomas algorithm for tridiagonal systems (O(n) operations)
import numpy as np


def thomas(a, d, c, b):
    """Solve a tridiagonal system.

    a: sub-diagonal (length n-1), d: diagonal (n), c: super-diagonal (n-1), b: rhs (n).
    This is LU factorisation without pivoting specialised to tridiagonal matrices."""
    n = len(d)
    d = np.array(d, dtype=float)
    b = np.array(b, dtype=float)
    for i in range(1, n):                 # elimination
        m = a[i - 1] / d[i - 1]
        d[i] -= m * c[i - 1]
        b[i] -= m * b[i - 1]
    x = np.zeros(n)
    x[-1] = b[-1] / d[-1]
    for i in range(n - 2, -1, -1):        # back substitution
        x[i] = (b[i] - c[i] * x[i + 1]) / d[i]
    return x


# -u'' = pi^2 sin(pi x) on (0,1), u(0) = u(1) = 0; exact solution u = sin(pi x)
for n in [10, 100, 1000, 10000]:
    h = 1.0 / (n + 1)
    xg = np.linspace(h, 1 - h, n)
    rhs = h**2 * np.pi**2 * np.sin(np.pi * xg)
    u = thomas(-np.ones(n - 1), 2 * np.ones(n), -np.ones(n - 1), rhs)
    print(f"n = {n:5d}: max error = {np.max(np.abs(u - np.sin(np.pi * xg))):.3e}")
