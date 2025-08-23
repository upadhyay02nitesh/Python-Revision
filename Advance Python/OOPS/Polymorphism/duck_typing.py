class Duck:
    def walk(self):
        print("Walking on webbed feet")

    def quack(self):
        print("Quack Quack")

class Dog:
    def walk(self):
        print("Walking on all fours")

    def bark(self):
        print("Woof Woof")

def perform_actions(animal):
    animal.walk()  # Both Duck and Dog have walk()


d=Duck()
perform_actions(d)

d=Dog()
perform_actions(d)