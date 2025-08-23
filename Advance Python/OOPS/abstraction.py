# What is Abstraction?

# Abstraction means hiding implementation details and showing only essential features to the user.

# You don’t care how something works internally, you only care about what it does.

# When you drive a car, you only use the steering wheel, accelerator, brake → you don’t bother how the engine works inside. That’s abstraction.

# In Python, abstraction is mainly achieved using Abstract Base Classes (ABC).

# We use the abc module (ABC, abstractmethod).

# Abstract class: a class that cannot be instantiated directly.

# Abstract method: a method that is declared but not implemented in the base class.

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):   # Abstract method (only definition, no body)
        pass

    @abstractmethod
    def stop(self):
        pass


# Concrete class implementing abstract class
class Car(Vehicle):

    def start(self):
        print("Car started with key ignition")

    def stop(self):
        print("Car stopped using brakes")


class Bike(Vehicle):

    def start(self):
        print("Bike started with self-start button")

    def stop(self):
        print("Bike stopped with disc brakes")
    
    def kick_start(self):
        print("Bike kick-started")

#         ✅ In short:

# Abstraction = enforces must-have methods.

# Subclasses = free to add extra features.

# That’s why bike.kick_start() works.


# Usage
car = Car()
car.start()
car.stop()

bike = Bike()
bike.start()
bike.stop()
bike.kick_start()




# 🔹 Key Points

# Vehicle is abstract → can’t create v = Vehicle().

# Classes Car and Bike implement the abstract methods.

# Abstraction ensures a blueprint → every child must provide its own implementation.

# 🔹 Where is Abstraction Used in Real Life Code?

# Database drivers (you just call .connect(), you don’t care about the low-level protocol).

# Payment gateways (you just call make_payment(), not how encryption/transfer works).

# Machine Learning frameworks (e.g., model.fit(X, y) → you don’t see gradient descent math).