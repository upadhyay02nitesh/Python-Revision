# ============================================
# Math Module in Python
# ============================================
import math

# -------------------------------
# 1. Constants
# -------------------------------
print("1. Constants:")
print("PI:", math.pi)        # 3.141592653589793
print("Euler's number (e):", math.e)   # 2.718281828459045
print("Tau (2*pi):", math.tau) # 6.283185307179586
print("Infinity:", math.inf)   # inf
print("NaN (Not a Number):", math.nan) # nan


# -------------------------------
# 2. Basic functions
# -------------------------------
print("\n2. Basic Functions:")
print("Absolute value:", math.fabs(-10))      # 10.0
print("Factorial:", math.factorial(5))        # 120
print("Square root:", math.sqrt(16))          # 4.0
print("Power (2^3):", math.pow(2, 3))         # 8.0
print("Remainder:", math.remainder(22, 5))    # -3.0 (different from % operator)


# -------------------------------
# 3. Trigonometric functions
# -------------------------------
print("\n3. Trigonometric Functions:")
print("sin(90°):", math.sin(math.radians(90)))   # 1.0
print("cos(0°):", math.cos(math.radians(0)))     # 1.0
print("tan(45°):", math.tan(math.radians(45)))   # 0.999...
print("asin(1):", math.degrees(math.asin(1)))    # 90.0 degrees
print("acos(0):", math.degrees(math.acos(0)))    # 90.0 degrees
print("atan(1):", math.degrees(math.atan(1)))    # 45.0 degrees
print("atan2(1,1):", math.degrees(math.atan2(1, 1)))  # 45.0


# -------------------------------
# 4. Logarithmic and Exponential
# -------------------------------
print("\n4. Logarithmic and Exponential:")
print("exp(1):", math.exp(1))                # e^1
print("log(e):", math.log(math.e))           # natural log (base e)
print("log10(1000):", math.log10(1000))      # log base 10
print("log2(8):", math.log2(8))              # log base 2


# -------------------------------
# 5. Rounding & Approximation
# -------------------------------
print("\n5. Rounding & Approximation:")
print("Ceil(4.3):", math.ceil(4.3))          # 5
print("Floor(4.7):", math.floor(4.7))        # 4
print("Truncate(4.9):", math.trunc(4.9))     # 4
print("Round to nearest int:", round(4.5))   # 4 or 5 depending on case
print("Modf(3.14):", math.modf(3.14))        # (fractional, integer)


# -------------------------------
# 6. Angle Conversions
# -------------------------------
print("\n6. Angle Conversions:")
print("Degrees from radians(pi):", math.degrees(math.pi))  # 180.0
print("Radians from degrees(180):", math.radians(180))     # 3.14159...


# -------------------------------
# 7. Special Functions
# -------------------------------
print("\n7. Special Functions:")
print("Greatest Common Divisor (gcd):", math.gcd(12, 18))   # 6
print("Least Common Multiple (lcm):", math.lcm(12, 18))     # 36
print("isfinite(5):", math.isfinite(5))     # True
print("isinf(math.inf):", math.isinf(math.inf))   # True
print("isnan(math.nan):", math.isnan(math.nan))   # True


# -------------------------------
# 8. Hypotenuse Calculation
# -------------------------------
print("\n8. Hypotenuse (Pythagoras theorem):")
print("hypot(3,4):", math.hypot(3,4))    # sqrt(3^2 + 4^2) = 5.0
