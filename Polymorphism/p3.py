# Define a class Animal with a method sound(). Create subclasses Cat, Cow, and Horse. Each subclass should override the sound() method to return the respective animal sound.

class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

class Horse(Animal):
    def sound(self):
        return "Neigh"
