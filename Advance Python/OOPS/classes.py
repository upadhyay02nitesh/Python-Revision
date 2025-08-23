# ---------------- Example 1: Simple class with constructor ----------------
class Animal:
    def __init__(self) -> None:       # Constructor without arguments
        print("constructor call ")    # Runs when object is created
    
    def disp(self):                   # Instance method
        print("Function call")

# Object creation -> constructor is called
a = Animal()
a.disp()


# ---------------- Example 2: Constructor with argument ----------------
class Animal:
    def __init__(self, name):         # Constructor with one parameter
        self.name = name
        print("constructor call ")
    
    def disp(self, a, b):             # Instance method takes extra arguments
        print("Function call", self.name, a+b)

# Object creation
a = Animal("Kalua")
a.disp(10, 20)                        # Output: Function call Kalua 30


# ---------------- Example 3: Inheritance (Child without constructor override) ----------------
class Animal:
    def __init__(self, name):
        self.name = name
        print("constructor call ")
    
    def disp(self, a, b):
        print("Function call", self.name, a+b)

# Dog inherits Animal
class Dog(Animal):
    def display(self):                # New method in child class
        print("Function call", self.name)

a = Dog("Kalua")                      # Parent constructor runs
a.disp(10, 20)
a.display()


# ---------------- Example 4: Inheritance with Child constructor overriding ----------------
class Animal:
    def __init__(self, name):
        self.name = name
        print("parent constructor call ")
    
    def disp(self, a, b):
        print("Function call", self.name, a+b)

class Dog(Animal):
    def __init__(self, name):         # Overriding constructor
        self.name = name
        print("child constructor call ")
    
    def display(self):
        print("Function call", self.name)

a = Dog("Kalua")                      # Only child constructor runs
a.disp(10, 20)                        # Works because disp() is inherited
a.display()


# ---------------- Example 5: Inheritance with super() ----------------
class Animal:
    def __init__(self, name):
        self.name = name
        print("parent constructor call ")
    
    def disp(self, a, b):
        print("Function call", self.name, a+b)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)        # Calls parent constructor
        self.name = name
        print("child constructor call ")
    
    def display(self):
        print("Function call", self.name)

a = Dog("Kalua")                      # Parent + Child constructor run
a.disp(10, 20)
a.display()


# ---------------- Example 6: Instance, Class, and Static Methods ----------------
class A:
    def __init__(self, a):
        self.a = a                    # Instance variable
    
    b = "yes"                         # Class variable
    
    # Instance method
    def disp(self):
        print(self.a)
    
    # Class method (works with class instead of object)
    @classmethod
    def fp(cls, name):
        print(name, cls.b)
    
    # Static method (independent of class/object variables)
    @staticmethod
    def show(age):
        print(age)

a = A(10)
a.disp()          # Instance method → 10
a.fp("kalu")      # Class method → kalu yes
a.show(18)        # Static method → 18

print()
A.fp("kalua")     # Called directly with class
A.show(22)


# ---------------- Example 7: Instance variable access ----------------
class A:
    def __init__(self):
        self.model = "Realme"         # Instance variable initialized

    def display(self):
        print(self.model)

a = A()
a.display()        # Output: Realme


# ---------------- Example 8: Changing instance variable inside method ----------------
class A:
    def __init__(self):
        self.model = "Realme"         # Initially "Realme"

    def display(self):
        self.model = "Redmi"          # Value updated to "Redmi"

a = A()
print(a.model)     # Output: Realme (before calling display)
a.display()
print(a.model)     # Output: Redmi (after calling display)
