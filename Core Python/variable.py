# Assigning integer value 5 to variable x
x = 5
# Assigning string value "John" to variable y
y = "John"
print(x)   # Prints 5
print(y)   # Prints John


# Integer variables
z = 6
n = 6
# 'id()' gives the memory address (object identity) of the variable
# Since both z and n have the same value (6), Python reuses the same memory location (integer caching)
print(id(z))  
print(id(n))


# Different ways of writing valid variable names in Python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Printing all variables (they all store "John")
print(myvar, myvar2, my_var, _my_var, myVar, MYVAR)


# Multiple variables assigned the same value in one line
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange


# Multiple variables assigned different values in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry


# Unpacking list into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry


# Simple string variable
x = "Python is awesome"
print(x)   # Python is awesome


# Printing multiple variables with commas (comma adds space between them)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)   # Python is awesome


# String concatenation (using +, no spaces added automatically)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)   # Python is awesome


# Converting integer to string before concatenation
x = 5
x = str(x)   # Convert int to string
y = "John"
print(x + y)  # Prints 5John


# Variable scope example (global vs local)
x = "awesome"

def myfunc():
  # Function can access global variable if not redefined inside
  print("Python is " + x)

myfunc()          # Python is awesome


# Local variable inside function (different from global variable)
x = "awesome"

def myfunc():
  x = "fantastic"   # Local variable (only inside this function)
  print("Python is " + x)

myfunc()           # Python is fantastic
print("Python is " + x)   # Global variable still "awesome"


# Using 'global' keyword to modify global variable inside function
def myfunc():
  global x
  x = "fantastic"   # This modifies the global variable

myfunc()
print("Python is " + x)   # Now global x = fantastic


# Same as above example again
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)   # Prints "Python is fantastic"
