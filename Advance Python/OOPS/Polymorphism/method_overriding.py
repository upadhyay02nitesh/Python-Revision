# class Calculator:
#     def add(self,a,b):
#         print(a*b)

# class AdvancedCalculator(Calculator):
#     def add(self, a, b, c):--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#         return a + b + c
    
# c= AdvancedCalculator()
# print(c.add(10, 20, 30))



class Calculator:
    def add(self, a, b):
        return a * b   # Return multiplication instead of print

class AdvancedCalculator(Calculator):
    def add(self, a, b, c):
        parent_result = super().add(a, b)   # Get parent result
        child_result = a + b + c            # Calculate child result
        return parent_result, child_result  # Return both as tuple

c = AdvancedCalculator()
multiplication, addition = c.add(10, 20, 30)
print("Multiplication:", multiplication)
print("Addition:", addition)
