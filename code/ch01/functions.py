# Functions, default arguments, lambda and passing functions as arguments
import math


def quadratic_roots(a, b, c):
    """Return the two roots of a x^2 + b x + c = 0 (real or complex)."""
    d = b * b - 4 * a * c
    sq = math.sqrt(d) if d >= 0 else complex(0, math.sqrt(-d))
    return (-b + sq) / (2 * a), (-b - sq) / (2 * a)


print("roots of x^2 - 3x + 2:", quadratic_roots(1, -3, 2))
print("roots of x^2 + 2x + 5:", quadratic_roots(1, 2, 5))


def forward_difference(f, x, h=1e-5):
    """Approximate f'(x) by (f(x+h) - f(x))/h.  f is itself a function!"""
    return (f(x + h) - f(x)) / h


square = lambda t: t**2                  # a small anonymous function
print("d/dx x^2 at x=3   ~", forward_difference(square, 3.0))
print("d/dx sin at x=0   ~", forward_difference(math.sin, 0.0))
print("with h = 0.1      ~", forward_difference(math.sin, 0.0, h=0.1))
