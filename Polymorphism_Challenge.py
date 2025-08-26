# Base class
class Animal:
    def move(self):
        pass  # generic action

# Derived classes with different implementations
class Dog(Animal):
    def move(self):
        print("Dog is running 🐕")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

# Demonstrate polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
