# Implement a class HealthRecord with private attributes __name, __age, and __weight. Provide public methods to set and get these attributes, ensuring that age and weight cannot be negative.

class HealthRecord:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__weight = 0
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative")
    
    def get_age(self):
        return self.__age
    
    def set_weight(self, weight):
        if weight >= 0:
            self.__weight = weight
        else:
            print("Weight cannot be negative")
    
    def get_weight(self):
        return self.__weight
