# Create a class Person with private attributes __name, __age, and __gender. Provide public methods to set and get these attributes.

class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__gender = ""
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_gender(self, gender):
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
