# ==============================
# 🐍 Python Tuples – Full Guide
# ==============================

# 🔹 Creating Tuples
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.5, [10, 20])   # mixed
t4 = tuple([1, 2, 3])              # using tuple() function
t5 = ()                            # empty tuple
t6 = (42,)                         # single element tuple needs a comma
print(type(t5))
print("Tuples:", t1, t2, t3, t4, t5, t6)

# 🔹 Accessing Elements
t = (10, 20, 30, 40, 50)
print("First element:", t[0])
print("Last element:", t[-1])
print("Slice [1:4]:", t[1:4])

# 🔹 Immutability
try:
    t[0] = 100  # ❌ will raise error
except TypeError as e:
    print("Tuples are immutable:", e)

# 🔹 Tuple Methods
t = (1, 2, 3, 2, 4, 2)
print("Count of 2:", t.count(2))  # 3
print("Index of 4:", t.index(4))  # 4

# 🔹 Tuple Operations
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 2)
print("Membership 2 in t1:", 2 in t1)
print("Membership 10 not in t1:", 10 not in t1)
print("Length:", len(t1))
print("Min/Max/Sum:", min(t1), max(t1), sum(t1))

# 🔹 Iterating Tuples
t = ("a", "b", "c")
print("Iteration:")
for item in t:
    print("Item:", item)

print("Enumerate Iteration:")
for i, val in enumerate(t):
    print(f"Index {i} → {val}")

# 🔹 Tuple Packing & Unpacking
packed = 10, 20, 30
a, b, c = packed
print("Packed tuple:", packed)
print("Unpacked values:", a, b, c)

# 🔹 Nested Tuples
nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("Access nested element:", nested[1][0])  # 3

# 🔹 Using Tuples as Dictionary Keys (since they’re immutable)
d = { (1, 2): "point A", (3, 4): "point B" }
print("Dictionary with tuple keys:", d)
print("Access dict with tuple key:", d[(1, 2)])

# 🔹 Tuple from String & Range
s = tuple("hello")
r = tuple(range(5))
print("Tuple from string:", s)
print("Tuple from range:", r)
