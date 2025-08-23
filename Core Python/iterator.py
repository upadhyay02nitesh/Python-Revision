
# An iterator is an object in Python that allows you to traverse through all elements of a collection one at a time, without needing to know the internal structure of the collection.

# Iterators follow the iterator protocol:

# __iter__() → returns the iterator object itself

# __next__() → returns the next element, raises StopIteration when done

class MyIterator:
    def __init__(self, limit):
        self.num = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.limit:
            raise StopIteration
        self.num += 1
        return self.num

it = MyIterator(5)
for i in it:
    print(i)
