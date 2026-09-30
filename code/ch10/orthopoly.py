# Legendre and Chebyshev polynomials: recurrences, orthogonality and plots
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def legendre(n, x):
    """P_n(x) by the three-term recurrence (k+1) P_{k+1} = (2k+1) x P_k - k P_{k-1}."""
    p0, p1 = np.ones_like(x), x
    if n == 0:
        return p0
    for k in range(1, n):
        p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
    return p1


def chebyshev(n, x):
    """T_n(x) by the recurrence T_{k+1} = 2x T_k - T_{k-1}."""
    t0, t1 = np.ones_like(x), x
    if n == 0:
        return t0
    for _ in range(1, n):
        t0, t1 = t1, 2 * x * t1 - t0
    return t1


print("Gram matrix <P_i, P_j> on [-1,1] (should be diagonal with 2/(2i+1)):")
G = np.array([[quad(lambda x: legendre(i, x) * legendre(j, x), -1, 1)[0]
               for j in range(4)] for i in range(4)])
G[np.abs(G) < 1e-12] = 0.0                                # hide rounding noise
print(np.round(G, 10))
print("Chebyshev Gram matrix with weight 1/sqrt(1-x^2):")
Gc = np.array([[quad(lambda th: chebyshev(i, np.cos(th)) * chebyshev(j, np.cos(th)), 0, np.pi)[0]
                for j in range(4)] for i in range(4)])     # substitution x = cos(theta)
Gc[np.abs(Gc) < 1e-12] = 0.0
print(np.round(Gc, 10))

x = np.linspace(-1, 1, 400)
fig, ax = plt.subplots(1, 2, figsize=(8.5, 3.2), sharey=True)
for n in range(6):
    ax[0].plot(x, legendre(n, x), label=f"$P_{n}$")
    ax[1].plot(x, chebyshev(n, x), label=f"$T_{n}$")
ax[0].set_title("Legendre polynomials", fontsize=10)
ax[1].set_title("Chebyshev polynomials", fontsize=10)
for a in ax:
    a.grid(alpha=0.3)
    a.legend(fontsize=7, ncol=3, loc="lower right")
plt.tight_layout()
plt.savefig("ch10_orthopoly.pdf")
