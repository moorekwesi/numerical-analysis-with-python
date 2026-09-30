# When Newton's method struggles: bad starting values, cycles and multiple roots
def newton_iterates(f, df, x0, n):
    xs = [x0]
    for _ in range(n):
        xs.append(xs[-1] - f(xs[-1]) / df(xs[-1]))
    return xs


# 1. A poor starting value: x0 = 0.5 for x^3 - x^2 - x - 1
f = lambda x: x**3 - x**2 - x - 1
df = lambda x: 3 * x**2 - 2 * x - 1
xs = newton_iterates(f, df, 0.5, 30)
print("x0 = 0.5 :", ", ".join(f"{x:.4f}" for x in xs[:12]), "...")
print("   iterate 30 =", xs[-1])

# 2. A 2-cycle: x^3 - 2x + 2 with x0 = 0
g = lambda x: x**3 - 2 * x + 2
dg = lambda x: 3 * x**2 - 2
print("cycle    :", newton_iterates(g, dg, 0.0, 6))

# 3. A double root: f(x) = (x - 1)^2 (x + 2), root r = 1 of multiplicity 2
h = lambda x: (x - 1) ** 2 * (x + 2)
dh = lambda x: 2 * (x - 1) * (x + 2) + (x - 1) ** 2
print("\n n   Newton e_n     ratio    | modified Newton (m=2) e_n")
x, y = 2.0, 2.0
e_old = abs(x - 1)
for n in range(1, 9):
    x = x - h(x) / dh(x)
    y = y - 2 * h(y) / dh(y) if abs(y - 1) > 1e-15 else y
    e = abs(x - 1)
    print(f"{n:2d}   {e:.3e}    {e / e_old:.4f}   | {abs(y - 1):.3e}")
    e_old = e
