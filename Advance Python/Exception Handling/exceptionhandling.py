# 1. What is an Exception?

# An exception is an error that occurs during the execution of a program.

# Example: dividing by zero, accessing a non-existent key in a dictionary, etc.

a=10
b=0
try:
    temp=a/b
except ZeroDivisionError:
    print("We can not divide from zero")
except Exception as e:
    print(e)

else:
    print(temp)

finally:
    print("Program done ...")


# exception_demo.py
# Demonstrates try, except, else, finally, raise, and custom exceptions

# -------------------------
# 1. Basic try-except
# -------------------------
try:
    x = int(input("Enter a number to divide 100 by: "))
    result = 100 / x
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input, enter a number!")

# -------------------------
# 2. Multiple exceptions in one block
# -------------------------
try:
    lst = [1, 2, 3]
    idx = int(input("Enter an index to access list: "))
    print("Value at index:", lst[idx])
except (ValueError, IndexError) as e:
    print("Error:", e)

# -------------------------
# 3. Catching all exceptions
# -------------------------
try:
    num = int("abc")  # This will fail
except Exception as e:
    print("Caught an exception:", e)

# -------------------------
# 4. else block
# -------------------------
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)

# -------------------------
# 5. finally block
# -------------------------
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs (cleanup section)")

# -------------------------
# 6. Raising exceptions manually
# -------------------------
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
else:
    print("Age entered:", age)

# -------------------------
# 7. Custom exception
# -------------------------
class MyCustomError(Exception):
    pass

try:
    value = int(input("Enter a number <= 100: "))
    if value > 100:
        raise MyCustomError("Value cannot be greater than 100")
except MyCustomError as e:
    print("Custom Exception Caught:", e)


class bankexp(Exception):
    pass 

try:
    balance=120
    amount=100
    if balance-amount<100:
        raise bankexp("You cannot withdraw amount if you have less than 101 ")
except Exception as e:
    print(e)
else:
    balance=balance-amount
    print(balance)

finally:
    print("Completed the program")
