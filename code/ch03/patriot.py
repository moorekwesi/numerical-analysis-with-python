# The Patriot missile failure (Dhahran, 25 February 1991)
# Time was counted in tenths of a second and multiplied by 0.1 stored in a
# 24-bit fixed-point register, i.e. 0.1 chopped after 23 binary digits.
import math

bits = 23
tenth = math.floor(0.1 * 2**bits) / 2**bits
err_per_tick = 0.1 - tenth
print(f"stored value of 0.1   : {tenth:.15f}")
print(f"error per 0.1 s tick  : {err_per_tick:.3e}")
for hours in [1, 8, 20, 48, 72, 100]:
    ticks = hours * 3600 * 10
    drift = ticks * err_per_tick
    print(f"after {hours:3d} h: clock error = {drift:.4f} s,"
          f" Scud travels {1676 * drift:6.0f} m in that time")
