# ================================
# FILE & DIRECTORY OPERATIONS IN PYTHON
# Using os and os.path modules
# ================================

import os
import time   # only needed in some examples

# -------------------------------
# 1. Check if a file exists
# -------------------------------
if os.path.isfile(r"C:\Users\VICTUS\Desktop\PythonAII\Advance Python\Directory\main.py"):
    print("File exists")
else:
    print("File does not exist")


# -------------------------------
# 2. Check if path is a file or directory
# -------------------------------
path = r"C:\Users\VICTUS\Desktop\PythonAII\Advance Python\Directory\main.py"

if os.path.isfile(path):
    print("It is a file")
elif os.path.isdir(path):
    print("It is a directory")
else:
    print("Path does not exist")


# -------------------------------
# 3. Get file size (in bytes)
# -------------------------------
file = r"C:\Users\VICTUS\Desktop\PythonAII\Advance Python\Directory\main.py"

if os.path.isfile(file):
    print("File size:", os.path.getsize(file), "bytes")   # returns file size in bytes


# -------------------------------
# 4. Get file last modified & created time
# -------------------------------
file = r"C:\Users\VICTUS\Desktop\PythonAII\Advance Python\Directory\main.py"

if os.path.isfile(file):
    print("Last modified:", time.ctime(os.path.getmtime(file)))  # modification time
    print("Created on:", time.ctime(os.path.getctime(file)))     # creation time


# -------------------------------
# 5. Join paths safely
# -------------------------------
base = r"C:\Users\VICTUS\Desktop\PythonAII\Advance Python\Directory"
filename = "main.py"

path = os.path.join(base, filename)   # joins folder and file safely
print("Full path:", path)


# -------------------------------
# 6. Split path into directory & filename
# -------------------------------
path = r"C:\Users\VICTUS\Desktop\PythonAII\Advance Python\Directory\main.py"

dirname, filename = os.path.split(path)
print("Directory:", dirname)
print("File:", filename)


# -------------------------------
# 7. List all files in a directory
# -------------------------------
path = r"C:\Users\VICTUS\Desktop\PythonAII\Advance Python\Directory"

if os.path.isdir(path):
    print("Files in directory:", os.listdir(path))   # returns list of files/folders


# -------------------------------
# 8. Delete a file
# -------------------------------
file = r"C:\Users\VICTUS\Desktop\PythonAII\delete_me.txt"

if os.path.isfile(file):
    os.remove(file)   # deletes the file
    print("File deleted")


# -------------------------------
# 9. Walk through a directory tree
# -------------------------------
root = r"C:\Users\VICTUS\Desktop\PythonAII"

for dirpath, dirnames, filenames in os.walk(root):
    print("Current directory:", dirpath)   # prints current folder
    print("Subdirectories:", dirnames)     # prints subfolders
    print("Files:", filenames)             # prints files in folder
    print("-" * 40)


# -------------------------------
# 10. Absolute vs Relative path
# -------------------------------
relative = "file.txt"
absolute = os.path.abspath(relative)  # converts to full path

print("Relative path:", relative)
print("Absolute path:", absolute)


# -------------------------------
# 11. Check file permissions
# -------------------------------
file = r"C:\Users\VICTUS\Desktop\PythonAII\Advance Python\Directory\main.py"

print("Readable:", os.access(file, os.R_OK))   # can we read?
print("Writable:", os.access(file, os.W_OK))   # can we write?
print("Executable:", os.access(file, os.X_OK)) # can we run/execute?


# -------------------------------
# 12. Split file into name & extension
# -------------------------------
path = r"C:\Users\VICTUS\Desktop\PythonAII\script.py"

filename, ext = os.path.splitext(path)
print("Filename:", filename)   # script
print("Extension:", ext)       # .py


# -------------------------------
# 13. Read environment variables
# -------------------------------
print("PATH variable:", os.environ.get("PATH"))       # system PATH variable
print("Username:", os.environ.get("USERNAME"))        # logged-in user


# -------------------------------
# 14. Run system command (like CMD)
# -------------------------------
os.system("dir")   # Lists files (Windows)
# os.system("ls")  # Lists files (Linux/Mac)
