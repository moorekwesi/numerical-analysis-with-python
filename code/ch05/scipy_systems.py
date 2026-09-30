# Solving nonlinear systems with SciPy
import numpy as np
from scipy import optimize


def F(v):
    x, y = v
    return [x**2 + y**2 - 4, x * y - 1]


# fsolve: a classic MINPACK routine (Powell's hybrid method)
print("fsolve:", optimize.fsolve(F, [2, 1]))

# root: a common interface to several methods
for method in ["hybr", "lm", "broyden1"]:
    sol = optimize.root(F, [2, 1], method=method)
    print(f"root(method={method!r:11}): x = {sol.x}, success = {sol.success}")

# the four solutions, found from four starting points
for start in ([2, 1], [1, 2], [-2, -1], [-1, -2]):
    print(start, "->", np.round(optimize.fsolve(F, start), 8))
