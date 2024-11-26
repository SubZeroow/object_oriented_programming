# Base class: Animal
class Animal:
    def move(self):
        print("The animal moves.")

# Derived class: Dog
class Dog(Animal):
    def move(self):
        print("The dog runs on four legs! 🐶")

# Derived class: Bird
class Bird(Animal):
    def move(self):
        print("The bird flies in the sky! 🦅")

# Base class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle moves on roads.")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("The car drives on roads. 🚗")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("The plane flies in the sky. ✈️")

# Creating objects of Animal and Vehicle
dog = Dog()
bird = Bird()

car = Car()
plane = Plane()

# Demonstrating polymorphism by calling move() on different objects
animals = [dog, bird]
for animal in animals:
    animal.move()

vehicles = [car, plane]
for vehicle in vehicles:
    vehicle.move()
