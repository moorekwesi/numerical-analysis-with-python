# Basic Python: numbers, variables, strings and printing
import math

a = 7            # an int
b = 2.5          # a float
c = 3 + 4j       # a complex number
print(type(a), type(b), type(c))

print("a / 2  =", a / 2)      # true division
print("a // 2 =", a // 2)     # integer (floor) division
print("a % 2  =", a % 2)      # remainder
print("a ** 2 =", a ** 2)     # power
print("|c|    =", abs(c))

# The math module
print("pi      =", math.pi)
print("sqrt(2) =", math.sqrt(2))
print("e^1     =", math.exp(1))

# Strings
name = "Numerical Analysis"
print(name.upper())
print(name.lower())
print(len(name), "characters")
print(name[0:9])          # slicing: characters 0,...,8
print(name.split())       # split into words
print(name.replace("Analysis", "Methods"))

# f-strings: formatted output (very useful for tables)
x = math.pi
print(f"pi to 4 decimal places: {x:.4f}")
print(f"pi in scientific form : {x:.6e}")
print(f"pi in a field of 12   : |{x:12.5f}|")
