# ================================
# Dictionary in Python - Full Demo
# ================================

# Creating dictionaries
dict1 = {"name": "Alice", "age": 25, "city": "New York"}
dict2 = dict([("brand", "Ford"), ("model", "Mustang"), ("year", 1964)])

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

# Accessing values
print("Name:", dict1["name"])
print("City using get():", dict1.get("city"))
print("Non-existing key with default:", dict1.get("country", "Not Found"))

# Adding and updating values
dict1["email"] = "alice@example.com"
dict1.update({"age": 26, "city": "Boston"})
print("Updated dict1:", dict1)

# Removing values
dict1.pop("email")
print("After pop():", dict1)

dict1.popitem()  # removes last inserted
print("After popitem():", dict1)

del dict1["age"]
print("After del:", dict1)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print("Squares dict:", squares)

# Iterating
print("Keys:")
for k in dict2.keys():
    print(k)

print("Values:")
for v in dict2.values():
    print(v)

print("Items:")
for k, v in dict2.items():
    print(f"{k}: {v}")

# Copying
dict3 = dict2.copy()
dict4 = dict(dict2)
print("Shallow copy (dict3):", dict3)
print("Copy via dict() (dict4):", dict4)

# Nested dictionary
nested = {
    "student1": {"name": "John", "marks": 85},
    "student2": {"name": "Emma", "marks": 92}
}
print("Nested Dictionary:", nested)
print("Student2 name:", nested["student2"]["name"])

# Dictionary methods
print("Keys:", dict2.keys())
print("Values:", dict2.values())
print("Items:", dict2.items())

dict2.setdefault("color", "Red")
print("After setdefault:", dict2)

dict2.update({"year": 2025})
print("After update:", dict2)

removed = dict2.pop("model", "Not Found")
print("Popped model:", removed)

# Clear dictionary
dict5 = {"a": 1, "b": 2}
dict5.clear()
print("Cleared dict5:", dict5)

# fromkeys()
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("Fromkeys dict:", new_dict)

# Dictionary membership
print("Is 'brand' in dict2?", "brand" in dict2)
print("Is 'price' not in dict2?", "price" not in dict2)

# Length
print("Length of dict2:", len(dict2))

# Sorting dictionary by keys
sorted_dict = dict(sorted(dict2.items()))
print("Sorted dict by keys:", sorted_dict)

# Dictionary with tuple keys (Immutable keys allowed)
tuple_key_dict = {("x", 1): "Point X1", ("y", 2): "Point Y2"}
print("Tuple key dict:", tuple_key_dict)

# End
print("\n✅ Completed Dictionary Demo in Python!")


l=[1,2,3]
l1=[4,5,6]
d=dict()
for i in range(len(l)):
    d[l[i]]=l1[i]
print(d)