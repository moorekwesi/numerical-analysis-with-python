# Why pivoting is necessary: a tiny pivot destroys the solution
import numpy as np


def solve_2x2_no_pivot(A, b):
    m = A[1, 0] / A[0, 0]
    u22 = A[1, 1] - m * A[0, 1]
    c2 = b[1] - m * b[0]
    x2 = c2 / u22
    x1 = (b[0] - A[0, 1] * x2) / A[0, 0]
    return np.array([x1, x2])


for eps in [1e-4, 1e-8, 1e-12, 1e-16, 1e-20]:
    A = np.array([[eps, 1.0], [1.0, 1.0]])
    b = np.array([1.0, 2.0])
    x_np = solve_2x2_no_pivot(A, b)
    x_pp = solve_2x2_no_pivot(A[::-1], b[::-1])   # swap the rows = partial pivoting
    print(f"eps = {eps:.0e}:  no pivoting x = {x_np},   with pivoting x = {x_pp}")
print("exact solution is x1 = 1/(1-eps) ~ 1, x2 = (1-2 eps)/(1-eps) ~ 1")
