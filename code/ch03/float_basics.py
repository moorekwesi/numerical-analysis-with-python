# Surprises and facts about IEEE double precision
import sys
from decimal import Decimal
import numpy as np

print("0.1 + 0.2        =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 :", 0.1 + 0.2 == 0.3)
print("exact value stored for 0.1:")
print("   ", Decimal(0.1))

# machine epsilon: the gap between 1 and the next larger double
eps = 1.0
while 1.0 + eps / 2 > 1.0:
    eps = eps / 2
print("machine epsilon (loop)    =", eps)
print("np.finfo(float).eps       =", np.finfo(float).eps)
print("1 + eps/2 == 1 ?          ", 1.0 + eps / 2 == 1.0)
print("largest double            =", sys.float_info.max)
print("smallest normalised double=", sys.float_info.min)
print("smallest subnormal double =", 5e-324, "=", 2.0**-1074)
print("significant decimal digits:", sys.float_info.dig)
print("overflow : 1e308 * 10     =", 1e308 * 10)
print("underflow: 1e-320 / 1e10  =", 1e-320 / 1e10)
print("inf - inf                 =", float("inf") - float("inf"))
nan = float("nan")
print("nan == nan                :", nan == nan)
print("hex form of 0.1           :", (0.1).hex())
print("hex form of 1.0           :", (1.0).hex())
