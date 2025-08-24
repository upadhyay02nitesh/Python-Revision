# The sys module in Python
# provides low-level access to the runtime environment and 
# command-line arguments (sys.argv), letting you quickly read 
# inputs, exit programs, or access system info, making it suitable
# for simple scripts or personal tools with minimal setup. In contrast,



#     argparse is a high-level module built on top of sys.argv that allows
# structured, user-friendly command-line argument parsing, with automatic type checking, 
# optional arguments, flags, and help messages, making it ideal for robust, scalable CLI
# programs intended for wider use. Simply put, use sys for quick, small scripts, and use 
# argparse for complex, user-friendly command-line applications.




import argparse
import os
import sys

# -------------------------------
# Read username from sys.argv
# -------------------------------
if len(sys.argv) < 2:
    print("Usage: python script.py <username> \"<path>\"")
    sys.exit(1)

username = sys.argv[1]  # First argument is username
# Remaining arguments are passed to argparse
args_list = sys.argv[2:]  # Pass the rest to argparse

# -------------------------------
# Argument parser for path
# -------------------------------
parser = argparse.ArgumentParser(description=f"Hello {username}! Check if a path is file or directory")
parser.add_argument("path", type=str, help="Enter file or directory path")
args = parser.parse_args(args_list)  # parse only remaining arguments

# -------------------------------
# Get the path
# -------------------------------
path = args.path

# -------------------------------
# Check if file or directory
# -------------------------------
print(f"Hello {username}!")
if os.path.exists(path):
    if os.path.isfile(path):
        print(f"{path} is a file")
    elif os.path.isdir(path):
        print(f"{path} is a directory")
else:
    print(f"{path} does not exist")
