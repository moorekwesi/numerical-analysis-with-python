# Chebyshev rational approximation of e^{-x} on [-1, 1], compared with Pade
import math
import numpy as np
from numpy.polynomial import chebyshev as C

f = lambda x: np.exp(-x)
n, m = 3, 2
N = n + m
a = C.chebinterpolate(f, 30)             # (essentially exact) Chebyshev coefficients of f

# Unknowns: p_0..p_n and q_1..q_m (q_0 = 1). Require the Chebyshev coefficients
# of  f*q - p  to vanish for T_0, ..., T_N.
M = np.zeros((N + 1, n + 1 + m))
for j in range(n + 1):
    M[j, j] = -1.0                        # -p_j contributes to T_j
for j in range(1, m + 1):
    col = C.chebmul(a, [0] * j + [1])     # coefficients of f(x) * T_j(x)
    M[:, n + j] = col[:N + 1]             # f * T_j
rhs = -a[:N + 1]                          # from the q_0 = 1 term: f * T_0
sol = np.linalg.solve(M, rhs)
p, q = sol[:n + 1], np.concatenate([[1.0], sol[n + 1:]])
print("numerator   (Chebyshev coefficients):", np.round(p, 6))
print("denominator (Chebyshev coefficients):", np.round(q, 6))

x = np.linspace(-1, 1, 4001)
rT = C.chebval(x, p) / C.chebval(x, q)
# Pade [3/2] of e^{-x} about 0 (from pade.py)
pade = (1 - 3 * x / 5 + 3 * x**2 / 20 - x**3 / 60) / (1 + 2 * x / 5 + x**2 / 20)
taylor5 = sum((-x) ** k / math.factorial(k) for k in range(6))
cheb5 = C.chebval(x, a[:6])               # truncated Chebyshev series of degree 5
for name, g in [("Taylor degree 5", taylor5), ("Chebyshev series deg 5", cheb5),
                ("Pade [3/2]", pade), ("Chebyshev rational [3/2]", rT)]:
    print(f"{name:26s}: max error on [-1,1] = {np.max(np.abs(f(x) - g)):.3e}")
