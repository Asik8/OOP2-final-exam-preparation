# 1. Define a class `Animal` with a method `sound()`. Create a subclass `Dog` that inherits from `Animal` and overrides the `sound()` method to return "Woof".

class Animal:
    def sound(self):
        print("sounds like gheu gheu!!")
        
class Dog(Animal):
    def sound(self):
        print("sounds like Woof!!")


d = Dog()
d.sound()