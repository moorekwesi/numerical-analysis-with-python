# Interpolation by the method of undetermined coefficients (a Vandermonde system)
import numpy as np

x = np.array([0.0, 0.5, 1.0])
y = np.array([1.0000, 1.6487, 2.7183])        # values of e^x
V = np.vander(x, increasing=True)              # columns 1, x, x^2
a = np.linalg.solve(V, y)
print("Vandermonde matrix:\n", V)
print("coefficients a0, a1, a2 =", a)
p = lambda t: a[0] + a[1] * t + a[2] * t**2
print(f"P2(0.25) = {p(0.25):.6f},   e^0.25 = {np.exp(0.25):.6f}")

# The Vandermonde matrix becomes extremely ill-conditioned as n grows
print("\n  n   cond(V) for equally spaced nodes in [0,1]")
for n in [5, 10, 15, 20, 25]:
    xs = np.linspace(0, 1, n)
    print(f"{n:3d}   {np.linalg.cond(np.vander(xs, increasing=True)):.3e}")
