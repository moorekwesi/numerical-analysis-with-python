# Newton's method, with a table showing quadratic convergence
def newton(f, df, x0, tol=1e-12, max_iter=50):
    """Newton's method x_{n+1} = x_n - f(x_n)/f'(x_n).

    Returns the list of iterates. Stops when |x_{n+1} - x_n| < tol."""
    xs = [x0]
    for _ in range(max_iter):
        d = df(xs[-1])
        if d == 0:
            raise ZeroDivisionError("f'(x_n) = 0: Newton's method breaks down")
        xs.append(xs[-1] - f(xs[-1]) / d)
        if abs(xs[-1] - xs[-2]) < tol:
            return xs
    raise RuntimeError("Newton's method did not converge")


f = lambda x: x**3 - x**2 - x - 1
df = lambda x: 3 * x**2 - 2 * x - 1
r = 1.839286755214161                 # the exact root, for measuring errors

xs = newton(f, df, 1.5)
print(" n        x_n                 |e_n|       |e_n|/|e_{n-1}|^2")
for n, x in enumerate(xs):
    e = abs(x - r)
    # once e_n reaches rounding level (~1e-16) the ratio is meaningless
    ratio = f"{e / abs(xs[n - 1] - r) ** 2:.4f}" if 0 < n and e > 1e-15 else "-"
    print(f"{n:2d}  {x:.16f}  {e:.3e}   {ratio}")
print("theory: |f''(r) / (2 f'(r))| =", abs((6 * r - 2) / (2 * df(r))))

# Leonardo of Pisa's equation (1225):  x^3 + 2x^2 + 10x - 20 = 0
g = lambda x: x**3 + 2 * x**2 + 10 * x - 20
dg = lambda x: 3 * x**2 + 4 * x + 10
xs = newton(g, dg, 1.0)
print("\nFibonacci's equation:", ", ".join(f"{x:.10f}" for x in xs))
