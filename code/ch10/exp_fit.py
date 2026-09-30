# Fitting exponential models: linearisation versus nonlinear least squares
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Demand for pens: price (GHS) and number sold
x = np.array([6.5, 8.3, 11.2, 14.3])
y = np.array([33.0, 21.0, 13.0, 9.0])
b, c = np.polyfit(x, np.log(y), 1)            # ln y = ln a + b x
a = np.exp(c)
print(f"linearised fit : y = {a:.4f} exp({b:.5f} x)")
(a2, b2), _ = curve_fit(lambda t, a, b: a * np.exp(b * t), x, y, p0=(a, b))
print(f"nonlinear fit  : y = {a2:.4f} exp({b2:.5f} x)")
for name, (aa, bb) in [("linearised", (a, b)), ("nonlinear", (a2, b2))]:
    print(f"   {name:10s}: sum of squared errors = {np.sum((y - aa * np.exp(bb * x))**2):.4f}")

# 2. Population of Ghana (census, millions)
year = np.array([1960, 1970, 1984, 2000, 2010, 2021])
pop = np.array([6.727, 8.559, 12.296, 18.912, 24.659, 30.832])
t = year - 1960
b, c = np.polyfit(t, np.log(pop), 1)
P0 = np.exp(c)
print(f"\nGhana: P(t) = {P0:.3f} exp({b:.5f} t),  t = years since 1960")
print(f"growth rate = {100 * b:.2f}% per year, doubling time = {np.log(2) / b:.1f} years")
for yr in [1990, 2030]:
    print(f"model estimate for {yr}: {P0 * np.exp(b * (yr - 1960)):.2f} million")

tt = np.linspace(0, 75, 200)
fig, ax = plt.subplots(1, 2, figsize=(8.5, 3.2))
ax[0].plot(year, pop, "o", label="census")
ax[0].plot(1960 + tt, P0 * np.exp(b * tt), label="exponential fit")
ax[0].set_xlabel("year")
ax[0].set_ylabel("millions")
ax[0].legend()
ax[1].semilogy(year, pop, "o")
ax[1].semilogy(1960 + tt, P0 * np.exp(b * tt))
ax[1].set_xlabel("year")
ax[1].set_title("log scale: a straight line", fontsize=10)
for a_ in ax:
    a_.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch10_ghana.pdf")
