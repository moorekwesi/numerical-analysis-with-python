# Vectors with NumPy
import numpy as np

L = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("L          =", L)
print("L.shape    =", L.shape, " len(L) =", len(L))

K = L.reshape(-1, 1)          # a column vector (10 x 1)
print("K.shape    =", K.shape)

s = np.linspace(1, 10, 5)     # 5 equally spaced points from 1 to 10
print("linspace   =", s)
V = np.arange(1, 21, 1)       # 1,2,...,20   (the end point is excluded!)
B = np.arange(0, 21, 2)       # 0,2,...,20
print("arange     =", V)
print("even       =", B)

A = np.array([1, 2, 4, 8])
Bv = np.array([-1, 2, 1, 0])
print("A + Bv     =", A + Bv)
print("A - Bv     =", A - Bv)
print("A * Bv     =", A * Bv, "  (element-wise)")
print("A @ Bv     =", A @ Bv, "  (dot product)")
print("2*A        =", 2 * A)
print("A**2       =", A ** 2)
print("sqrt(A)    =", np.sqrt(A))

# Indexing starts at 0 in Python (it starts at 1 in MATLAB/Octave)
print("A[0], A[-1] =", A[0], A[-1])
print("A[1:3]      =", A[1:3])

# Concatenation
F = np.concatenate([A, Bv])
print("F          =", F)
# Deleting an element
O = np.array([1, -1, 0, 2, 0])
O = np.delete(O, 2)           # remove the third element (index 2)
print("O          =", O)
print("sum, max, min, mean of A:", A.sum(), A.max(), A.min(), A.mean())
