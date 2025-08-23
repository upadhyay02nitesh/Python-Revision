import os  # Import the OS module, which allows you to interact with the operating system

# Get the current working directory
# print(os.getcwd())  
# os.getcwd() returns the path of the current working directory
# Uncommenting this line would print the current folder path

# Create a new directory named 'JSON_MODULE'
# os.mkdir('JSON_MODULE')  
# os.mkdir() creates a single new directory at the specified path

# Create nested directories: 'Python_MODULE/Submodule1'
# os.makedirs('Python_MODULE/Submodule1')  
# os.makedirs() can create multiple levels of directories at once
# If 'Python_MODULE' doesn't exist, it will be created along with 'Submodule1'

# Change the current working directory to 'Python_MODULE'
# os.chdir('Python_MODULE')  
# os.chdir() changes the current working directory to the specified path

# Print the new current working directory to verify change
# print(os.getcwd())  
# This would now print the path ending with 'Python_MODULE'

# Rename an existing directory 'Directory' to 'Directory and OS'
# os.rename('Directory','Directory and OS')  
# os.rename() is used to rename files or directories

# Remove an empty directory 'Python_MODULE/Submodule1'
# os.rmdir('Python_MODULE/Submodule1')  
# os.rmdir() deletes a single empty directory. It will raise an error if the directory is not empty

# Remove nested directories recursively (all empty directories in the path)
# os.removedirs('Python_MODULE/Submodule1')  
# os.removedirs() removes directories recursively. 
# It will remove 'Submodule1' and also remove 'Python_MODULE' if it becomes empty after removing 'Submodule1'
