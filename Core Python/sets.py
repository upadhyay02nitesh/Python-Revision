# ==============================
# 🐍 Python Sets – Full Guide
# ==============================

# 🔹 Creating Sets
s1 = {1, 2, 3, 4}
s2 = set([4, 5, 6, 7])
s3 = set("hello")   # removes duplicates
s4 = set()          # empty set ({} = dict, not set)

print("Sets:", s1, s2, s3, s4)

# 🔹 Properties
print("No duplicates:", {1, 2, 2, 3, 3, 4})
print("Unordered (may vary):", {10, 20, 30})

# 🔹 Adding & Removing Elements
s = {1, 2, 3}
s.add(4)                 # add single element
s.update([5, 6])         # add multiple
print("After add & update:", s)

s.remove(2)              # remove (error if not present)
s.discard(10)            # remove safely (no error)
popped = s.pop()         # removes random element
print("After remove/discard/pop:", s, "| popped:", popped)

s.clear()
print("After clear:", s)

# 🔹 Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)               # {1,2,3,4,5,6}
print("Intersection:", a & b)        # {3,4}
print("Difference (a-b):", a - b)    # {1,2}
print("Difference (b-a):", b - a)    # {5,6}
print("Symmetric Difference:", a ^ b)# {1,2,5,6}

# 🔹 Membership
print("3 in a:", 3 in a)
print("10 not in a:", 10 not in a)

# 🔹 Set Functions
nums = {10, 20, 30, 40}
print("Length:", len(nums))
print("Min/Max:", min(nums), max(nums))
print("Sum:", sum(nums))

# 🔹 Iteration
for item in nums:
    print("Item:", item)

# 🔹 Set Comprehension
squares = {x**2 for x in range(5)}
print("Set comprehension:", squares)

# 🔹 Frozen Set (immutable set)
fs = frozenset([1, 2, 3, 2, 1])
print("Frozen set:", fs)
# fs.add(4)  # ❌ Error (cannot modify)

# 🔹 Nested Sets (not allowed, but can use frozenset)
# s = { {1,2}, {3,4} }  ❌ Error (unhashable type)
s = {frozenset([1,2]), frozenset([3,4])}
print("Set of frozensets:", s)
