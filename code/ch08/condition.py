# Condition numbers: small residual does not mean small error
import numpy as np

# A nearly singular 2x2 system (Burden & Faires)
A = np.array([[1.0, 2.0], [1.0001, 2.0]])
b = np.array([3.0, 3.0001])
x = np.linalg.solve(A, b)
xhat = np.array([3.0, -0.0001])
r = b - A @ xhat
print("exact solution x      =", x)
print("approximation xhat    =", xhat)
print("residual b - A xhat   =", r, "  ||r||_inf =", np.linalg.norm(r, np.inf))
print("error ||x - xhat||_inf=", np.linalg.norm(x - xhat, np.inf))
print("cond_inf(A)           =", np.linalg.cond(A, np.inf))
bound = np.linalg.cond(A, np.inf) * np.linalg.norm(r, np.inf) / np.linalg.norm(b, np.inf)
print(f"bound  K ||r||/||b||  = {bound:.4f} >= relative error "
      f"{np.linalg.norm(x - xhat, np.inf) / np.linalg.norm(x, np.inf):.4f}")

# Hilbert matrices: digits lost ~ log10(cond)
print("\n  n     cond_2(H_n)     rel. error of solve   correct digits")
for n in [2, 4, 6, 8, 10, 12, 14]:
    H = 1.0 / (np.arange(1, n + 1)[:, None] + np.arange(n)[None, :])
    xt = np.ones(n)
    xs = np.linalg.solve(H, H @ xt)
    rel = np.linalg.norm(xs - xt, np.inf) / np.linalg.norm(xt, np.inf)
    print(f"{n:3d}   {np.linalg.cond(H):12.4e}     {rel:12.4e}        {max(0, -np.log10(rel)):5.1f}")
