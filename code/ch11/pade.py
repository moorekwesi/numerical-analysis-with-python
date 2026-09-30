# Pade approximation of e^{-x}: r(x) = p(x)/q(x) with deg p = n, deg q = m
import math
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import pade


def pade_coefficients(a, n, m):
    """Pade approximant from Maclaurin coefficients a[0..n+m] (exact fractions).

    Solves  sum_{j=0}^{k} a_{k-j} q_j = p_k  (k = 0..n+m), with q_0 = 1,
    p_k = 0 for k > n and q_j = 0 for j > m."""
    N = n + m
    # equations k = n+1..N determine q_1..q_m
    M = [[a[k - j] if k - j >= 0 else Fraction(0) for j in range(1, m + 1)]
         for k in range(n + 1, N + 1)]
    rhs = [-a[k] for k in range(n + 1, N + 1)]
    # Gaussian elimination in exact rational arithmetic
    for c in range(m):
        piv = next(r for r in range(c, m) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        rhs[c], rhs[piv] = rhs[piv], rhs[c]
        for r in range(m):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
                rhs[r] -= f * rhs[c]
    q = [Fraction(1)] + [rhs[i] / M[i][i] for i in range(m)]
    p = [sum(a[k - j] * q[j] for j in range(0, min(k, m) + 1)) for k in range(n + 1)]
    return p, q


a = [Fraction((-1) ** k, math.factorial(k)) for k in range(6)]     # e^{-x}
p, q = pade_coefficients(a, 3, 2)
print("p:", [str(c) for c in p])
print("q:", [str(c) for c in q])

# the same with SciPy (floating point); note: pade returns numpy poly1d objects
P, Q = pade([float(c) for c in a], 2)          # 2 = degree of the denominator
print("scipy p:", P.coeffs[::-1])
print("scipy q:", Q.coeffs[::-1] / Q.coeffs[-1])

r = lambda x: np.polyval([float(c) for c in p[::-1]], x) / np.polyval([float(c) for c in q[::-1]], x)
taylor5 = lambda x: sum(float(c) * x**k for k, c in enumerate(a))
print("\n  x      e^-x        Taylor P5    error       Pade r32     error")
for x in [0.2, 0.4, 0.6, 0.8, 1.0]:
    e = math.exp(-x)
    print(f"{x:.1f}  {e:.8f}  {taylor5(x):.8f}  {abs(e - taylor5(x)):.2e}  {r(x):.8f}  {abs(e - r(x)):.2e}")

xs = np.linspace(0, 3, 400)
plt.figure(figsize=(6, 3.4))
plt.semilogy(xs, np.abs(np.exp(-xs) - taylor5(xs)) + 1e-17, label="Taylor, degree 5")
plt.semilogy(xs, np.abs(np.exp(-xs) - r(xs)) + 1e-17, label="Pade [3/2]")
plt.xlabel("x")
plt.ylabel("absolute error")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch11_pade.pdf")
