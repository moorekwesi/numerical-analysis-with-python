# Iterative refinement: improve a computed solution using the residual
import numpy as np
import scipy.linalg as sla

n = 10
H = 1.0 / (np.arange(1, n + 1)[:, None] + np.arange(n)[None, :])
x_true = np.ones(n)
b = H @ x_true

# Solve in SINGLE precision (float32) to make the effect visible ...
H32, b32 = H.astype(np.float32), b.astype(np.float32)
lu = sla.lu_factor(H32)
x = sla.lu_solve(lu, b32).astype(np.float64)
print(f"step 0: error = {np.linalg.norm(x - x_true, np.inf):.3e}")
# ... and refine with residuals computed in DOUBLE precision
for k in range(1, 6):
    r = b - H @ x                       # residual in double precision
    d = sla.lu_solve(lu, r.astype(np.float32)).astype(np.float64)
    x = x + d
    print(f"step {k}: error = {np.linalg.norm(x - x_true, np.inf):.3e}")
print(f"cond(H_10) = {np.linalg.cond(H):.2e},  1/u_single = {1 / np.finfo(np.float32).eps:.2e}")

n = 6
H = 1.0 / (np.arange(1, n + 1)[:, None] + np.arange(n)[None, :])
x_true = np.ones(n)
b = H @ x_true
H32, b32 = H.astype(np.float32), b.astype(np.float32)
lu = sla.lu_factor(H32)
x = sla.lu_solve(lu, b32).astype(np.float64)
print(f"\nn = 6, cond = {np.linalg.cond(H):.2e}")
print(f"step 0: error = {np.linalg.norm(x - x_true, np.inf):.3e}")
for k in range(1, 6):
    r = b - H @ x
    x = x + sla.lu_solve(lu, r.astype(np.float32)).astype(np.float64)
    print(f"step {k}: error = {np.linalg.norm(x - x_true, np.inf):.3e}")
