class A:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
      return self.x + other.x

class B:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
        return self.x + other.x

a=A(10)
b=B(20)
print(a+b)

# print(a + b)        # Python internally calls a.__add__(b)
print(a.__add__(b)) # Directly calling the method, same result



# 🔹 Key Differences in Practice
# Feature	    + Operator	                 __add__ Method
# Usage	                a + b	                 a.__add__(b)
# Readability	    Very readable,               Pythonic	Less common, more explicit
# Overridable	    Uses __add__ internally	            You define this to control + behavior
# Flexibility	Works with built-in types or user-defined types	Can define custom behavior for your classes
# 🔹 Important Notes

# Operator overloading: You can define __add__ for custom behavior with +.

# Cross-class addition: Python allows adding objects of different classes as long as the __add__ method can handle it.

# Other arithmetic operators:

# - → __sub__

# * → __mul__

# / → __truediv__

# // → __floordiv__

# % → __mod__

