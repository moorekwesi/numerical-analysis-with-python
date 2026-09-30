# Newton's divided differences and interpolation error
import numpy as np


def divided_differences(x, y):
    """Return the full divided-difference table F, with F[i, j] = f[x_{i-j}, ..., x_i].
    The Newton coefficients are the diagonal entries F[j, j]."""
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    for j in range(1, n):
        for i in range(j, n):
            F[i, j] = (F[i, j - 1] - F[i - 1, j - 1]) / (x[i] - x[i - j])
    return F


def newton_eval(x, coef, t):
    """Evaluate the Newton form by nested multiplication (Horner-like)."""
    p = coef[-1]
    for k in range(len(coef) - 2, -1, -1):
        p = p * (t - x[k]) + coef[k]
    return p


x = np.array([0.0, 0.5, 0.8, 1.0, 1.4])
y = np.array([1.00, 1.6487, 2.2255, 2.7183, 4.0552])     # e^x rounded
F = divided_differences(x, y)
print("Divided-difference table:")
print("  x_i     f[x_i]      1st        2nd        3rd        4th")
for i in range(len(x)):
    row = "  ".join(f"{F[i, j]:9.5f}" for j in range(i + 1))
    print(f"{x[i]:4.1f}  {row}")
coef = np.diag(F)
print("Newton coefficients:", np.round(coef, 5))
for n in range(1, 5):
    print(f"P_{n}(0.7) = {newton_eval(x[:n + 1], coef[:n + 1], 0.7):.6f}")
print(f"e^0.7    = {np.exp(0.7):.6f}")

# f(0.7) by quadratics on two different sets of nodes, with error estimates
print()
for nodes, extra in (([0.0, 0.5, 0.8], 1.0), ([0.5, 0.8, 1.0], 1.4)):
    xs = np.array(nodes)
    ys = np.exp(xs).round(4)                       # the tabulated values
    c = np.diag(divided_differences(xs, ys))
    p = newton_eval(xs, c, 0.7)
    w = np.prod(0.7 - xs)                          # (0.7-x0)(0.7-x1)(0.7-x2)
    bound = abs(w) * np.exp(xs.max()) / 6          # max |f^(3)| / 3!  with f^(3) = e^x
    # next-term rule: the term that one more node (extra) would add
    x4 = np.append(xs, extra)
    nxt = np.diag(divided_differences(x4, np.exp(x4).round(4)))[-1] * w
    print(f"nodes {nodes}: P2(0.7) = {p:.6f}, true error = {np.exp(0.7) - p:+.2e},")
    print(f"      error bound = {bound:.2e}, next-term estimate = {nxt:+.2e}")
