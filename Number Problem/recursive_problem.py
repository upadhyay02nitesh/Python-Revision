#Print Natural Number 

# def natural_number(n):
#     if n==1:
#         return 1
#     # print(n)
#     return n+natural_number(n-1)

# print(natural_number(10))


# def factorial_number(n):
#     if n < 0:
#         return "Factorial not defined for negative numbers"
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_number(n - 1)

# print(factorial_number(-1))  # Output: Factorial not defined for negative numbers
# print(factorial_number(5))   # Output: 120



# def n_natural(n):
#     if n>0:
#         n_natural(n-1)
#         print(n,end=" ")

# n_natural(5)

# def n_natural_reverse(n):
#     if n>0:
#         print(n,end=" ")
#         n_natural_reverse(n-1)

# n_natural_reverse(5)




# def n_odd_number(n):
#     if n>0:
#         n_odd_number(n-1)
#         print(2*n-1,end=" ")

# n_odd_number(5)


# def n_odd_reverse_number(n):
#     if n>0:
#         print(2*n-1,end=" ")
#         n_odd_reverse_number(n-1)

# n_odd_reverse_number(5)

# def n_even_number(n):
#     if n>0:
#         n_even_number(n-1)
#         print(2*n,end=" ")

# n_even_number(5)




# def even_sum_natural_number(n):
#     if n==1:
#         return 1
#     return 2*n+even_sum_natural_number(n-1)

# print(even_sum_natural_number(5))


def fibo(n):
    if n==1:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(1,6):
    print(fibo(i),end=" ")