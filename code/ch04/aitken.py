# Aitken's Delta^2 acceleration and Steffensen's method for x = cos(x)
import math

g = math.cos
r = 0.7390851332151607        # the Dottie number: the solution of cos x = x

# plain fixed-point iteration
x = [1.0]
for _ in range(12):
    x.append(g(x[-1]))

# Aitken's formula applied to the sequence x_n
print(" n    x_n (fixed point)   error      Aitken x^_n        error")
for n in range(len(x) - 2):
    d1 = x[n + 1] - x[n]
    d2 = x[n + 2] - 2 * x[n + 1] + x[n]
    xa = x[n] - d1 * d1 / d2
    print(f"{n:2d}  {x[n]:.12f}  {abs(x[n] - r):.2e}  {xa:.12f}  {abs(xa - r):.2e}")

# Steffensen: restart the fixed-point iteration from each Aitken value
p = 1.0
print("\nSteffensen's method:")
for k in range(5):
    p1 = g(p)
    p2 = g(p1)
    denom = p2 - 2 * p1 + p
    if denom == 0:
        break
    p = p - (p1 - p) ** 2 / denom
    print(f"  k = {k + 1}: p = {p:.15f}, error = {abs(p - r):.2e}")
