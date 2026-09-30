# Basins of attraction of Newton's method for z^3 - 1 = 0 in the complex plane
import numpy as np
import matplotlib.pyplot as plt

n = 600
x = np.linspace(-1.6, 1.6, n)
Z = x[None, :] + 1j * x[:, None]          # grid of starting points
with np.errstate(all="ignore"):
    for _ in range(40):
        Z = Z - (Z**3 - 1) / (3 * Z**2)   # 40 Newton steps for every point at once

roots = np.array([1, np.exp(2j * np.pi / 3), np.exp(-2j * np.pi / 3)])
basin = np.argmin(np.abs(Z[..., None] - roots), axis=-1)
for k, rt in enumerate(roots):
    print(f"root {rt:.4f}: {np.mean(basin == k) * 100:.1f}% of starting points")

plt.figure(figsize=(4.2, 4.2))
plt.imshow(basin, extent=[-1.6, 1.6, -1.6, 1.6], origin="lower", cmap="viridis")
plt.plot(roots.real, roots.imag, "w*", ms=10)
plt.xlabel("Re z")
plt.ylabel("Im z")
plt.title("Newton basins for $z^3 = 1$")
plt.tight_layout()
plt.savefig("ch04_fractal.png", dpi=150)
