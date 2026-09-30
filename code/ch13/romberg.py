# Romberg integration = composite trapezoid + Richardson extrapolation
import numpy as np


def romberg(f, a, b, levels):
    """R[k, 0] = trapezoid with 2^k subintervals, reusing old function values;
    R[k, j] = R[k, j-1] + (R[k, j-1] - R[k-1, j-1]) / (4^j - 1)."""
    R = np.zeros((levels, levels))
    h = b - a
    R[0, 0] = h / 2 * (f(a) + f(b))
    for k in range(1, levels):
        h /= 2
        new_points = a + h * np.arange(1, 2**k, 2)           # only the NEW midpoints
        R[k, 0] = R[k - 1, 0] / 2 + h * np.sum(f(new_points))
        for j in range(1, k + 1):
            R[k, j] = R[k, j - 1] + (R[k, j - 1] - R[k - 1, j - 1]) / (4**j - 1)
    return R


R = romberg(np.sin, 0, np.pi, 6)
print("Romberg table for the integral of sin x over [0, pi] (exact value 2):")
for k in range(6):
    print("  ".join(f"{R[k, j]:.10f}" for j in range(k + 1)))
print("error of R[5,5] =", abs(R[5, 5] - 2), " using", 2**5 + 1, "function values")
