# 1. Sum of First N Natural Numbers

# Question: Find the sum of the first N natural numbers.
# Input: 5
# Output: 15

# def natural_sum(n):
#     s=0
#     for i in range(1,n+1):
#         s+=i 
#     return s
# print(natural_sum(5))
        
        
# 2. Check Whether a Number is Abundant Number or not

# A number in which the sum of it’s divisors is greater than the number is known as Abundant Number

# Let’s take number 12 as an example

# Sum of it’s divisors = 1+2+3+4+6 = 16 which is greater than 12. Hence, It is an abundant number


# def abundant_number(n):
#     s=0
#     for i in range(1,n):
#         if n%i==0:
#             s+=i
#     if s>n:
#         return "Abudant number"
#     return "Not Abudant"
# print(abundant_number(12))



# 3. Check Whether a Number is Automorphic Number or Not

# A Number is known as an Automorphic Number if the last digits of it’s square is same as the number itself

# Let’s take number 76 as an example

# 76² = 5776

# The last two digit of the square , 76 is equal to the number itself




# def Automorphic_Number(n):
#     s=n*n
#     temp = str(s)[-len(str(n)):]
#     if temp==n:
#         return "Automorphic_Number"
#     return "not Automorphic_Number"
# print(Automorphic_Number(76))



# 5. Print Harshad Numbers in nth range

# A number that is divisible by sum of it’s own digits is know an Harshad Number.

# Example: 12 , 1+ 2 = 3 , 12 is divisible by 3


# def Harshad_Numbers(n):
#     s=0
#     temp=n 
#     while temp>0:
#         r=temp%10 
#         s+=r
#         temp//=10
#     print(s)
        
#     if n%s==0:
#         return "Harshad Numbers"
#     return "not Harshad Numbers"
# print(Harshad_Numbers(12))



# 6. Print the Armstrong Numbers in Nth Range

# An number is an Armstrong number if the sum of its own digits, 
# each raised to the power of n, is equal to the number itself.

# Example:
# 153 = 1³ + 5³ + 3³ = 153

# 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1634


# def Armstrong_Numbers(n):
#     s=0
#     temp=n 
#     length=int(len(str(n)))
   
#     while temp>0:
#         r=temp%10 
#         s+=r**length
#         temp//=10
#     print(s)
        
#     if s==n:
#         return "Armstrong Numbers"
#     return "not Armstrong Numbers"
# print(Armstrong_Numbers(153))




# 7. Check Whether a Number is Palindrome or Not

# A number when reversed, equates to the same number is known as Palindrome Number

# 121 reversed is 121 itself

# def Palindrome(n):
#     s=0
#     temp=n 
   
#     while temp>0:
#         r=temp%10 
#         s=s*10+r
#         temp//=10
#     print(s)
        
#     if s==n:
#         return "Palindrome Numbers"
#     return "not Palindrome Numbers"
# print(Palindrome(121))


# 8. Print the Reverse of a Number


# def reverse_fun(n):
#     s=0
#     temp=n 
   
#     while temp>0:
#         r=temp%10 
#         s=s*10+r
#         temp//=10
        
#     return s
# print(reverse_fun(153))


# def sum_of_digit(n):
#     temp=n 
#     s=0
#     while temp>0:
#         r=temp%10
#         s+=r 
#         temp//=10
#     return s
# print(sum_of_digit(123))

# a,b,c=10,20,30
# if a>b and a>c :
#     print("A is the greatest")
# elif b>a and b>c:
#     print("B is the greatest")
# else:
#     print("C is the greatest")

# def leap_year(year):
#     if (year%4==0 and year%100!=0) or year%400==0:
#         print(year ,": Leap Year")
#     else:
#         print(year," Not a Leap Year")
# leap_year(1900)


# def prime_number(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         else:
#             return True
# print(prime_number(13))


# def prime_number(r):
#     l=[]
#     for n in range(2,100):
        
#         if n>1:
#             for i in range(r,n):
#                 if n%i==0:
#                     break
#             else:
#                 l.append(n)
#     return l
                
# print(prime_number(2))

# def fact(n):
#     s=1
#     for i in range(1,n+1):
#         s*=i 
#     return s 
# print(fact(5))



# def perfect_number(n):
#     s=0
#     for i in range(1,n):
#         if n%i==0:
#             s+=i 
#     if s==n :
#         return True
#     return False
    
# print(perfect_number(28))

# def prime_factor(n):
#     s=[]
#     for i in range(1,n):
#         if n%i==0:
#             s.append(i)
    
#     s1=[]
#     for i in s:
#         if i>1:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 s1.append(i)
#     return s1
    
# print(prime_factor(28))

# def is_perfect_square(n):
#     sq = n ** 0.5
#     return sq.is_integer()  # True if square root is integer

# print(is_perfect_square(16))  # True
# print(is_perfect_square(20))  # False

# def friendly_pair(n1, n2):
#     s1, s2 = 0, 0
    
#     # Sum of factors of n1
#     for i in range(1, n1+1):
#         if n1 % i == 0:
#             s1 += i
            
#     # Sum of factors of n2
#     for i in range(1, n2+1):
#         if n2 % i == 0:
#             s2 += i
    
#     # Compare ratios
#     if (s1 / n1) == (s2 / n2):
#         return True
#     return False

# print(friendly_pair(6, 28))  # True

def fact(n):
    m=1
    for i in range(1,n+1):
        m*=i 
    return m

def strong_number(n):
    s=0
    temp=n 
    while temp>0:
        r=temp%10
        s=s+fact(r)
        temp//=10
    print(s)
    if s==n:
        return True
    return False
print(strong_number(145))


        