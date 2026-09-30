# Rational functions can reproduce poles: tan(x) near pi/2
import numpy as np
from scipy.interpolate import pade

# Maclaurin coefficients of tan x = x + x^3/3 + 2x^5/15 + 17x^7/315 + 62x^9/2835
a = [0, 1, 0, 1 / 3, 0, 2 / 15, 0, 17 / 315, 0, 62 / 2835]
p, q = pade(a, 4)                        # numerator degree 5, denominator degree 4
taylor = np.poly1d(a[::-1])
print("denominator roots (poles of r):", np.round(np.sort(q.roots.real), 6))
print("pi/2 =", np.pi / 2)
print("\n   x        tan x          Taylor(9)       Pade[5/4]")
for x in [0.5, 1.0, 1.3, 1.5, 1.55]:
    print(f"{x:5.2f}  {np.tan(x):14.8f}  {taylor(x):14.8f}  {p(x) / q(x):14.8f}")
