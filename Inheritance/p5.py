# 5. Create a class `Animal` with a method `sound()`. Create subclasses `Cat`, `Cow`, and `Horse`. Each subclass should override the `sound()` method to return the respective animal sound.

class Animal:
    def sound(self):
        print("sounds like gheu gheu!!")
        
class Dog(Animal):
    def sound(self):
        print("sounds like Woof!!")
        
class Cow(Animal):
    def sound(self):
        print("sounds like Hamba!!")
        
class Horse(Animal):
    def sound(self):
        print("sounds like Huuu!!")


d = Dog()
e = Cow()
f = Horse()

for x in (d,e,f):
    x.sound()
