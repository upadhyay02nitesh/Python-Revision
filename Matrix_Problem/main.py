# 1.Cretion of matrix

# m=3
# n=3
# mat=[]
# for i in range(m):
#     row=[]
#     for j in range(n):
#         row.append(int(input("Enter element : ")))
#     mat.append(row)
# print(mat)


# 2. Addition , substraction and multiplication
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

m=len(A)

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
n=len(B)


# result = [[0]*n for _ in range(m)]   # 3x3 zero matrix

# # print(result)

# for i in range(m):
#     for j in range(n):
#         result[i][j]=A[i][j]+B[i][j]
# print(result)


# result=[[0]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         result[i][j]=A[i][j]-B[i][j]
# print(result)

# result=[[0]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         result[i][j]=A[i][j]-B[i][j]
# print(result)


# result=[[0]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         result[i][j]=A[i][j]*B[i][j]

# for row in result:
#     for column in row:
#         print(column,end=" ")
#     print()


# 🔹 4. Matrix Transpose (rows → columns)
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# transpose = [[0]*3 for _ in range(3)]

# for i in range(len(A)):
#     for j in range(len(A[i])):
#         transpose[i][j]=A[j][i]
# print(transpose)


# 5. Diagonal Elements
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# n=len(A)
# s=[]

# for i in range(len(A)):
#      s.append(A[i][i])
#      m+=1
# print(s)
     
     
     
     
# 6. Rotate Matrix 90° Clockwise

# 👉 Rule: Transpose + Reverse each row

# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]

# transpose = [[0]*3 for _ in range(3)]

# for i in range(len(A)):
#     for j in range(len(A[i])):
#         transpose[i][j]=A[j][i]


# for i in range(len(transpose)):
#      transpose[i]=transpose[i][::-1]
# print(transpose)



# 🔹 7. Rotate Matrix 90° Anti-Clockwise

# 👉 Rule: Transpose + Reverse each column


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# [3, 6, 9]
# [2, 5, 8]
# [1, 4, 7]


transpose = [[0]*3 for _ in range(3)]

for i in range(len(A)):
    for j in range(len(A[i])):
        transpose[i][j]=A[j][i]

transpose=transpose[::-1]
print(transpose)