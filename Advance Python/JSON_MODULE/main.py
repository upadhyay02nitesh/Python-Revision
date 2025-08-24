# =========================================
# JSON in Python (json module)
# =========================================
import json

# -------------------------------
# 1. Convert Python dict to JSON string (dumps)
# -------------------------------
d = {'a': 1, 'b': 2, 'c': 3}
data_str = json.dumps(d)   # dictionary -> JSON string
print("1. Python dict -> JSON string:", data_str)
print(type(data_str))   # <class 'str'>


# -------------------------------
# 2. Convert JSON string to Python dict (loads)
# -------------------------------
json_str = '{"name": "Nitesh", "age": 24, "city": "Rewa"}'
data_dict = json.loads(json_str)  # JSON string -> dictionary
print("\n2. JSON string -> Python dict:", data_dict)
print(type(data_dict))   # <class 'dict'>


# -------------------------------
# 3. Write Python object to JSON file (dump)
# -------------------------------
data_to_save = {
    "username": "nitesh",
    "skills": ["Python", "FastAPI", "AI"],
    "active": True
}

with open("data.json", "w") as f:
    json.dump(data_to_save, f, indent=4)  
    # indent=4 → pretty formatting

print("\n3. Data written to data.json file")


# -------------------------------
# 4. Read JSON file into Python object (load)
# -------------------------------
with open("data.json", "r") as f:
    loaded_data = json.load(f)   # file -> dict
    print("\n4. Data read from data.json file:", loaded_data)
    print(type(loaded_data))   # <class 'dict'>


# -------------------------------
# 5. Formatting Options with dumps
# -------------------------------
print("\n5. Formatting options:")

# Sorted keys
print("Sorted keys:", json.dumps(d, sort_keys=True))

# Indentation
print("Indented:\n", json.dumps(d, indent=4))

# Custom separators (comma + equal sign)
print("Custom separators:", json.dumps(d, separators=(",", "=")))


# -------------------------------
# 6. Convert Python types to JSON
# -------------------------------
print("\n6. Python -> JSON type conversion:")
print(json.dumps({"int": 1, "float": 2.5, "bool": True, "none": None, "list": [1,2,3]}))
# int -> number
# float -> number
# bool -> true/false
# None -> null
# list -> array


# -------------------------------
# 7. Handle Nested Data
# -------------------------------
nested = {
    "user": {"name": "Nitesh", "id": 101},
    "projects": [
        {"title": "AuricMart", "tech": ["Django", "AWS"]},
        {"title": "Taskit", "tech": ["FastAPI", "Streamlit"]}
    ]
}

print("\n7. Nested dict to JSON:")
print(json.dumps(nested, indent=2))
