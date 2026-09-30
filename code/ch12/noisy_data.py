# Differentiating noisy data amplifies the noise
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(407)                 # fixed seed: reproducible output
t = np.linspace(0, 10, 101)                      # time (s), h = 0.1
g, m, cd = 9.81, 68.1, 0.25
v_true = np.sqrt(g * m / cd) * np.tanh(np.sqrt(g * cd / m) * t)
a_true = g - cd / m * v_true**2                  # exact acceleration dv/dt
v_meas = v_true + rng.normal(0, 0.05, t.size)    # measured velocity, noise 5 cm/s

h = t[1] - t[0]
a_fd = np.gradient(v_meas, h)                    # central differences (one-sided at the ends)
coef = np.polyfit(t, v_meas, 6)                  # smooth first by least squares ...
a_ls = np.polyval(np.polyder(coef), t)           # ... then differentiate the fit
print(f"noise in v             : {0.05:.3f} m/s")
print(f"max error, central diff: {np.max(np.abs(a_fd - a_true)):.3f} m/s^2")
print(f"max error, LS fit      : {np.max(np.abs(a_ls - a_true)):.3f} m/s^2")
print(f"expected noise amplification ~ noise/h = {0.05 / h:.2f}")

fig, ax = plt.subplots(1, 2, figsize=(8.5, 3.2))
ax[0].plot(t, v_meas, ".", ms=3, label="measured v")
ax[0].plot(t, v_true, "k", lw=1, label="true v")
ax[0].set_xlabel("t (s)")
ax[0].legend(fontsize=8)
ax[1].plot(t, a_fd, ".", ms=3, label="central differences")
ax[1].plot(t, a_ls, "C2", label="derivative of LS fit")
ax[1].plot(t, a_true, "k", lw=1, label="true dv/dt")
ax[1].set_xlabel("t (s)")
ax[1].legend(fontsize=8)
for a in ax:
    a.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch12_noisy.pdf")
