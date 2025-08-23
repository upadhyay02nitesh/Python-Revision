# ============================================
# 📌 MASTER FILE: EVERYTHING ABOUT STRINGS IN PYTHON
# ============================================

print("===== STRING BASICS =====")

# 1. Creating Strings
s1 = "Hello"
s2 = 'World'
s3 = """This is 
a multi-line string"""
print(s1, s2, s3)

# 2. Accessing characters (Indexing)
word = "Python"
print("First char:", word[0])
print("Last char:", word[-1])

# 3. String Slicing
print("Slice [0:4]:", word[0:4])  # Pyth
print("Slice [2:]:", word[2:])    # thon
print("Slice [:4]:", word[:4])    # Pyth
print("Slice with step [::2]:", word[::2])  # Pto


print("\n===== STRING OPERATORS =====")
a, b = "Hello", "World"
print("Concatenation:", a + " " + b)
print("Repetition:", a * 3)
print("'H' in a?:", "H" in a)
print("'z' not in a?:", "z" not in a)


print("\n===== STRING FUNCTIONS =====")
txt = "  hello PYTHON world  "

# Case conversions
print("Upper:", txt.upper())
print("Lower:", txt.lower())
print("Title:", txt.title())
print("Capitalize:", txt.capitalize())
print("Swapcase:", txt.swapcase())

# Trimming
print("Strip:", txt.strip())
print("Lstrip:", txt.lstrip())
print("Rstrip:", txt.rstrip())

# Search
print("Find 'PYTHON':", txt.find("PYTHON"))     # index or -1
print("Index 'world':", txt.index("world"))     # index or error
print("Count 'o':", txt.count("o"))

# Replace
print("Replace PYTHON->JAVA:", txt.replace("PYTHON", "JAVA"))

# Split and Join
words = txt.split()
print("Split:", words)
print("Join with '-':", "-".join(words))

# Startswith / Endswith
print("Starts with 'hello':", txt.strip().startswith("hello"))
print("Ends with 'world':", txt.strip().endswith("world"))

# Check type
print("Is alpha?:", "Hello".isalpha())
print("Is digit?:", "12345".isdigit())
print("Is alnum?:", "Hello123".isalnum())
print("Is space?:", "   ".isspace())
print("Is title?:", "Hello World".istitle())


print("\n===== STRING FORMATTING =====")
name, age = "Nitesh", 24
print("Old Style: %s is %d years old" % (name, age))
print("format(): {} is {} years old".format(name, age))
print(f"f-string: {name} is {age} years old")

pi = 3.14159
print("Pi (2 decimals): {:.2f}".format(pi))


txt = "Hello\nWorld"
print(txt)      # Hello (line1), World (line2)

txt = "Hello\tWorld"
print(txt)      # Hello    World (tab space)

txt = "He said \"Python is fun!\""
print(txt)      # He said "Python is fun!"

txt = "C:\\Users\\Nitesh"
print(txt)      # C:\Users\Nitesh

path = r"C:\Users\Nitesh"
print(path)   # C:\Users\Nitesh  (no need to escape)
