# class EncapsulationExample:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age  # Private attribute __ for private and _ for protect

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.__age}")

# obj = EncapsulationExample("Alice", 30)
# obj.display()

# --------------------------------------------------------------------------------------------------------------
# Example of Inheritance
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(f"Parent Name: {self.name}")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def display(self):
#         super().display()
#         print(f"Child Age: {self.age}")

# child = Child("John", 12)
# child.display()

# --------------------------------------------------------------------------------------------------------------
# polymorphism
# class Animal:
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# def make_sound(animal):
#     print(animal.sound())

# dog = Dog()
# cat = Cat()
# make_sound(dog)
# make_sound(cat)

# --------------------------------------------------------------------------------------------------------------
