# Gauss-Legendre quadrature
import numpy as np
from math import erf, sqrt, pi


def gauss_legendre(f, a, b, n):
    """n-point Gauss-Legendre rule on [a, b] (exact for polynomials of degree 2n-1)."""
    x, w = np.polynomial.legendre.leggauss(n)          # nodes/weights on [-1, 1]
    t = (b - a) / 2 * x + (a + b) / 2                  # change of variable
    return (b - a) / 2 * np.sum(w * f(t))


for n in [1, 2, 3, 4]:
    x, w = np.polynomial.legendre.leggauss(n)
    print(f"n = {n}: nodes = {np.round(x, 10)}, weights = {np.round(w, 10)}")

f = lambda x: np.exp(-x**2)
exact = sqrt(pi) / 2 * (erf(1.5) - erf(1.0))
print(f"\nintegral of exp(-x^2) over [1, 1.5] = {exact:.10f}")
for n in [2, 3, 4, 5]:
    g = gauss_legendre(f, 1.0, 1.5, n)
    print(f"  Gauss, n = {n}: {g:.10f}   error = {abs(g - exact):.2e}")
x = np.linspace(1.0, 1.5, 5)            # Simpson with 5 points, for comparison
s = 0.125 / 3 * (f(x[0]) + 4 * f(x[1]) + 2 * f(x[2]) + 4 * f(x[3]) + f(x[4]))
print(f"  Simpson, 5 points: {s:.10f}   error = {abs(s - exact):.2e}")

print("\nDegree of precision of the 3-point rule on [-1, 1]:")
for k in range(8):
    exact_k = (1 - (-1) ** (k + 1)) / (k + 1)
    val = gauss_legendre(lambda t: t**k, -1, 1, 3)
    print(f"  x^{k}: rule = {val:+.12f}, exact = {exact_k:+.12f}")
