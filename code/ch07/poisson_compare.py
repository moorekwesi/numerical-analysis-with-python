# Comparing iterative methods on the 2D Poisson equation  -Laplace(u) = f  on the unit square
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt

m = 20                                   # interior grid points per direction
n = m * m                                # number of unknowns
h = 1.0 / (m + 1)
T = sp.diags([-1, 4, -1], [-1, 0, 1], shape=(m, m))
S = sp.diags([-1, -1], [-1, 1], shape=(m, m))
A = (sp.kron(sp.identity(m), T) + sp.kron(S, sp.identity(m))).tocsr()   # 5-point Laplacian * h^2
b = h**2 * np.ones(n)                    # f = 1
Ad = A.toarray()
tol, maxit = 1e-8, 5000
bnorm = np.linalg.norm(b)
print(f"n = {n} unknowns, nonzeros in A: {A.nnz} of {n * n}")


def run(update):
    x = np.zeros(n)
    res = []
    for k in range(maxit):
        x = update(x)
        res.append(np.linalg.norm(b - A @ x) / bnorm)
        if res[-1] < tol:
            break
    return res


d = Ad.diagonal()
jac = lambda x: x + (b - A @ x) / d


def gs_sweep(x, omega=1.0):
    x = x.copy()
    for i in range(n):
        row = A.indices[A.indptr[i]:A.indptr[i + 1]]
        val = A.data[A.indptr[i]:A.indptr[i + 1]]
        s = val @ x[row] - d[i] * x[i]
        x[i] = (1 - omega) * x[i] + omega * (b[i] - s) / d[i]
    return x


rhoJ = np.cos(np.pi * h)                 # known spectral radius of Jacobi here
w_opt = 2 / (1 + np.sin(np.pi * h))
histories = {"Jacobi": run(jac),
             "Gauss-Seidel": run(gs_sweep),
             f"SOR (omega={w_opt:.3f})": run(lambda x: gs_sweep(x, w_opt))}

cg_res = []
record = lambda xk: cg_res.append(np.linalg.norm(b - A @ xk) / bnorm)
try:                                     # SciPy >= 1.12 calls the tolerance 'rtol'
    spla.cg(A, b, rtol=tol, maxiter=maxit, callback=record)
except TypeError:                        # older SciPy versions call it 'tol'
    spla.cg(A, b, tol=tol, maxiter=maxit, callback=record)
histories["Conjugate gradient"] = cg_res

print(f"rho(T_J) = cos(pi h) = {rhoJ:.5f},  rho(T_GS) = {rhoJ**2:.5f}")
for name, res in histories.items():
    print(f"{name:24s}: {len(res):5d} iterations")

plt.figure(figsize=(6.2, 3.8))
for name, res in histories.items():
    plt.semilogy(res, label=name)
plt.xlabel("iteration")
plt.ylabel("relative residual")
plt.xlim(0, 1700)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch07_poisson.pdf")
