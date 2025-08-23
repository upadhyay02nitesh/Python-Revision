# class MathOperations:
#     def addition(self, a, b):
#         return a + b

#     def addition(self, a, b, c):
#         return a + b + c

# m = MathOperations()
# print(m.addition(10, 20, 30)) # Calls the second addition method
# print(m.addition(10, 20))      # Error: Only the second addition method exists

class MathOperations:
    def addition(self, *args):
        return sum(args)

m = MathOperations()
print(m.addition(10, 20))      # 30
print(m.addition(10, 20, 30))  # 60
