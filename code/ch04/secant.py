# The secant method and its order of convergence (the golden ratio!)
import math


def secant(f, x0, x1, tol=1e-12, max_iter=50):
    """Secant method. Returns the list of iterates x0, x1, x2, ..."""
    xs = [x0, x1]
    for _ in range(max_iter):
        f0, f1 = f(xs[-2]), f(xs[-1])
        if f1 == f0:
            break
        xs.append(xs[-1] - f1 * (xs[-1] - xs[-2]) / (f1 - f0))
        if abs(xs[-1] - xs[-2]) < tol:
            break
    return xs


f = lambda x: x**3 - x**2 - x - 1
r = 1.839286755214161
xs = secant(f, 1.0, 2.0)
e = [abs(x - r) for x in xs]
print(" n        x_n                 |e_n|      order estimate")
for n, x in enumerate(xs):
    q = ""
    if n >= 4 and e[n] > 1e-15:     # skip the first steps and rounding level
        q = f"{math.log(e[n] / e[n - 1]) / math.log(e[n - 1] / e[n - 2]):.4f}"
    print(f"{n:2d}  {x:.16f}  {e[n]:.3e}   {q}")
print("golden ratio (1 + sqrt 5)/2 =", (1 + math.sqrt(5)) / 2)
