# Summation errors: naive summation, Kahan's compensated summation and math.fsum
import math
import numpy as np

n = 10**6
naive = 0.0
for _ in range(n):
    naive += 0.1

kahan, comp = 0.0, 0.0
for _ in range(n):
    y = 0.1 - comp          # correct the next term by the lost low-order part
    t = kahan + y
    comp = (t - kahan) - y  # what was lost when adding y
    kahan = t

print(f"naive sum of 0.1 (10^6 times) = {naive:.15f}")
print(f"Kahan compensated sum         = {kahan:.15f}")
print(f"math.fsum (correctly rounded) = {math.fsum([0.1] * n):.15f}")

# Floating-point addition is not associative
a, b, c = 1e16, -1e16, 1.0
print("(a + b) + c =", (a + b) + c, "   a + (b + c) =", a + (b + c))

# Order matters: summing 1/k^2 forwards and backwards in single precision
N = 10**6
terms = (1.0 / np.arange(1, N + 1, dtype=np.float64) ** 2).astype(np.float32)
fwd = np.float32(0)
for t in terms:
    fwd += t
bwd = np.float32(0)
for t in terms[::-1]:
    bwd += t
exact = math.fsum(1.0 / k**2 for k in range(1, N + 1))
print(f"float32 forward  sum = {fwd:.8f}")
print(f"float32 backward sum = {bwd:.8f}")
print(f"true value           = {exact:.8f}")
