l = [10, 20, 30, 40, 50]   # corrected list

# filter all numbers > 30
l1 = list(filter(lambda x: x > 30, l))
print(l1)


l = [10, 20, 30, 40, 50]   # corrected list

# filter all numbers > 30
l1 = list(map(lambda x: x *2, l))
print(l1)

from functools import reduce
l = [10, 20, 30, 40, 50]   # corrected list

# filter all numbers > 30
l1 = reduce(lambda x,y: x +y, l)
print(l1)


