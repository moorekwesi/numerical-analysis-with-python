# Regula falsi (false position) and the Illinois modification
def regula_falsi(f, a, b, tol=1e-10, max_iter=200, illinois=False, verbose=False):
    """False position on [a, b] with f(a) f(b) < 0.

    If illinois=True, the function value at an endpoint that is retained twice in
    a row is halved (Dowell & Jarratt, 1971), which prevents stagnation.
    Returns (root, number of iterations)."""
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    side = 0
    c_old = a
    for n in range(1, max_iter + 1):
        c = b - fb * (b - a) / (fb - fa)       # x-intercept of the chord
        fc = f(c)
        if verbose:
            print(f"{n:3d} {a:12.8f} {b:12.8f} {c:12.8f} {fc:12.4e}")
        if fc == 0 or abs(c - c_old) < tol:
            return c, n
        c_old = c
        if fa * fc < 0:          # root in [a, c]: replace b
            b, fb = c, fc
            if illinois and side == -1:
                fa /= 2
            side = -1
        else:                    # root in [c, b]: replace a
            a, fa = c, fc
            if illinois and side == +1:
                fb /= 2
            side = +1
    raise RuntimeError("no convergence")


f = lambda x: x**3 + 2 * x**2 + 10 * x - 20
print(f"{'n':>3} {'a_n':>12} {'b_n':>12} {'c_n':>12} {'f(c_n)':>12}")
root, n = regula_falsi(f, 1, 2, verbose=True)
print(f"regula falsi: root = {root:.10f} in {n} iterations")
root, n = regula_falsi(f, 1, 2, illinois=True)
print(f"Illinois    : root = {root:.10f} in {n} iterations")

# A convex function on which plain regula falsi is very slow
g = lambda x: x**10 - 1
for ill in [False, True]:
    root, n = regula_falsi(g, 0, 1.3, illinois=ill, max_iter=1000)
    print(f"x^10 - 1 on [0, 1.3], illinois={ill!s:5}: root = {root:.10f}, {n} iterations")
