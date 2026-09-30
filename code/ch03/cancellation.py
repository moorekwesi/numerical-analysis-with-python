# Catastrophic cancellation and how to avoid it
import math

# 1. The quadratic formula for x^2 + 1e8 x + 1 = 0
a, b, c = 1.0, 1e8, 1.0
d = math.sqrt(b * b - 4 * a * c)
x1_naive = (-b + d) / (2 * a)             # subtracts two nearly equal numbers
x2 = (-b - d) / (2 * a)
x1_stable = c / (a * x2)                  # Vieta: x1 * x2 = c / a
print("small root, school formula :", x1_naive)
print("small root, stable formula :", x1_stable)
print("(true value is -1.0000000000000000e-08 to 16 digits)")

# 2. f(x) = (1 - cos x)/x^2  -> 1/2 as x -> 0
print("\n   x        (1-cos x)/x^2       2 sin^2(x/2)/x^2")
for k in range(1, 9):
    x = 10.0 ** (-k)
    f1 = (1 - math.cos(x)) / x**2
    f2 = 2 * math.sin(x / 2) ** 2 / x**2
    print(f"1e-{k:d}   {f1:.15f}   {f2:.15f}")

# 3. exp(-20) from its Taylor series
s, term = 0.0, 1.0
largest = 0.0
for n in range(1, 120):
    s += term
    largest = max(largest, abs(term))
    term *= -20.0 / n
print("\nTaylor series for e^-20   :", s)
print("largest term in the series:", largest)
print("math.exp(-20)             :", math.exp(-20))
s2, term = 0.0, 1.0
for n in range(1, 120):
    s2 += term
    term *= 20.0 / n
print("1 / (series for e^20)     :", 1 / s2)
