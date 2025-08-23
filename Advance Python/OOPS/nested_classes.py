
# ✅ Real-Life Scenarios

# Army & Gun → A soldier (Army object) always has a Gun (inner class).

# Car & Engine → A Car always comes with its Engine; engine doesn’t make sense without a car.

# University & Department → A University has departments, but a Department class is not needed globally, only inside University.

# Computer & Processor → Processor is defined inside Computer, since it’s not meaningful without it.

# class Army:
#     def __init__(self):
#         self.name="Armyman"
#         self.gn=self.Gun()

#     def disp(self):
#         print(self.name,self.gn)
#         self.gn.show()



#     class Gun:
#         def __init__(self):
#             self.nam="AK47"
#             self.weight="10kg"

#         def show(self):
#             print(self.nam,self.weight)
    
# A=Army()
# A.disp()


class Car:
    def __init__(self, model):
        self.model = model
        self.engine = self.Engine()

    def show(self):
        print(f"Car: {self.model}")
        self.engine.specs()

    class Engine:
        def __init__(self):
            self.hp = "120HP"
            self.type = "Petrol"

        def specs(self):
            print(f"Engine: {self.hp}, {self.type}")

c = Car("Tesla")
c.show()


# Feature	         Nested Gun (inside Army)	        Separate Gun (outside Army)

# Scope	             Limited to Army	Global,         reusable everywhere
# Encapsulation	        Strong (hidden inside Army)	    Weak (anyone can access)
# Code Organization	C   lean, Army owns Gun	        Cluttered if many global classes
# Reusability	        Low (only for Army)	                High (other classes can use)
# Example use	         Army.Gun()	                        Gun(), Police(Gun()), etc.