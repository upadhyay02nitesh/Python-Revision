class Duck:
    def walk(self):
        print("Walking on webbed feet")

    def quack(self):
        print("Quack Quack")

class Dog:
    def talk(self):
        print("Walking on all fours")

    def bark(self):
        print("Woof Woof")

def perform_actions(animal):
    if hasattr(animal, 'talk'):
        animal.talk()
    else:
        print("This animal can't talk")

d=Duck()
perform_actions(d)

d=Dog()
perform_actions(d)