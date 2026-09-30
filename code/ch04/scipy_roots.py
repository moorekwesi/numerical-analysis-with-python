# Professional root finders in SciPy and NumPy
import numpy as np
from scipy import optimize

f = lambda x: x**3 - x**2 - x - 1
df = lambda x: 3 * x**2 - 2 * x - 1

r1 = optimize.bisect(f, 1, 2, xtol=1e-12)
r2 = optimize.brentq(f, 1, 2, xtol=1e-14)        # Brent's method: safe AND fast
r3 = optimize.newton(f, 1.5, fprime=df)            # Newton
r4 = optimize.newton(f, 1.5)                       # no derivative given -> secant
sol = optimize.root_scalar(f, bracket=[1, 2], method="brentq")
print("bisect :", r1)
print("brentq :", r2)
print("newton :", r3)
print("secant :", r4)
print("root_scalar:", sol.root, " function calls:", sol.function_calls)

# All roots of a polynomial: eigenvalues of the companion matrix
coeffs = [1, -1, -1, -1]                           # x^3 - x^2 - x - 1
print("np.roots:", np.roots(coeffs))
