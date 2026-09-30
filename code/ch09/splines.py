# Piecewise interpolation: linear and cubic splines for the Runge function
import numpy as np
from scipy.interpolate import CubicSpline

f = lambda x: 1 / (1 + 25 * x**2)
t = np.linspace(-1, 1, 4001)
print("  n    piecewise linear     natural cubic spline   not-a-knot spline")
for n in [8, 16, 32, 64, 128]:
    x = np.linspace(-1, 1, n + 1)
    lin = np.interp(t, x, f(x))
    nat = CubicSpline(x, f(x), bc_type="natural")(t)
    nak = CubicSpline(x, f(x))(t)                 # default end condition
    print(f"{n:4d}   {np.max(np.abs(lin - f(t))):14.3e}   {np.max(np.abs(nat - f(t))):18.3e}"
          f"   {np.max(np.abs(nak - f(t))):16.3e}")
