# Conversion between number bases
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, beta):
    """Digits of the non-negative integer n in base beta (repeated division)."""
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        n, r = divmod(n, beta)       # n = beta*q + r
        digits.append(DIGITS[r])     # remainders give the digits right-to-left
    return "".join(reversed(digits))


def from_base(s, beta):
    """Value of the digit string s in base beta, by Horner's rule."""
    value = 0
    for ch in s.upper():
        value = value * beta + DIGITS.index(ch)
    return value


def fraction_to_base(x, beta, ndigits=20):
    """First ndigits digits of 0 <= x < 1 in base beta (repeated multiplication)."""
    digits = []
    for _ in range(ndigits):
        x = x * beta
        d = int(x)
        digits.append(DIGITS[d])
        x = x - d
        if x == 0:
            break
    return "0." + "".join(digits)


print("Repeated division of 9 by 2:")
n = 9
while n > 0:
    print(f"   {n:3d} = 2 x {n // 2:3d} + {n % 2}")
    n //= 2
print("9 in binary       :", to_base(9, 2))
print("735 in binary     :", to_base(735, 2), "  built-in:", bin(735))
print("2622 in hex       :", to_base(2622, 16), "   built-in:", hex(2622))
print("2622 in octal     :", to_base(2622, 8), "  built-in:", oct(2622))
print("10110 (base 2)    =", from_base("10110", 2), "  built-in:", int("10110", 2))
print("A3E   (base 16)   =", from_base("A3E", 16), "  built-in:", int("A3E", 16))
print("A3C5  (base 16)   =", from_base("A3C5", 16))
print("A3C5 in binary    :", to_base(from_base("A3C5", 16), 2))
print("0.625 in binary   :", fraction_to_base(0.625, 2))
print("0.1   in binary   :", fraction_to_base(0.1, 2, 24), "... (repeats)")
print("1/3   in base 3   :", fraction_to_base(1 / 3, 3, 5))
