# Lagrange interpolation
import numpy as np
import matplotlib.pyplot as plt


def lagrange_basis(xnodes, k, t):
    """The k-th Lagrange cardinal polynomial L_k evaluated at t."""
    L = np.ones_like(t, dtype=float)
    for j, xj in enumerate(xnodes):
        if j != k:
            L *= (t - xj) / (xnodes[k] - xj)
    return L


def lagrange_interp(xnodes, ynodes, t):
    """P_n(t) = sum_k y_k L_k(t)."""
    t = np.asarray(t, dtype=float)
    return sum(yk * lagrange_basis(xnodes, k, t) for k, yk in enumerate(ynodes))


x = np.array([0.0, 0.5, 1.0])
y = np.array([1.0000, 1.6487, 2.7183])
for t in [0.25, 0.75]:
    Ls = [float(lagrange_basis(x, k, np.array(t))) for k in range(3)]
    print(f"t = {t}: L0 = {Ls[0]:.4f}, L1 = {Ls[1]:.4f}, L2 = {Ls[2]:.4f}, "
          f"P2 = {float(lagrange_interp(x, y, t)):.6f}, e^t = {np.exp(t):.6f}")

# Plot the cardinal functions for 5 equally spaced nodes
xn = np.linspace(0, 1, 5)
t = np.linspace(0, 1, 300)
plt.figure(figsize=(6, 3.4))
for k in range(5):
    plt.plot(t, lagrange_basis(xn, k, t), label=f"$L_{k}$")
plt.plot(xn, np.zeros(5), "ko", ms=4)
plt.plot(xn, np.ones(5), "k+", ms=8)
plt.legend(ncol=5, fontsize=8, loc="lower center")
plt.title("Lagrange cardinal functions: $L_k(x_j)=\\delta_{kj}$")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch09_cardinal.pdf")
