# Basic Newton-Cotes rules and their degree of precision
import numpy as np


def trapezoid(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))


def simpson(f, a, b):
    m = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4 * f(m) + f(b))


def simpson38(f, a, b):
    h = (b - a) / 3
    return 3 * h / 8 * (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(b))


def midpoint(f, a, b):
    return (b - a) * f((a + b) / 2)


rules = {"midpoint": midpoint, "trapezoid": trapezoid, "Simpson": simpson, "Simpson 3/8": simpson38}

print("Integral of e^x over [0, 1] = e - 1 =", np.e - 1)
for name, Q in rules.items():
    val = Q(np.exp, 0.0, 1.0)
    print(f"  {name:12s}: {val:.8f}   error = {abs(val - (np.e - 1)):.2e}")

print("\nDegree of precision: is x^k integrated exactly on [0, 1]?")
print("  k  " + "".join(f"{name:>13s}" for name in rules))
for k in range(6):
    exact = 1 / (k + 1)
    row = ["yes" if abs(Q(lambda x: x**k, 0.0, 1.0) - exact) < 1e-14 else "no" for Q in rules.values()]
    print(f"  {k}  " + "".join(f"{r:>13s}" for r in row))
