# Composite trapezoidal and Simpson rules: convergence rates
import numpy as np
import matplotlib.pyplot as plt


def composite_trapezoid(f, a, b, n):
    """n subintervals of width h = (b-a)/n."""
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + y[1:-1].sum() + 0.5 * y[-1])


def composite_simpson(f, a, b, n):
    """n subintervals (n must be even)."""
    if n % 2:
        raise ValueError("n must be even for Simpson's rule")
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h / 3 * (y[0] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum() + y[-1])


exact = 2.0                                      # integral of sin over [0, pi]
print("  n     trapezoid error  ratio   Simpson error   ratio")
ns = [2, 4, 8, 16, 32, 64, 128]
et, es = [], []
for n in ns:
    et.append(abs(composite_trapezoid(np.sin, 0, np.pi, n) - exact))
    es.append(abs(composite_simpson(np.sin, 0, np.pi, n) - exact))
    rt = f"{et[-2] / et[-1]:6.2f}" if len(et) > 1 else "      "
    rs = f"{es[-2] / es[-1]:6.2f}" if len(es) > 1 else "      "
    print(f"{n:4d}   {et[-1]:14.3e}  {rt}   {es[-1]:13.3e}  {rs}")

# A periodic integrand: the trapezoidal rule converges exponentially fast!
f = lambda x: np.exp(np.cos(x))
exact_p = 7.954926521012845                      # = 2 pi I_0(1)
print("\nperiodic integrand e^{cos x} on [0, 2 pi]:")
for n in [2, 4, 8, 12, 16]:
    print(f"  n = {n:2d}: trapezoid error = {abs(composite_trapezoid(f, 0, 2 * np.pi, n) - exact_p):.2e}")

hs = [np.pi / n for n in ns]
plt.figure(figsize=(5.5, 3.6))
plt.loglog(hs, et, "o-", label="composite trapezoid")
plt.loglog(hs, es, "s-", label="composite Simpson")
plt.loglog(hs, 0.2 * np.array(hs) ** 2, "k:", label="slope 2")
plt.loglog(hs, 0.01 * np.array(hs) ** 4, "k--", label="slope 4")
plt.xlabel("h")
plt.ylabel("error")
plt.legend(fontsize=8)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch13_composite.pdf")
