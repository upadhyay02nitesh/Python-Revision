import pickle

class Animal:
    # Constructor to initialize the object
    def __init__(self, name, species):
        self.name = name       # instance variable for name
        self.species = species # instance variable for species

    # Method to make the animal speak
    def speak(self):
        print(f"{self.name} says hello!")


# with open('animat.dat',mode='wb') as f:
#     data = Animal("Buddy", "Dog")
#     pickle.dump(data,f)
#     print("Pickling done ...")




with open('animat.dat',mode='rb') as f:
    data=pickle.load(f)
    print("UNPickling done ...")
    data.speak()
