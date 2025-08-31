# Example 1:
    
# Input: N = 6

# Output:
    
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# n=6
# for i in range(1,n+1):
#     print("* "*n,end="\n")
   
   
    
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()
    


# Input Format: N = 6
# Result:
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * * * *

# n=6
# for i in range(1,n+1):
#     print("* "*i)

# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()



# Input Format: N = 6
# Result:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

# n=6

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==i:
#             print(j,end="")
#         else:
#             print(j,end=" ")
#     print()



# Input Format: N = 6
# Result:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6


# n=6

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==i:
#             print(i,end="")
#         else:
#             print(i,end=" ")
#     print()


# Input Format: N = 6
# Result:
# * * * * * *
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

n=6
# for i in range(n,0,-1):
#     if i==1:
#         print("*"*i)
#     else:
#         print("* "*i,end="\n")
        
        
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# Input Format: N = 6
# Result:
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1

# n=6
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         if j==i:
#             print(j,end="")
#         else:
#             print(j,end=" ")
#     print()


# Input Format: N = 6
# Result:
#      *     
#     ***    
#    *****   
#   *******  
#  ********* 
# ***********

# n = 6
# for i in range(1, n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()


# n=6
#             *
#           ***
#         *****
#       *******
#     *********
#   ***********

# n=6
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()

# Input Format: N = 6
# Result:     
# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *

# n=6
# for i in range(n,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print("*",end=" ")
#     print()



# Input Format: N = 6
# Result:   
#      *
#     ***
#    ***** 
#   *******
#  *********
# ***********  
# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *


# n=6
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()


# Input Format: N = 6
# Result:   
#      *
#      **
#      *** 
#      ****
#      *****
#      ******  
#      *****
#      ****
#      ***    
#      **
#      *

# n=6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()



# Input Format: N = 6
# Result:   
# 1       
# 0 1     
# 1 0 1   
# 0 1 0 1
# 1 0 1 0 1
# 0 1 0 1 0 1

# n=6
# for i in range(0,n):
#     for j in range(0,i+1):
#         if j==i:
#             if (i+j)%2==0:
#                 print("1",end="")
#             else:
#                 print("0",end="")
#         else:
#             if (i+j)%2==0:
#                 print("1",end=" ")
#             else:
#                 print("0",end=" ")
            
#     print()
            
            
# # Input Format: N = 6
# # Result:   
# # 1
# # 2  3
# # 4  5  6
# # 7  8  9  10
# # 11  12  13  14  15
# # 16  17  18  19  20  21

# n=6
# m=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==i:  
#             print(m,end="")
#         else:
#             print(m,end=" ")
#         m+=1
#     print()


# Input Format: N = 6
# Result:   
# 1          1
# 12        21
# 12       321
# 1234    4321
# 12345  54321
# 123456654321

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()

# Input Format: N = 6
# Result:   
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F

# n=6
# for i in range(1,n+1):
#     c=ord('A')
#     for j in range(1,i+1):
#         print(chr(c),end=" ")
#         c+=1
#     print()



# Input Format: N = 6
# Result:   
# A B C D E F
# A B C D E 
# A B C D
# A B C
# A B
# A

# n=6
# for i in range(n,0,-1):
#     c=ord('A')
#     for j in range(1,i+1):
#         print(chr(c),end=" ")
#         c+=1
#     print()


# Input Format: N = 6
# Result:   
#      A     
#     ABA    
#    ABCBA   
#   ABCDCBA  
#  ABCDEDCBA 
# ABCDEFEDCBA

# n=6
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     c=ord('A')
#     for j in range(1,i+1):
#         print(chr(c+j-1),end="")
#     c1=ord('A')
#     for j in range(i-1,0,-1):
#         print(chr(c1+j-1),end="")
        
#     print()


# Input Format: N = 6
# Result:   
# F
# E F
# D E F
# C D E F
# B C D E F
# A B C D E F


# n = 6
# for i in range(1, n + 1):
#     # Starting character for the row
#     c = ord('A') + n - i
#     # Print i letters in ascending order
#     for j in range(1, i + 1):
#         print(chr(c + j - 1), end=" ")
#     print()

# Input Format: N = 6
# Result:   
# ************
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *
# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ************

# n=6
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
    

# Input Format: N = 6
# Result:   
# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ************
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *

# n=6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()


# Input Format: N = 6
# Result:   
# ******
# *    *
# *    *
# *    *
# *    *
# ******


# n=6
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==0 or i==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# Input Format: N = 3
# Result: 
# 3 3 3 3 3 
# 3 2 2 2 3 
# 3 2 1 2 3 
# 3 2 2 2 3 
# 3 3 3 3 3


n = 6
size = 2*n - 1   # total rows/columns

for i in range(size):
    for j in range(size):
        # find the minimum distance from any border
        layer = min(i, j, size-1-i, size-1-j)

        # print number based on which "layer" you are in
        print(n - layer, end=" ")
    print()
