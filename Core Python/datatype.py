# -----------------------------
# All Python Data Types Example
# -----------------------------

print("📌 NUMERIC TYPES")
x = 10               # int
y = 10.5             # float
z = 3 + 5j           # complex
print(x, type(x))
print(y, type(y))
print(z, type(z))
print("-" * 40)

print("📌 SEQUENCE TYPES")
s = "Hello World"    # str
l = [1, 2, 3, "apple"]   # list
t = (1, 2, 3, "banana")  # tuple
r = range(5)         # range
print(s, type(s))
print(l, type(l))
print(t, type(t))
print(list(r), type(r))   # converting range to list for display
print("-" * 40)

print("📌 MAPPING TYPE")
d = {"name": "John", "age": 25}   # dict
print(d, type(d))
print("-" * 40)

print("📌 SET TYPES")
s = {1, 2, 3, 3, 2}         # set
fs = frozenset([1, 2, 3, 2]) # frozenset
print(s, type(s))
print(fs, type(fs))
print("-" * 40)

print("📌 BOOLEAN TYPE")
b1 = True
b2 = False
print(b1, type(b1))
print(b2, type(b2))
print("-" * 40)

print("📌 BINARY TYPES")
bt = b"Hello"                 # bytes
ba = bytearray([65, 66, 67])  # bytearray
mv = memoryview(b"Hello")     # memoryview
print(bt, type(bt))
print(ba, type(ba))
print(mv, type(mv))
print("-" * 40)

print("📌 NONE TYPE")
n = None
print(n, type(n))
print("-" * 40)
