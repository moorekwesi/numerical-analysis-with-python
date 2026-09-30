# The bit pattern of an IEEE 754 double:  1 sign bit, 11 exponent bits, 52 fraction bits
import struct


def double_bits(x):
    """Return (sign, exponent bits, fraction bits) of the double x."""
    (n,) = struct.unpack(">Q", struct.pack(">d", x))
    b = f"{n:064b}"
    return b[0], b[1:12], b[12:]


for x in [1.0, -2.0, 0.1, 13.25, 1e-310]:
    s, e, f = double_bits(x)
    E = int(e, 2)
    kind = "subnormal" if E == 0 else "normal"
    print(f"x = {x!r}")
    print(f"   sign={s}  exponent={e} (={E}, unbiased {E - 1023})  [{kind}]")
    print(f"   fraction={f}")
