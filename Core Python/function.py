# ======================================
# 📌 PYTHON FUNCTIONS – ONE FILE GUIDE
# ======================================

# 1. Simple function (no parameters, no return)
def hello():
    print("Hello, Python!")

hello()


# 2. Function with parameters
def greet(name):
    print("Hello,", name)

greet("Nitesh")


# 3. Function with return value
def add(a, b):
    return a + b

print("Addition:", add(5, 3))


# 4. Default parameters
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()
welcome("Nitesh")


# 5. Keyword arguments
def intro(name, age):
    print(f"My name is {name}, I am {age} years old.")

intro(age=24, name="Nitesh")


# 6. Arbitrary arguments (*args)
def fruits(*items):
    print("Fruits:", items)

fruits("Apple", "Banana", "Mango")


# 7. Arbitrary keyword arguments (**kwargs)
def student(**details):
    print("Student details:", details)

student(name="Nitesh", age=24, course="AI")

# 8. Return multiple values
def math_ops(x, y):
    return x + y, x - y, x * y

s, d, m = math_ops(10, 5)
print("Sum:", s, "Diff:", d, "Mul:", m)


# 9. Function inside function
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()


# 10. Anonymous / Lambda functions
square = lambda x: x ** 2
print("Square:", square(6))


# 11. Higher-order function (function as argument)
def apply(func, value):
    return func(value)

print("Double:", apply(lambda x: x * 2, 5))


# 12. Map, Filter, Reduce
nums = [1, 2, 3, 4, 5]

# map → apply function
squares = list(map(lambda x: x ** 2, nums))
print("Squares:", squares)

# filter → condition check
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)

from functools import reduce
sum_all = reduce(lambda a, b: a + b, nums)
print("Sum:", sum_all)


# 13. Recursive function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial 5:", factorial(5))


# 14. Docstring (function documentation)
def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

print("Multiply:", multiply(3, 4))
print("Docstring:", multiply.__doc__)


# 15. Function with type hints
def divide(a: int, b: int) -> float:
    return a / b

print("Division:", divide(10, 2))


# 16. Global and Local variables
x = 10  # Global

def test():
    x = 5  # Local
    print("Inside:", x)

test()
print("Outside:", x)


# 17. Use global keyword
y = 100
def change_global():
    global y
    y = 200

change_global()
print("Global y:", y)


# 18. Closures (function remembers outer variable)
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print("Double 7:", double(7))


# 19. Decorators (functions that wrap other functions)
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hi():
    print("Hi there!")

say_hi()


# 20. Generator functions (yield)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("Countdown:", list(countdown(5)))


# 21. Async function (for concurrency)
# import asyncio

# async def async_hello():
#     print("Hello async!")

# asyncio.run(async_hello())