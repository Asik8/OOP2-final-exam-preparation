# Define a class Animal with a method sound(). Create subclasses Bird, Dog, and Cat. Each subclass should override the sound() method to return the respective animal sound.

class Animal:
    def sound(self):
        pass

class Bird(Animal):
    def sound(self):
        return "Tweet"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"
