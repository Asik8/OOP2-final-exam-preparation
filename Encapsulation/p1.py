# 1. Create a class `Student` with private attributes `__name` and `__age`. Provide public methods to set and get these attributes.

class Student:
    def __init__(self):
        self.__name = ""
        self.__age = 0
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age

