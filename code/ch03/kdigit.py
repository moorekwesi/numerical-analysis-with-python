# Simulating k-digit decimal arithmetic with chopping or rounding
from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP
import math


def set_arithmetic(k, mode):
    """Make every Decimal operation keep k significant digits."""
    getcontext().prec = k
    getcontext().rounding = ROUND_HALF_UP if mode == "round" else ROUND_DOWN


def fl(x, k, mode="round"):
    """k significant decimal digits of x, by chopping or rounding."""
    set_arithmetic(k, mode)
    return +Decimal(repr(x))          # unary + applies the context


for k in [3, 5, 7]:
    for mode in ["chop", "round"]:
        f = fl(math.pi, k, mode)
        rel = abs(float(f) - math.pi) / math.pi
        bound = 10.0 ** (1 - k) * (0.5 if mode == "round" else 1.0)
        print(f"k={k} {mode:5s}: fl(pi) = {str(f):9s} rel.err = {rel:.2e} <= {bound:.1e}")


def poly(x, k, mode):
    """f(x) = x^3 - 6.1 x^2 + 3.2 x + 1.5 in k-digit arithmetic, two ways."""
    set_arithmetic(k, mode)
    x = +Decimal(str(x))
    a2, a1, a0 = Decimal("-6.1"), Decimal("3.2"), Decimal("1.5")
    direct = x * x * x + a2 * (x * x) + a1 * x + a0     # every operation rounded
    nested = ((x + a2) * x + a1) * x + a0               # Horner's rule
    return direct, nested


x = 4.71
exact = x**3 - 6.1 * x**2 + 3.2 * x + 1.5
print(f"\nexact f(4.71) = {exact:.6f}")
for mode in ["chop", "round"]:
    d, n = poly(x, 3, mode)
    print(f"3-digit {mode:5s}: direct = {d},  nested (Horner) = {n}")
