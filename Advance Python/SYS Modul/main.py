# sys is essential when you want your Python script to interact with the system, 
# handle CLI input, control runtime behavior, or debug efficiently.

# ============================================
# sys module in Python
# ============================================
import sys

# -------------------------------
# 1. Python version
# -------------------------------
print("Python version:", sys.version)
print("Version info:", sys.version_info)

# -------------------------------
# 2. Command-line arguments
# -------------------------------
# When you run: python script.py arg1 arg2
print("Command-line arguments:", sys.argv)
print("Script name:", sys.argv[0])  # First argument is script name

# -------------------------------
# 3. Standard input/output/error
# -------------------------------
print("Writing to stdout")
sys.stdout.write("Hello stdout\n")  # Same as print, but lower-level
sys.stderr.write("This is an error message\n")

# -------------------------------
# 4. Exiting the program
# -------------------------------
# sys.exit(0)  # Exit program with status 0 (success)
# sys.exit(1)  # Exit program with status 1 (error)

# -------------------------------
# 5. Path information
# -------------------------------
print("Python module search paths:", sys.path)
print("Executable path:", sys.executable)

# -------------------------------
# 6. Maxsize & recursion limit
# -------------------------------
print("Max integer size:", sys.maxsize)
print("Recursion limit:", sys.getrecursionlimit())
sys.setrecursionlimit(2000)  # Set new recursion limit
print("New recursion limit:", sys.getrecursionlimit())

# -------------------------------
# 7. Platform info
# -------------------------------
print("Platform:", sys.platform)

# -------------------------------
# 8. Check if running interactively
# -------------------------------
print("Interactive:", hasattr(sys, 'ps1'))

# -------------------------------
# 9. Modules loaded in current session
# -------------------------------
print("Modules loaded:", list(sys.modules.keys())[:10])  # Show first 10 modules
