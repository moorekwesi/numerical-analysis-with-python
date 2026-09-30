# The unit "circles" {x : ||x||_p = 1} in R^2 for several p
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 800)
plt.figure(figsize=(4.2, 4.2))
for p, style in [(1, "-"), (1.5, ":"), (2, "-"), (4, "--"), (np.inf, "-")]:
    c, s = np.cos(t), np.sin(t)
    if p == np.inf:
        r = 1 / np.maximum(np.abs(c), np.abs(s))
    else:
        r = 1 / (np.abs(c) ** p + np.abs(s) ** p) ** (1 / p)
    label = r"$p=\infty$" if p == np.inf else f"$p={p}$"
    plt.plot(r * c, r * s, style, label=label)
plt.gca().set_aspect("equal")
plt.axhline(0, color="gray", lw=0.5)
plt.axvline(0, color="gray", lw=0.5)
plt.legend(fontsize=8, loc="center")
plt.title(r"$\|x\|_p = 1$")
plt.tight_layout()
plt.savefig("ch08_unitballs.pdf")
