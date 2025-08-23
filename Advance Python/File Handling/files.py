import os

# ===================== TEXT FILE HANDLING =====================

# 1. Write mode ('w') - creates or overwrites
# with open('file.txt', mode='w') as f:
#     f.write("I am fine")

# # 2. Append mode ('a') - adds to existing content
# with open('file.txt', mode='a') as f:
#     f.write("\nWhat about you?")

# # 3. Read mode ('r') - read content
# with open('file.txt', mode='r') as f:
#     print("TEXT FILE CONTENT:")
#     print(f.read())

# 4. Exclusive creation mode ('x') - creates new file, error if exists
# try:
#     with open('file1.txt', mode='x') as f:
#         f.write("This is a newly created file.")
# except FileExistsError:
#     print("file1.txt already exists, cannot create with 'x' mode.")

# ===================== BINARY FILE HANDLING =====================

# 5. Write binary ('wb') - creates binary file
# with open('file.bin', mode='wb') as f:
#     f.write(b'\x48\x65\x6C\x6C\x6F')  # bytes for "Hello"

# 6. Append binary ('ab') - add bytes
# with open('file.bin', mode='ab') as f:
#     f.write(b'\x20\x57\x6F\x72\x6C\x64')  # bytes for " World"

# # 7. Read binary ('rb') - read bytes
# with open('file.bin', mode='rb') as f:
#     content = f.read()
#     print("\nBINARY FILE CONTENT (as bytes):", content)
#  
# 
#    print("BINARY FILE CONTENT (decoded):", content.decode())  # decode to string


# with open('file.txt',mode='r') as f:
#     content=f.read(2)
#     print(content)


# with open('file.txt',mode='r') as f:
#     content=f.readlines()
#     print(content)


# with open('file.txt',mode='r') as f:
#     con=f.read(2)
#     print(f.tell())
#     print(con)
#     f.seek(4)
#     print(f.tell())

# with open("files.txt",mode='w') as f:
#     with open("file.txt" ,mode='r')as f1:
#         content=f1.read()
    
#     f.write(content)

# with open("files.txt",mode='w') as f:
#     print(f.name)
#     print(f.mode)
#     print(f.closed)
#     print(f.writable())
#     print(f.readable())

# words = ["AI", "Machine", "Learning", "Data", "Python", "Model", 
#          "Neural", "Network", "GenAI", "Algorithm"]
# with open('demo.txt',mode='w') as f:
#     f.writelines(words)


# words = ["AI", "Machine", "Learning", "Data", "Python", "Model", 
#          "Neural", "Network", "GenAI", "Algorithm"]
# with open('demo.txt',mode='w') as f:
#     f.write(" ".join(words))

