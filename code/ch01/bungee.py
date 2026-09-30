# Bungee jumper: analytical velocity and Euler's method
import numpy as np
import matplotlib.pyplot as plt

g, m, cd = 9.81, 68.1, 0.25          # gravity (m/s^2), mass (kg), drag (kg/m)


def v_exact(t):
    """Analytical velocity v(t) = sqrt(g m/cd) tanh( sqrt(g cd/m) t )."""
    return np.sqrt(g * m / cd) * np.tanh(np.sqrt(g * cd / m) * t)


def v_euler(t_end, h):
    """Euler's method for dv/dt = g - (cd/m) v^2, v(0) = 0."""
    n = int(round(t_end / h))
    t = np.linspace(0, t_end, n + 1)
    v = np.zeros(n + 1)
    for i in range(n):
        v[i + 1] = v[i] + h * (g - cd / m * v[i] ** 2)
    return t, v


t, v = v_euler(12, 2.0)
print(" t (s)   Euler v   exact v   error")
for ti, vi in zip(t, v):
    print(f"{ti:5.1f} {vi:9.4f} {v_exact(ti):9.4f} {abs(vi - v_exact(ti)):8.4f}")
print("terminal velocity sqrt(g m/cd) =", np.sqrt(g * m / cd))

# The error at t = 12 s decreases in proportion to the step size h
for h in [2.0, 1.0, 0.5, 0.25, 0.125]:
    t, v = v_euler(12, h)
    print(f"h = {h:6.3f}   error at t = 12: {abs(v[-1] - v_exact(12)):.6f}")

tt = np.linspace(0, 12, 200)
t, v = v_euler(12, 2.0)
plt.figure(figsize=(6, 3.6))
plt.plot(tt, v_exact(tt), label="exact")
plt.plot(t, v, "o--", label="Euler, h = 2")
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch01_bungee.pdf")
