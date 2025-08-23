# ==============================================
# 📌 PYTHON LIST COMPLETE REFERENCE WITH EXAMPLES
# ==============================================

print("\n📌 1. Creating Lists")
my_list = [10, 20, 30, 40, 50]
mixed_list = [1, "Hello", 3.14, True]
nested_list = [[1, 2], [3, 4]]
print("Simple List:", my_list)
print("Mixed List:", mixed_list)
print("Nested List:", nested_list)

print("\n📌 2. Indexing & Negative Indexing")
print("First element:", my_list[0])
print("Last element:", my_list[-1])

print("\n📌 3. Slicing")
print("my_list[1:4] =", my_list[1:4])   # [20, 30, 40]
print("my_list[:3] =", my_list[:3])     # [10, 20, 30]
print("my_list[::2] =", my_list[::2])   # [10, 30, 50]
print("Reversed:", my_list[::-1])       # [50, 40, 30, 20, 10]

print("\n📌 4. Updating Lists")
my_list[1] = 200
print("After update:", my_list)
my_list[1:3] = [300, 400]
print("After slice update:", my_list)

print("\n📌 5. Adding Elements")
my_list.append(60)
print("append(60):", my_list)
my_list.insert(2, 999)
print("insert(2,999):", my_list)
my_list.extend([70, 80])
print("extend([70,80]):", my_list)

print("\n📌 6. Removing Elements")
my_list.remove(999)
print("remove(999):", my_list)
popped = my_list.pop()  # removes last element
print("pop():", popped, "->", my_list)
popped2 = my_list.pop(2)  # removes index 2
print("pop(2):", popped2, "->", my_list)
del my_list[0]   # delete by index
print("del[0]:", my_list)
my_list.clear()
print("clear():", my_list)

print("\n📌 7. Recreating list for next examples")
nums = [5, 2, 9, 1, 5, 6]

print("\n📌 8. Searching in Lists")
print("Count of 5:", nums.count(5))
print("Index of 9:", nums.index(9))

print("\n📌 9. Sorting & Reversing")
nums.sort()
print("sort():", nums)
nums.sort(reverse=True)
print("sort(reverse=True):", nums)
nums.reverse()
print("reverse():", nums)

print("\n📌 10. Copying Lists")
copy1 = nums.copy()
print("copy():", copy1)
copy2 = list(nums)
print("list():", copy2)
copy3 = nums[:]
print("[:]:", copy3)

print("\n📌 11. Built-in Functions on Lists")
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Sorted copy:", sorted(nums))

print("\n📌 12. List Comprehension")
squares = [x**2 for x in range(5)]
print("Squares:", squares)
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)

print("\n📌 13. Nested Lists")
matrix = [[1, 2], [3, 4], [5, 6]]
print("Matrix:", matrix)
print("matrix[1][0] =", matrix[1][0])

print("\n📌 14. Iterating Lists")
for item in ["a", "b", "c"]:
    print("Item:", item)

print("\n📌 15. Join + Split with Strings")
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print("Join:", sentence)
split_back = sentence.split()
print("Split:", split_back)

print("\n✅ DONE! We have covered almost ALL list features & methods.")


import copy

list1 = [[1, 2], [3, 4],4]
shallow = copy.copy(list1)

shallow[0][0] = 99   # change inside nested list
shallow[2]=10

print("Original:", list1)   # [[99, 2], [3, 4]]
print("Shallow:", shallow)  # [[99, 2], [3, 4]]


# import copy

# list1 = [[1, 2], [3, 4],6]
# deep = copy.deepcopy(list1)

# deep[0][0] = 99   # change inside nested list
# deep[2]=10
# print("Original:", list1)   # [[1, 2], [3, 4]]
# print("Deep:", deep)        # [[99, 2], [3, 4]]

# In simple words:

# Shallow Copy = “Two containers sharing the same stuff inside.”

# Deep Copy = “Two containers with their own separate stuff.”


l=[[1,2,3],4,[5,6,7]]
n=len(l)
for i in range(n):
    if type(l[i]) is list:
        for j in range(len(l[i])):
            print(i,j,":->",l[i][j])
    else:
        print(i,"  :->",l[i])

n=int(input("Enter the number : "))
l=list(map(int,input("Enter the element : ").split()))[:n]
print(l)