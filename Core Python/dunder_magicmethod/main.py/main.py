# 4️⃣ Key Points

# Magic methods start and end with double underscores (__method__)

# They allow custom behavior for Python operators and built-in functions

# Many magic methods are already implemented in built-in types

# You can override them to make your classes behave like built-in types


# Dunder methods = magic methods = special methods

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}"

    def __add__(self, other):
        return self.price + other.price

    def __eq__(self, other):
        return self.price == other.price

# Create objects
p1 = Product("Laptop", 75000)
p2 = Product("Smartphone", 25000)

print(p1)              # Laptop costs $75000 (__str__)
print(p1 + p2)         # 100000 (__add__)
print(p1 == p2)        # False (__eq__)
