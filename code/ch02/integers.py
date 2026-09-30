# Integers in a computer: fixed width, two's complement and overflow
import numpy as np

for bits, t in [(8, np.int8), (16, np.int16), (32, np.int32), (64, np.int64)]:
    info = np.iinfo(t)
    print(f"{bits:2d}-bit signed integers: {info.min} ... {info.max}")

# two's complement bit patterns of some 8-bit integers
for k in [5, 1, 0, -1, -5, 127, -128]:
    print(f"{k:5d} -> {np.binary_repr(k, width=8)}")

# overflow: 127 + 1 "wraps around" in 8-bit arithmetic
a = np.array([127], dtype=np.int8)
print("int8: 127 + 1 =", (a + np.int8(1))[0])
b = np.array([32767], dtype=np.int16)
print("int16: 32767 + 1 =", (b + np.int16(1))[0])
# Python's own integers have unlimited size
print("Python int: 2**100 =", 2**100)
