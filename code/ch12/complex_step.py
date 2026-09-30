# The complex-step derivative: f'(x) ~ Im f(x + i h) / h, with no cancellation
import numpy as np

f = lambda x: np.exp(x) / np.sqrt(np.sin(x) ** 3 + np.cos(x) ** 3)   # Squire & Trapp's test function
x0 = 1.5
# reference value from a very accurate complex step
exact = np.imag(f(x0 + 1e-100j)) / 1e-100
print(f"f'(1.5) = {exact:.15f}")
print("     h      central difference error   complex step error")
for h in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-20]:
    cd = (f(x0 + h) - f(x0 - h)) / (2 * h)
    cs = np.imag(f(x0 + 1j * h)) / h
    print(f"{h:8.0e}   {abs(cd - exact):20.2e}   {abs(cs - exact):18.2e}")
