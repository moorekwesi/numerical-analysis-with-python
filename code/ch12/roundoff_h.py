# Truncation error versus rounding error: the best step size h
import numpy as np
import matplotlib.pyplot as plt

f, df, x0 = np.sin, np.cos, 1.0
hs = 10.0 ** np.arange(-1, -16.5, -0.25)
err_fwd = [abs((f(x0 + h) - f(x0)) / h - df(x0)) for h in hs]
err_cen = [abs((f(x0 + h) - f(x0 - h)) / (2 * h) - df(x0)) for h in hs]

i, j = int(np.argmin(err_fwd)), int(np.argmin(err_cen))
eps = np.finfo(float).eps
print(f"forward : best h = {hs[i]:.1e}, error = {err_fwd[i]:.1e}   (theory: h ~ sqrt(eps) = {np.sqrt(eps):.1e})")
print(f"central : best h = {hs[j]:.1e}, error = {err_cen[j]:.1e}   (theory: h ~ eps^(1/3) = {eps ** (1 / 3):.1e})")
for h in [1e-2, 1e-5, 1e-8, 1e-11, 1e-14]:
    print(f"h = {h:.0e}: forward error {abs((f(x0 + h) - f(x0)) / h - df(x0)):.2e}, "
          f"central error {abs((f(x0 + h) - f(x0 - h)) / (2 * h) - df(x0)):.2e}")

plt.figure(figsize=(6, 3.8))
plt.loglog(hs, err_fwd, "o-", ms=3, label="forward difference")
plt.loglog(hs, err_cen, "s-", ms=3, label="central difference")
plt.loglog(hs, 0.5 * hs * abs(np.sin(x0)), "k:", lw=1, label="truncation ~ h")
plt.loglog(hs, eps / hs, "k--", lw=1, label="rounding ~ eps/h")
plt.ylim(1e-12, 1)
plt.xlabel("h")
plt.ylabel("error in f'(1)")
plt.legend(fontsize=8)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch12_roundoff.pdf")
