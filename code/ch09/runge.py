# Runge's phenomenon: equally spaced versus Chebyshev nodes
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator

f = lambda x: 1 / (1 + 25 * x**2)
t = np.linspace(-1, 1, 2001)

print("  n   max error (equispaced)   max error (Chebyshev)")
for n in [4, 8, 12, 16, 20, 40]:
    xe = np.linspace(-1, 1, n + 1)
    xc = np.cos((2 * np.arange(n + 1) + 1) * np.pi / (2 * n + 2))   # Chebyshev nodes
    pe = BarycentricInterpolator(xe, f(xe))
    pc = BarycentricInterpolator(xc, f(xc))
    print(f"{n:3d}   {np.max(np.abs(f(t) - pe(t))):18.4e}   {np.max(np.abs(f(t) - pc(t))):18.4e}")

n = 12
xe = np.linspace(-1, 1, n + 1)
xc = np.cos((2 * np.arange(n + 1) + 1) * np.pi / (2 * n + 2))
fig, ax = plt.subplots(1, 2, figsize=(8.5, 3.3), sharey=True)
for a, xn, title in [(ax[0], xe, "13 equally spaced nodes"), (ax[1], xc, "13 Chebyshev nodes")]:
    a.plot(t, f(t), "k", lw=1, label="$f(x)=1/(1+25x^2)$")
    a.plot(t, BarycentricInterpolator(xn, f(xn))(t), "C3", label="$P_{12}$")
    a.plot(xn, f(xn), "o", ms=4)
    a.set_ylim(-1.5, 2.2)
    a.set_title(title, fontsize=10)
    a.grid(alpha=0.3)
ax[0].legend(fontsize=8, loc="upper center")
plt.tight_layout()
plt.savefig("ch09_runge.pdf")
