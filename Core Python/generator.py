# A generator is a special type of iterable like a list, but doesn’t store all values in memory at once.
# It generates values on the fly using the yield keyword.

def numbers(n):
    for i in range(n):
        yield i

# for num in numbers(5):
#     print(num)

num=numbers(5)
print(next(num))
print(next(num))
print(next(num))
print(type(num))