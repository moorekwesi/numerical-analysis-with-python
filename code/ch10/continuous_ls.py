# Continuous least squares: best quadratic approximation of e^x on [0,1]
import numpy as np
from scipy.integrate import quad
from numpy.polynomial import legendre as leg

# (a) monomial basis 1, x, x^2 -> normal equations with the Hilbert matrix
H = np.array([[1 / (i + j + 1) for j in range(3)] for i in range(3)])
rhs = np.array([quad(lambda x: x**k * np.exp(x), 0, 1)[0] for k in range(3)])
a = np.linalg.solve(H, rhs)
print("Hilbert matrix H_3 =\n", H)
print("right-hand side  =", rhs, " ( = [e-1, 1, e-2] )")
print("P2(x) = %.6f + %.6f x + %.6f x^2" % tuple(a))
xs = np.linspace(0, 1, 1001)
P = a[0] + a[1] * xs + a[2] * xs**2
err_ls = np.exp(xs) - P
print(f"max |e^x - P2|          = {np.max(np.abs(err_ls)):.3e}")
print(f"L2 error ||e^x - P2||_2 = {np.sqrt(quad(lambda x: (np.exp(x) - np.polyval(a[::-1], x))**2, 0, 1)[0]):.3e}")
T = 1 + xs + xs**2 / 2
print(f"Taylor 1 + x + x^2/2: max error = {np.max(np.abs(np.exp(xs) - T)):.3e}")

# (b) Legendre basis on [-1,1]: the normal equations are DIAGONAL
print("\ne^x on [-1,1] in Legendre polynomials: c_k = (2k+1)/2 * <f, P_k>")
for n in [2, 4, 6, 8]:
    c = [(2 * k + 1) / 2 * quad(lambda x: np.exp(x) * leg.legval(x, [0] * k + [1]), -1, 1)[0]
         for k in range(n + 1)]
    t = np.linspace(-1, 1, 2001)
    print(f"degree {n}: max error = {np.max(np.abs(np.exp(t) - leg.legval(t, c))):.3e}")
print("first coefficients:", np.round(c[:4], 6))
