# Least-squares straight line: normal equations, lstsq and polyfit
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([-1.0, 3.0, 7.0, 10.0])

# design matrix: columns 1 and x
A = np.column_stack([np.ones_like(x), x])
print("A^T A =\n", A.T @ A, "\nA^T y =", A.T @ y)
a_normal = np.linalg.solve(A.T @ A, A.T @ y)          # normal equations
a_lstsq, res, rank, sv = np.linalg.lstsq(A, y, rcond=None)   # QR/SVD based
a_poly = np.polyfit(x, y, 1)                           # highest power first!
print("normal equations: a0, a1 =", a_normal)
print("np.linalg.lstsq : a0, a1 =", a_lstsq)
print("np.polyfit      : a1, a0 =", a_poly)
r = y - A @ a_normal
print("residuals r =", r, "  sum of squares E =", r @ r)
print("A^T r =", A.T @ r, " (residual is orthogonal to the columns of A)")

plt.figure(figsize=(5, 3.4))
plt.plot(x, y, "o", label="data")
t = np.linspace(0.5, 4.5, 10)
plt.plot(t, a_normal[0] + a_normal[1] * t, label=f"y = {a_normal[0]:.1f} + {a_normal[1]:.1f}x")
for xi, yi, fi in zip(x, y, A @ a_normal):
    plt.plot([xi, xi], [yi, fi], "r:", lw=1)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch10_linefit.pdf")
