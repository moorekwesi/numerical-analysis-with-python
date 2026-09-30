# Finite-difference formulas and their orders of accuracy
import numpy as np

f = lambda x: x * np.exp(x)
df = lambda x: (x + 1) * np.exp(x)          # exact f'
d2f = lambda x: (x + 2) * np.exp(x)         # exact f''
x0 = 2.0

forward = lambda h: (f(x0 + h) - f(x0)) / h
backward = lambda h: (f(x0) - f(x0 - h)) / h
central = lambda h: (f(x0 + h) - f(x0 - h)) / (2 * h)
five_point = lambda h: (f(x0 - 2 * h) - 8 * f(x0 - h) + 8 * f(x0 + h) - f(x0 + 2 * h)) / (12 * h)
second = lambda h: (f(x0 + h) - 2 * f(x0) + f(x0 - h)) / h**2

print(f"f(x) = x e^x at x0 = 2:  f'(2) = {df(x0):.10f},  f''(2) = {d2f(x0):.10f}\n")
print("    h       forward     central     5-point    2nd deriv   (errors)")
prev = None
for h in [0.2, 0.1, 0.05, 0.025, 0.0125]:
    errs = [abs(forward(h) - df(x0)), abs(central(h) - df(x0)),
            abs(five_point(h) - df(x0)), abs(second(h) - d2f(x0))]
    print(f"{h:7.4f}  " + "  ".join(f"{e:10.3e}" for e in errs))
    if prev is not None:
        print("  ratio  " + "  ".join(f"{p / e:10.2f}" for p, e in zip(prev, errs)))
    prev = errs
print("\nexpected ratios when h is halved: 2 (O(h)), 4 (O(h^2)), 16 (O(h^4)), 4 (O(h^2))")
