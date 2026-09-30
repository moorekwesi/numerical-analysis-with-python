# Newton's method for a system of nonlinear equations F(x) = 0
import numpy as np
import matplotlib.pyplot as plt


def newton_system(F, J, x0, tol=1e-12, max_iter=50, verbose=False):
    """Solve F(x) = 0, where F: R^n -> R^n has Jacobian matrix J(x).

    Each step solves the LINEAR system J(x_k) dx = -F(x_k); the inverse of J
    is never formed.  Returns the solution and the number of iterations."""
    x = np.array(x0, dtype=float)
    for k in range(1, max_iter + 1):
        dx = np.linalg.solve(J(x), -F(x))
        x = x + dx
        if verbose:
            print(f"k={k}: x = {np.array2string(x, precision=10)}, "
                  f"||dx|| = {np.linalg.norm(dx):.2e}, ||F(x)|| = {np.linalg.norm(F(x)):.2e}")
        if np.linalg.norm(dx) < tol * (1 + np.linalg.norm(x)):
            return x, k
    raise RuntimeError("Newton's method did not converge")


# Example 5.1:  -x(x+1) + 2y = 18,  (x-1)^2 + (y-6)^2 = 25
def F(v):
    x, y = v
    return np.array([-x * (x + 1) + 2 * y - 18,
                     (x - 1) ** 2 + (y - 6) ** 2 - 25])


def J(v):
    x, y = v
    return np.array([[-2 * x - 1, 2.0],
                     [2 * (x - 1), 2 * (y - 6)]])


print("Starting from (2, 11):")
sol, k = newton_system(F, J, [2.0, 11.0], verbose=True)
print("Starting from (-1.5, 10.5):")
sol, k = newton_system(F, J, [-1.5, 10.5], verbose=True)

# Plot the two curves: the solutions are their intersection points
x = np.linspace(-4, 5, 400)
y = np.linspace(4, 14, 400)
X, Y = np.meshgrid(x, y)
plt.figure(figsize=(5, 4))
plt.contour(X, Y, -X * (X + 1) + 2 * Y - 18, levels=[0], colors="C0")
plt.contour(X, Y, (X - 1) ** 2 + (Y - 6) ** 2 - 25, levels=[0], colors="C1")
plt.plot([-2, 1.54694647], [10, 10.96999493], "ko")
plt.xlabel("x")
plt.ylabel("y")
plt.title("f = 0 (parabola) and g = 0 (circle)")
plt.gca().set_aspect("equal")
plt.tight_layout()
plt.savefig("ch05_curves.pdf")
