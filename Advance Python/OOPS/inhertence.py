# 1: Single Inheritance

# class Father:
#     def __init__(self,name):
#         self.name=name 
    
#     def show(self):
#         print(self.name)

# class Son(Father):
#     def __init__(self,age):
    
#         self.age=age

#     def show(self):
#         print(self.age)
    

# s=Son(20)
# s.show()


# class Father:
#     def __init__(self,name):
#         self.name=name 
    
#     def show(self):
#         print(self.name)

# class Son(Father):
#     def __init__(self,name,age):
#         super().__init__(name)   # Call Father constructor
    
#         self.age=age

#     def show(self):
#         super().show()
#         print(self.age)
    

# s=Son("John", 20)
# s.show()



# 2:Multilevel inheritance
# class Grandfather:
#     def __init__(self,name):
#         self.name=name 

#     def show(self):
#         print(self.name)

# class Father(Grandfather):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age

#     def show(self):
#         super().show()
#         print(self.age)

# class Son(Father):
#     def __init__(self,name,age,gender):
#         super().__init__(name,age)
#         self.gender=gender

#     def show(self):
#         super().show()
#         print(self.gender)

# s=Son("John", 20, "Male")
# s.show()

# 3.Hierarchical Inheritance

# class Father:
#     def __init__(self,name):
#         self.name=name 

#     def show(self):
#         print(self.name)

# class Son(Father):
#     def __init__(self,name,age,gender):
#         super().__init__(name)
#         self.age=age
#         self.gender=gender

#     def show(self):
#         super().show()
#         print(self.age)
#         print(self.gender)
# class Daughter(Father):
#     def __init__(self,name,age,gender):
#         super().__init__(name)
#         self.age=age
#         self.gender=gender

#     def show(self):
#         super().show()
#         print(self.age)
#         print(self.gender)

# s=Son("John", 20, "Male")
# s.show()

# d=Daughter("Jane", 22, "Female")
# d.show()

# 4:Multiple Inheritance

class Mother:
    def __init__(self,name):
        print("mother constructor")
        self.name=name 

    def show(self):
        print(self.name)

class Father:
    def __init__(self,name,age):
        print("father constructor")
        self.name=name
        self.age=age

    def show(self):
        print(self.name)
        print(self.age)

class Son(Mother,Father):
    print("son constructor")
    def __init__(self,name,age,gender):
        Mother.__init__(self,name)
        Father.__init__(self,name,age)
        self.gender=gender

    def show(self):
        Mother.show(self)
        Father.show(self)
        print(self.gender)

s=Son("John", 20, "Male")
s.show()
