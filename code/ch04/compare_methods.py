# Comparing bisection, regula falsi, fixed point, secant and Newton on one problem
import math
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**3 - x**2 - x - 1
df = lambda x: 3 * x**2 - 2 * x - 1
r = 1.839286755214161
N = 40


def errors_bisection(a, b):
    e = []
    for _ in range(N):
        p = (a + b) / 2
        e.append(abs(p - r))
        if f(a) * f(p) < 0:
            b = p
        else:
            a = p
    return e


def errors_regula(a, b):
    e = []
    for _ in range(N):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        e.append(abs(c - r))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return e


def errors_fixed(x):
    # x = g(x) = (x^2 + x + 1)^(1/3); g'(r) ~ 0.44
    e = []
    for _ in range(N):
        x = (x * x + x + 1) ** (1 / 3)
        e.append(abs(x - r))
    return e


def errors_secant(x0, x1):
    e = []
    for _ in range(N):
        if f(x1) == f(x0):
            break
        x0, x1 = x1, x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        e.append(abs(x1 - r))
    return e


def errors_newton(x):
    e = []
    for _ in range(N):
        x = x - f(x) / df(x)
        e.append(abs(x - r))
    return e


runs = {"bisection": errors_bisection(1, 2),
        "regula falsi": errors_regula(1, 2),
        "fixed point": errors_fixed(1.5),
        "secant": errors_secant(1, 2),
        "Newton": errors_newton(1.5)}

print(f"{'method':14s} {'its to 1e-10':>13s} {'order estimate':>15s}")
plt.figure(figsize=(6.5, 3.8))
for name, e in runs.items():
    e = [max(v, 1e-17) for v in e]
    its = next(k + 1 for k, v in enumerate(e) if v < 1e-10)
    # order estimate log(e_{n+1}/e_n) / log(e_n/e_{n-1}) just before the error hits 1e-10
    k = its - 1
    q = math.log(e[k] / e[k - 1]) / math.log(e[k - 1] / e[k - 2])
    q = "n/a (not monotone)" if name == "bisection" else f"{q:.3f}"
    print(f"{name:14s} {its:13d} {q:>18s}")
    plt.semilogy(range(1, len(e) + 1), e, "o-", ms=3, label=name)
plt.ylim(1e-16, 1)
plt.xlim(0, 36)
plt.xlabel("iteration n")
plt.ylabel("|x_n - r|")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch04_compare.pdf")
