print("\n===== USEFUL STRING PROGRAMS =====")

# 1. Reverse a string
s = "Python"
s1=""
for i in s:
    s1=i+s1 
print(s1)


# 2. Palindrome check
s = "madam"
print("Palindrome?:", s == s[::-1])

# 3. Count vowels
vowels = "aeiouAEIOU"
s = "Hello World"
count = 0
v="aeiou"
for i in s:
    if i in v:
        count+=1
print(count)

# 4. Remove duplicates
s = "programming"
s1=""
for i in s:
    if i not in s1:
        s1+=i 
print(s1)

# 5. Frequency of characters
s = "banana"
d=dict()
for i in s:
    if i not in d:
        d[i]=s.count(i)
print(d)


# 6. Anagram check
s1, s2 = "listen", "silent"
print("Anagram?:", sorted(s1) == sorted(s2))

# 7. Word count in a sentence
sentence = "this is a test this is python"
sentence=sentence.split()

d=dict()
for i in sentence:
    if i not in d:
        d[i]=sentence.count(i)
print(d)

# 9. First non-repeated character
for ch in s:
    if s.count(ch) == 1:
        print("First non-repeated char:", ch)
        break

# 10. Swap first and last character
s = "python"
s1=""
for i in range(len(s)):
    if i==0:
        s1+=s[len(s)-1]
    elif i==len(s)-1:
        s1+=s[0]
    else:
        s1+=s[i]
print(s1)

print("\n===== END OF STRING MASTER FILE =====")
