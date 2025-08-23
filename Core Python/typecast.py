# --------------------------------
# Python Type Casting Demonstration
# --------------------------------

print("📌 1. IMPLICIT TYPE CASTING (Automatic)")
x = 5        # int
y = 2.5      # float
z = x + y    # int + float = float
print(z, type(z))   # 7.5 <class 'float'>
print("-" * 40)


print("📌 2. EXPLICIT TYPE CASTING (Manual)")

# int() conversion
a = int(5.9)          # from float -> int
b = int("10")         # from string -> int
print(a, type(a))     # 5 <class 'int'>
print(b, type(b))     # 10 <class 'int'>

# float() conversion
c = float(10)         # int -> float
d = float("11.5")     # str -> float
print(c, type(c))     # 10.0 <class 'float'>
print(d, type(d))     # 11.5 <class 'float'>

# str() conversion
e = str(25)           # int -> str
f = str(3.14)         # float -> str
print(e, type(e))     # "25" <class 'str'>
print(f, type(f))     # "3.14" <class 'str'>

# list(), tuple(), set() conversion
g = list((1, 2, 3))   # tuple -> list
h = tuple([4, 5, 6])  # list -> tuple
i = set([1, 2, 2, 3]) # list -> set
print(g, type(g))
print(h, type(h))
print(i, type(i))

# dict() conversion (must be key-value pairs)
j = dict([(1, "apple"), (2, "banana")])
print(j, type(j))     # {1: 'apple', 2: 'banana'}

# complex() conversion
k = complex(5)        # int -> complex
l = complex(3, 4)     # two args -> complex
print(k, type(k))     # (5+0j)
print(l, type(l))     # (3+4j)
print("-" * 40)


print("📌 3. BOOLEAN CASTING")
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None))     # False
print(bool(1))        # True
print(bool("Hi"))     # True
print("-" * 40)


print("📌 4. BINARY TYPE CASTING")

# bytes() from string needs encoding
bt = bytes("Hello", "utf-8")
print(bt, type(bt))   # b'Hello' <class 'bytes'>

# bytearray() from list of ASCII values
ba = bytearray([65, 66, 67])
print(ba, type(ba))   # bytearray(b'ABC') <class 'bytearray'>

# memoryview() of bytes
mv = memoryview(b"World")
print(mv, type(mv))   # <memory at ...> <class 'memoryview'>
print("-" * 40)


print("📌 5. INVALID CONVERSIONS (Examples)")
try:
    print(int("10.5"))  # ❌ cannot convert float string to int
except ValueError as e:
    print("Error:", e)

try:
    print(dict([1, 2, 3]))  # ❌ must be key-value pairs
except TypeError as e:
    print("Error:", e)

try:
    print(list(123))  # ❌ int is not iterable
except TypeError as e:
    print("Error:", e)
