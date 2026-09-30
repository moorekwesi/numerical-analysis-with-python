# Matrices with NumPy
import numpy as np

A = np.array([1, 2, 4, 8])
O = np.array([1, -1, 2, 0])
B = np.array([-1, 2, 1, 0])
H = np.vstack([A, O, B])          # stack rows
print("H =\n", H)
print("H.shape =", H.shape)

try:
    np.vstack([A, np.array([1, -1, 0, 2, 0]), B])
except ValueError as err:
    print("Error:", err)

Z = np.array([[1, -1], [0, 2]])
I2 = np.array([[1, 2], [-3, 4]])
print("Z^T =\n", Z.T)
print("2Z =\n", 2 * Z)
print("Z + I2 =\n", Z + I2)
print("Z @ I2 (matrix product) =\n", Z @ I2)
print("Z * I2 (element-wise)   =\n", Z * I2)

Mq = np.array([[2, 1], [-3, 6], [1, -1], [0, 2]])
print("Mq.shape =", Mq.shape)
print("Mq[3, 0] =", Mq[3, 0], "   row 2:", Mq[2, :], "   column 1:", Mq[:, 1])
try:
    np.linalg.inv(Mq)
except np.linalg.LinAlgError as err:
    print("Error:", err)

print("inv(I2) =\n", np.linalg.inv(I2))
print("det(I2) =", np.linalg.det(I2))

# Special matrices
print("eye(3) =\n", np.eye(3))
print("zeros((2,3)) =\n", np.zeros((2, 3)))
print("diag([1,2,3]) =\n", np.diag([1, 2, 3]))

# Solving a linear system  I2 x = b  (better than computing the inverse!)
b = np.array([5.0, 5.0])
x = np.linalg.solve(I2, b)
print("solution of I2 x = b:", x)
