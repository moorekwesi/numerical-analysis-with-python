# Richardson extrapolation of the central difference
import numpy as np


def richardson_table(D, h, levels):
    """R[i][0] = D(h / 2^i);  R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / (4^j - 1).

    Valid when the error of D has an expansion in EVEN powers of h (central differences)."""
    R = np.zeros((levels, levels))
    for i in range(levels):
        R[i, 0] = D(h / 2**i)
        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)
    return R


f = lambda x: x * np.exp(x)
x0, exact = 2.0, 3 * np.exp(2.0)
central = lambda h: (f(x0 + h) - f(x0 - h)) / (2 * h)
R = richardson_table(central, 0.4, 5)
print("Richardson table for f'(2), f(x) = x e^x, starting with h = 0.4")
for i in range(5):
    print("  ".join(f"{R[i, j]:.10f}" for j in range(i + 1)))
print(f"exact f'(2) = {exact:.10f}")
print("errors on the diagonal:", " ".join(f"{abs(R[i, i] - exact):.1e}" for i in range(5)))
