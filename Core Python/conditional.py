# ---------------------------------------
# Conditional Statements in Python
# ---------------------------------------

# 1. Simple if
x = 10
if x > 5:
    print("1️⃣ Simple if: x is greater than 5")

# 2. if-else
y = 3
if y % 2 == 0:
    print("2️⃣ if-else: y is even")
else:
    print("2️⃣ if-else: y is odd")

# 3. if-elif-else
marks = 85
if marks >= 90:
    print("3️⃣ if-elif-else: Grade A")
elif marks >= 75:
    print("3️⃣ if-elif-else: Grade B")
elif marks >= 50:
    print("3️⃣ if-elif-else: Grade C")
else:
    print("3️⃣ if-elif-else: Fail")

# 4. Nested if
num = 15
if num > 0:
    if num % 2 == 0:
        print("4️⃣ Nested if: Positive and Even")
    else:
        print("4️⃣ Nested if: Positive and Odd")
else:
    print("4️⃣ Nested if: Non-positive number")

# 5. Ternary Operator (One line if-else)
age = 20
result = "Adult" if age >= 18 else "Minor"
print("5️⃣ Ternary Operator:", result)

# 6. match-case (Python 3.10+)
day = 3
match day:
    case 1:
        print("6️⃣ match-case: Monday")
    case 2:
        print("6️⃣ match-case: Tuesday")
    case 3:
        print("6️⃣ match-case: Wednesday")
    case 4:
        print("6️⃣ match-case: Thursday")
    case 5:
        print("6️⃣ match-case: Friday")
    case 6:
        print("6️⃣ match-case: Saturday")
    case 7:
        print("6️⃣ match-case: Sunday")
    case _:
        print("6️⃣ match-case: Invalid day")

# 7. Combined Conditions with Logical Operators
a, b = 7, 12
if a > 5 and b > 10:
    print("7️⃣ Logical Operator: Both conditions true (AND)")
if a > 5 or b < 10:
    print("7️⃣ Logical Operator: At least one condition true (OR)")
if not (a < 5):
    print("7️⃣ Logical Operator: NOT operator condition true")

# ---------------------------------------
# ✅ Completed Conditional Statements Demo
# ---------------------------------------
