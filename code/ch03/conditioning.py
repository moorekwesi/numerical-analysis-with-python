# Condition number of evaluating a function: kappa(x) = |x f'(x) / f(x)|
import numpy as np

cases = [
    ("sqrt(x)", np.sqrt, lambda x: 0.5 / np.sqrt(x), 2.0),
    ("exp(x)", np.exp, np.exp, 10.0),
    ("x - 1", lambda x: x - 1, lambda x: 1.0, 1.000001),
    ("tan(x)", np.tan, lambda x: 1 / np.cos(x) ** 2, 1.5707),
    ("log(x)", np.log, lambda x: 1 / x, 1.0001),
]
print(f"{'f':8s} {'x':>10s} {'kappa':>12s}  perturb x by 1e-10 relatively")
for name, f, df, x in cases:
    kappa = abs(x * df(x) / f(x))
    xp = x * (1 + 1e-10)
    rel_out = abs(f(xp) - f(x)) / abs(f(x))
    print(f"{name:8s} {x:10.6f} {kappa:12.4e}  rel. change in f = {rel_out:.2e}")
