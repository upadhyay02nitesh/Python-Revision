# Write a Python program to reverse a string.

# def reverse_string(s):
#     s1=""
#     for i in s:
#         s1=i+s1 
#     return s1

# print(reverse_string("Nitesh"))

# Write a Python program to check if a string is a palindrome.

# def palindrome_string(s):
#     s1=""
#     for i in s:
#         s1=i+s1 
#     if s==s1:
#         return True
#     return False

# print(palindrome_string("malayalam"))


# Write a Python program to count the number of vowels in a string.

# def palindrome_string(s):
#     s1=""
#     for i in s:
#         s1=i+s1 
#     if s==s1:
#         return True
#     return False

# print(palindrome_string("malayalam"))


# Write a Python program to find the most frequent character in a string.

# def most_frequent(s):
#     d={}
#     for i in s:
#         if i not in d:
#             d[i]=s.count(i)
    
#     max_freq=0  
#     for i,j in d.items():
#         if j>max_freq:
#             max_freq=j 
#             s1=i 
#     return s1
              

# print(most_frequent("malayalam"))



# Write a Python program to remove all duplicates from a string and return the result.


# def remove_duplicacy(s):
#     s1=""
#     for i in s:
#         if i not in s1:
#             s1+=i 
#     return s1
              

# print(remove_duplicacy("malayalam"))

# Write a Python program to check if a string contains only digits.

# def check_only_digit(s):
#     s1=""
#     for i in s:
#         if not i.isdigit():
#             return False
#     return True
            
              
# print(check_only_digit("malayala12m"))



# Write a Python program to count the occurrences of each word in a sentence.

# def count_each_word(s):
#     s=s.split()
#     d={}
#     for i in s:
#         if i not in d:
#             d[i]=s.count(i)
#     return d
            
              
# print(count_each_word("what is it is it good this is cow"))

# Write a Python program to capitalize the first letter of each word in a sentence.

# def capitalize_first_word(s):
#     s=s.split()
    
#     for i in range(len(s)):
#         s[i]=s[i].title()
#     return " ".join(s)
            
              
# print(capitalize_first_word("what is it is it good this is cow"))





# Write a Python program to find the longest word in a sentence.

# def longest_word_string(s):
#     s=s.split()
#     m=0
#     for i in s:
#         if len(i)>m:
#             m=len(i)
#             s1=i 
#     return s1,m
              
# print(longest_word_string("what is malayalam an and janmbhoomi bharat"))




# Write a Python program to check if two strings are anagrams.

# def anagram(s1,s2):
#     s1="".join(sorted(s1))
#     s2="".join(sorted(s2))
#     return s1==s2
               
# print(anagram("listen","silent"))



# Write a Python program to count the number of occurrences of a specific substring in a string.

# def occurence_of_substring(s1,s2):
#     c=0
#     s1=s1.split()
#     for i in s1:
#         if i==s2:
#             c+=1
#     return c
            
    
               
# print(occurence_of_substring("hello how are you hello i am fine","hello"))


# Write a Python program to find the index of the first occurrence of a substring in a string.



# def occurence_of_substring(s1,s2):
#     c=0
#     s1=s1.split()
#     for i in s1:
#         if i==s2:
#             return s1.index(i)
   
            
               
# print(occurence_of_substring("hello how are you hello i am fine","hello"))

# def first_occurrence_index(s1, s2):
#     return s1.find(s2)

# print(first_occurrence_index("hello how are you hello i am fine","hello"))

# Write a Python program to replace all occurrences of a substring with another substring.


# def occurence_of_substring(s1,s2,s3):
#     return s1.replace(s2,s3)
   
               
# print(occurence_of_substring("hello how are you hello i am fine","hello","Hi"))

# Write a Python program to find the length of the last word in a sentence.

# def last_word_len(s1):
#     s1=s1.split()
#     return len(s1[-1])
               
# print(last_word_len("hello how are you hello i am fine"))

# Write a Python program to reverse the order of words in a sentence.

# def reverse_order(s1):
#     s1=s1.split()
#     return " ".join(reversed(s1))
            
# print(reverse_order("hello how are you hello i am fine"))

# Write a Python program to check if a string is a valid email address.
# import re

# def is_valid_email(email):
#     # Regex pattern for a simple email validation
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
#     if re.match(pattern, email):
#         return True
#     return False


# # Example usage
# emails = [
#     "test@example.com",
#     "user.name+tag@domain.co.in",
#     "invalid-email@",
#     "another@domain",
#     "hello@123"
# ]

# for email in emails:
#     print(f"{email} --> {'Valid' if is_valid_email(email) else 'Invalid'}")


# Write a Python program to find the common characters between two strings.

# def most_common_in_string(s1,s2):
#     s3=""
#     for i in s1:
#         if i in s2 and i!=" ":
#             if i not in s3:
#                 s3+=i 
#     return s3
            
            
# print(most_common_in_string("Hi how h are you","I am h h  fine "))

# Write a Python program to find the second most frequent character in a string.

# def second_most_frequent(s1):
#     c=0
#     d={}
#     m=0
#     s=0
#     for i in s1:
#         if i not in d:
#             d[i]=s1.count(i)
#     return sorted(d.items(), key=lambda x: x[1], reverse=True)[1][0]

                       
            
# print(second_most_frequent("aaaaaaabbbbccccbcbcbcccb"))



# Write a Python program to check if a string contains only unique characters.

# def unique_character(s1):
#     s2=""
#     for i in s1:
#         if i in s2:
#             return False
#         else:
#             s2+=i
#     return True
   
                       
            
# print(unique_character("aaaaaaabbbbccccbcbcbcccb"))


# # Write a Python program to a2b3c4--> aabbbcccc
# def fun(s):
#     s1=""
#     for i in s:
#         if i.isalpha():
#             c=i 
#         else:
#             s1=s1+c*int(i)
#     return s1
                     
    
# print(fun("a2b3c4"))


# # Write a Python program to a2b3c4--> aabbbcccc
# def fun(s):
#     s1=""
#     for i in s:
#        if i not in s1:
#            s1+=i+str(s.count(i))
#     return s1
                    
# print(fun("aabbbcccc"))


# Write a Python program ABC->65+66+67=198
# def fun(s):
#     c=0
#     for i in s:
#         c+=ord(i)
#     return c
                    
# print(fun("ABC"))


# def fun(s):
#     c=chr(s)
#     return c
                    
# print(fun(65))

# Write a Python program to shortest word in string

def fun(s):
    s=s.split()
    return sorted(s,key=lambda x:len(x))[0]
                    
print(fun("what is the captital india"))
