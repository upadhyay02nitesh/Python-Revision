# -----------------------------------
# Python Operators Demonstration
# -----------------------------------

print("📌 1. ARITHMETIC OPERATORS")
a, b = 10, 3
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division (float)
print("a // b =", a // b) # Floor division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation (10^3)
print("-" * 40)


print("📌 2. COMPARISON (RELATIONAL) OPERATORS")
x, y = 5, 10
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print("-" * 40)


print("📌 3. ASSIGNMENT OPERATORS")
x = 5
print("x =", x)
x += 3   # x = x + 3
print("x += 3 →", x)
x -= 2   # x = x - 2
print("x -= 2 →", x)
x *= 4   # x = x * 4
print("x *= 4 →", x)
x /= 3   # x = x / 3
print("x /= 3 →", x)
x //= 2  # Floor divide
print("x //= 2 →", x)
x %= 2   # Modulus
print("x %= 2 →", x)
x **= 3  # Power
print("x **= 3 →", x)
print("-" * 40)


print("📌 4. LOGICAL OPERATORS")
p, q = True, False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print("-" * 40)


print("📌 5. BITWISE OPERATORS")
m, n = 6, 3   # 6 = 110 (bin), 3 = 011 (bin)
print("m & n =", m & n)   # AND
print("m | n =", m | n)   # OR
print("m ^ n =", m ^ n)   # XOR
print("~m =", ~m)         # NOT
print("m << 2 =", m << 2) # Left shift
print("m >> 1 =", m >> 1) # Right shift
print("-" * 40)


print("📌 6. MEMBERSHIP OPERATORS")
list1 = [1, 2, 3, 4]
print("2 in list1:", 2 in list1)
print("5 not in list1:", 5 not in list1)
print("-" * 40)


print("📌 7. IDENTITY OPERATORS")
a = [1, 2]
b = [1, 2]
c = a
print("a is b:", a is b)       # False (different objects)
print("a == b:", a == b)       # True  (values same)
print("a is c:", a is c)       # True  (same object)
print("a is not b:", a is not b)
print("-" * 40)


print("📌 8. TERNARY (CONDITIONAL) OPERATOR")
age = 18
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
print("-" * 40)
