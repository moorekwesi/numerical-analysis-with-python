# Fixed-point iteration x_{n+1} = g(x_n) for x^2 - 2x - 3 = 0 (roots 3 and -1)
import math
import numpy as np
import matplotlib.pyplot as plt


def fixed_point(g, x0, tol=1e-8, max_iter=50):
    """Iterate x_{n+1} = g(x_n) until |x_{n+1} - x_n| < tol.

    Returns the list of all iterates (so that we can study convergence)."""
    xs = [x0]
    for _ in range(max_iter):
        try:
            x_new = g(xs[-1])
        except (ValueError, ZeroDivisionError, OverflowError):
            break
        xs.append(x_new)
        if abs(xs[-1] - xs[-2]) < tol or abs(x_new) > 1e8:
            break
    return xs


g1 = lambda x: math.sqrt(2 * x + 3)      # g1'(3) = 1/3
g2 = lambda x: 3 / (x - 2)               # g2'(3) = -3
g3 = lambda x: (x**2 - 3) / 2            # g3'(3) = 3

for name, g in [("g1 = sqrt(2x+3)", g1), ("g2 = 3/(x-2)", g2), ("g3 = (x^2-3)/2", g3)]:
    xs = fixed_point(g, 4.0, max_iter=60)
    shown = ", ".join(f"{x:.6f}" for x in xs[:7])
    print(f"{name:16s}: {shown}, ...  ({len(xs) - 1} its, last = {xs[-1]:.6g})")

# Error ratios for g1: |x_{n+1}-3| / |x_n-3|  ->  |g1'(3)| = 1/3
xs = fixed_point(g1, 4.0, tol=1e-14)
print("\n n     x_n              |e_n|        |e_n|/|e_{n-1}|")
for n, x in enumerate(xs[:12]):
    e = abs(x - 3)
    ratio = e / abs(xs[n - 1] - 3) if n > 0 else float("nan")
    print(f"{n:2d}  {x:.12f}  {e:.3e}   {ratio:.6f}")

# Cobweb diagrams
fig, axes = plt.subplots(1, 2, figsize=(8, 3.6))
for ax, g, x0, title, lim in [(axes[0], g1, 4.0, r"$g(x)=\sqrt{2x+3}$ (converges)", (0, 5)),
                              (axes[1], g3, 3.1, r"$g(x)=(x^2-3)/2$ (diverges)", (2.5, 5))]:
    xx = np.linspace(*lim, 200)
    ax.plot(xx, [g(t) for t in xx], label="y = g(x)")
    ax.plot(xx, xx, "k--", lw=0.8, label="y = x")
    xs = fixed_point(g, x0, max_iter=6)
    for k in range(len(xs) - 1):
        ax.plot([xs[k], xs[k]], [xs[k], xs[k + 1]], "r", lw=0.8)
        ax.plot([xs[k], xs[k + 1]], [xs[k + 1], xs[k + 1]], "r", lw=0.8)
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_title(title, fontsize=10)
    ax.legend(fontsize=8, loc="upper left")
plt.tight_layout()
plt.savefig("ch04_cobweb.pdf")
