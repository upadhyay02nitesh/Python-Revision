import random  

# 1. Random float between 0 and 1
print("random():", random.random())  

# 2. Random float in a range
print("uniform(10, 20):", random.uniform(10, 20))  

# 3. Random integer in a range (inclusive)
print("randint(1, 10):", random.randint(1, 10))  

# 4. Random integer from range(start, stop, step)
print("randrange(0, 20, 2):", random.randrange(0, 20, 2))  

# 5. Random choice from a list
items = ["apple", "banana", "cherry"]
print("choice(items):", random.choice(items))  

# 6. Random sample of given length
print("sample(items, 2):", random.sample(items, 2))  

