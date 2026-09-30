# Adaptive Simpson quadrature
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

evaluations = []                             # record every x at which f is evaluated


def f(x):
    evaluations.append(x)
    return 100 / x**2 * np.sin(10 / x)


def simpson(fa, fm, fb, a, b):
    return (b - a) / 6 * (fa + 4 * fm + fb)


def adaptive_simpson(f, a, b, tol):
    """Integrate f over [a, b] with estimated absolute error below tol."""
    fa, fm, fb = f(a), f((a + b) / 2), f(b)
    whole = simpson(fa, fm, fb, a, b)
    return _asr(f, a, b, fa, fm, fb, whole, tol, depth=0)


def _asr(f, a, b, fa, fm, fb, whole, tol, depth):
    m = (a + b) / 2
    lm, rm = (a + m) / 2, (m + b) / 2
    flm, frm = f(lm), f(rm)                  # only two new evaluations per call
    left = simpson(fa, flm, fm, a, m)
    right = simpson(fm, frm, fb, m, b)
    err = (left + right - whole) / 15        # error estimate of left + right
    if abs(err) < tol or depth > 50:
        return left + right + err            # accept (with Richardson correction)
    return (_asr(f, a, m, fa, flm, fm, left, tol / 2, depth + 1) +
            _asr(f, m, b, fm, frm, fb, right, tol / 2, depth + 1))


exact = 10 * (np.cos(10 / 3) - np.cos(10))   # exact value, by the substitution t = 10/x
for tol in [1e-3, 1e-6, 1e-9]:
    evaluations.clear()
    val = adaptive_simpson(f, 1.0, 3.0, tol)
    print(f"tol = {tol:.0e}: integral = {val:.12f}, error = {abs(val - exact):.1e}, "
          f"{len(evaluations)} function evaluations")

ref, est = quad(lambda x: 100 / x**2 * np.sin(10 / x), 1, 3, epsabs=1e-13, limit=200)
print(f"scipy.integrate.quad: {ref:.13f}, error = {abs(ref - exact):.1e} (its own estimate {est:.1e})")
print(f"exact value         : {exact:.13f}")

# how many points would composite Simpson need for the same accuracy?
for n in [64, 128, 256, 512]:
    x = np.linspace(1, 3, n + 1)
    y = 100 / x**2 * np.sin(10 / x)
    s = (2 / n) / 3 * (y[0] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum() + y[-1])
    print(f"composite Simpson, {n + 1:4d} points: error = {abs(s - exact):.1e}")

evaluations.clear()
adaptive_simpson(f, 1.0, 3.0, 1e-4)
xs = np.linspace(1, 3, 1000)
plt.figure(figsize=(6.5, 3.4))
plt.plot(xs, 100 / xs**2 * np.sin(10 / xs), lw=1)
pts = np.array(sorted(set(evaluations)))
plt.plot(pts, np.full(pts.size, -80), "|", color="C3", ms=10)
plt.title(f"Adaptive Simpson (tol = 1e-4): {pts.size} points, dense where f varies rapidly",
          fontsize=9)
plt.xlabel("x")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch13_adaptive.pdf")
