# A first plot with Matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
plt.figure(figsize=(6, 3.4))
plt.plot(x, np.sin(x), label=r"$\sin x$")
plt.plot(x, np.cos(x), "--", label=r"$\cos x$")
plt.plot(x, x - x**3 / 6, ":", label=r"$x - x^3/6$ (Taylor)")
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin, cos and a Taylor polynomial")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("ch01_plot.pdf")     # save to a file ...
plt.show()                       # ... and/or display on the screen
