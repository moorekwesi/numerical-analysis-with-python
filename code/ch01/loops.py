# Control flow: for loops, while loops and if statements
import numpy as np

v = np.array([1, 2, 3, 4, 5, 6])

# Sum of neighbouring entries  S[i] = v[i] + v[i+1]
S = np.zeros(len(v) - 1)
for i in range(len(v) - 1):
    S[i] = v[i] + v[i + 1]
print("S (loop)       =", S)
print("S (vectorised) =", v[:-1] + v[1:])

# Accumulating a sum
total = 0
for value in v:
    total = total + value
print("sum with loop =", total, "  np.sum =", np.sum(v))

# while loop: how many times can we halve 1 before it becomes < 1e-3?
x, n = 1.0, 0
while x >= 1e-3:
    x = x / 2
    n += 1
print("halvings needed:", n, " final x =", x)

# if / elif / else
for t in [-2, 0, 3]:
    if t < 0:
        print(t, "is negative")
    elif t == 0:
        print(t, "is zero")
    else:
        print(t, "is positive")

# list comprehension: squares of odd numbers below 10
print([k**2 for k in range(10) if k % 2 == 1])

# Partial sums of the harmonic series  1 + 1/2 + ... + 1/n
for n in [10, 100, 1000, 10000]:
    print(f"n = {n:6d}   H_n = {sum(1 / k for k in range(1, n + 1)):.6f}")
