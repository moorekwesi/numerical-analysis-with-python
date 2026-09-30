# All numbers of a toy floating-point system  x = +/- (0.d1 d2 d3)_2 * 2^e,
# d1 = 1 (normalised), e = -1, 0, 1, 2
import numpy as np
import matplotlib.pyplot as plt

beta, p, emin, emax = 2, 3, -1, 2
mantissas = [sum(d * beta ** -(k + 1) for k, d in enumerate(digits))
             for digits in [(1, a, b) for a in (0, 1) for b in (0, 1)]]
positive = sorted(m * beta ** e for e in range(emin, emax + 1) for m in mantissas)
print("mantissas :", mantissas)
print("positive numbers:", positive)
print("count (with negatives and zero):", 2 * len(positive) + 1)
print("gaps:", np.diff(positive))

allnums = [-v for v in positive] + [0.0] + positive
plt.figure(figsize=(7, 1.3))
plt.plot(allnums, np.zeros(len(allnums)), "|", markersize=18)
plt.yticks([])
plt.xticks(range(-4, 5))
plt.title("The toy system: beta=2, p=3, e in {-1,0,1,2}")
plt.tight_layout()
plt.savefig("ch03_toy.pdf")
