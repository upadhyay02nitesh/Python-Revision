names = ["A", "B", "C"]
scores = [90, 80, 70]

for n, s in zip(names, scores):
    print(n, "scored", s)


# loops_demo.py

# ---------- For Loop ----------
print("\n--- For Loop ---")
for i in range(5):
    print("Iteration:", i)

# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# ---------- While Loop ----------
print("\n--- While Loop ---")
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# ---------- Nested Loop ----------
print("\n--- Nested Loop ---")
for i in range(3):  # outer loop
    for j in range(2):  # inner loop
        print(f"i={i}, j={j}")

# ---------- Loop with else ----------
print("\n--- For Loop with else ---")
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

for i in range(3):
    print(i)
    if i == 1:
        break
else:
    print("Loop finished without break")


print("\n--- While Loop with else ---")
n = 3
while n > 0:
    print("n:", n)
    n -= 1
else:
    print("While loop finished")

# ---------- Break ----------
print("\n--- Break Example ---")
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)

# ---------- Continue ----------
print("\n--- Continue Example ---")
for i in range(6):
    if i == 3:
        print("Skipping", i)
        continue
    print(i)

# ---------- Pass ----------
print("\n--- Pass Example ---")
for i in range(3):
    if i == 1:
        pass  # does nothing (placeholder)
    print("i =", i)

# ---------- Iterating Dictionary ----------
print("\n--- Iterating Dictionary ---")
d = {"name": "Alice", "age": 25, "city": "London"}
for key, value in d.items():
    print(key, ":", value)

# ---------- Iterating with enumerate ----------
print("\n--- Using enumerate ---")
colors = ["red", "green", "blue"]
for idx, color in enumerate(colors):
    print(idx, "->", color)

print("\n✅ Completed Loops Demo in Python!")
