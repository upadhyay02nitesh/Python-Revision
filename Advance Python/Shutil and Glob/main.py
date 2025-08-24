# 💡 Rule of thumb:

# Use os for basic file/folder operations (check, create, delete, rename).

# Use shutil for copy/move/delete directories and files with content.

# Use glob for finding files by patterns.

import shutil
import glob
import os

# -------------------------------
# 1. Copy a file
# -------------------------------
shutil.copy("data.json", "backup.json")  # Copies file and preserves content
print("File copied to backup.json")

# -------------------------------
# 2. Copy file with metadata
# -------------------------------
shutil.copy2("data.json", "backup_with_meta.json")  # Preserves timestamps
print("File copied with metadata")

# -------------------------------
# 3. Copy an entire directory
# -------------------------------
# shutil.copytree("source_folder", "destination_folder")  # Uncomment to run
# print("Directory copied")

# -------------------------------
# 4. Move/Rename a file or directory
# -------------------------------
# shutil.move("backup.json", "moved_backup.json")  # Move or rename
# print("File moved/renamed")

# -------------------------------
# 5. Delete a file
# -------------------------------
if os.path.isfile("moved_backup.json"):
    os.remove("moved_backup.json")
    print("File deleted")

# -------------------------------
# 6. Delete a directory
# -------------------------------
# os.rmdir("empty_folder")        # Only works if folder is empty
# shutil.rmtree("folder_to_delete")  # Delete folder and all contents

# shutil.copytree("source_folder", "dest_folder") # copy folder
# shutil.move("file.txt", "folder/file.txt")  #move folder 

# -------------------------------
# 7. List all files in current directory (glob)
# -------------------------------
print("All Python files:", glob.glob("*.py"))
print("All JSON files:", glob.glob("*.json"))
print("All text files:", glob.glob("*.txt"))

# -------------------------------
# 8. Recursive search using glob
# -------------------------------
print("All Python files recursively:", glob.glob("**/*.py", recursive=True))

# -------------------------------
# 9. Get absolute paths with glob
# -------------------------------
for file in glob.glob("*.json"):
    print("Absolute path:", os.path.abspath(file))

txt_files = glob.glob("*file?.txt")
print("Text files:", txt_files)

# Recursive search for all files starting with 'file_' and ending with '.txt'
# txt_files = glob.glob("**/file_*.txt", recursive=True)

# print("Text files found recursively:", txt_files)
# -------------------------------
# 10. Check if file or directory exists
# -------------------------------
path = "data.json"
if os.path.exists(path):
    print(f"{path} exists")
if os.path.isfile(path):
    print(f"{path} is a file")
if os.path.isdir("some_folder"):
    print("some_folder is a directory")



