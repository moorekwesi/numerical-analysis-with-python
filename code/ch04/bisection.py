# The bisection method
import math


def bisection(f, a, b, tol=1e-6, max_iter=100, verbose=False):
    """Find a root of f in [a, b], where f(a) and f(b) have opposite signs.

    Returns the approximate root p and the number of iterations used.
    Stops when the half-length of the bracketing interval is below tol.
    """
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    if verbose:
        print(f"{'n':>3} {'a_n':>12} {'b_n':>12} {'p_n':>12} {'f(p_n)':>12}")
    for n in range(1, max_iter + 1):
        p = a + (b - a) / 2          # midpoint (this form avoids overflow)
        fp = f(p)
        if verbose:
            print(f"{n:3d} {a:12.8f} {b:12.8f} {p:12.8f} {fp:12.4e}")
        if fp == 0 or (b - a) / 2 < tol:
            return p, n
        if math.copysign(1, fa) == math.copysign(1, fp):   # same sign: root in [p, b]
            a, fa = p, fp
        else:                                              # root in [a, p]
            b, fb = p, fp
    raise RuntimeError("bisection did not converge")


def f(x):
    return x**3 - x**2 - x - 1


root, n = bisection(f, 1, 2, tol=1e-6, verbose=True)
print(f"\nroot ~ {root:.10f} after {n} iterations")
print("predicted number of iterations:",
      math.ceil(math.log2((2 - 1) / 1e-6)))
print("exact root (tribonacci constant) 1.839286755214161")
