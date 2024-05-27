# Create a function calculate_area_and_perimeter(shape) that takes an object of a class derived from Shape and returns both the area and perimeter of the shape.

import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)

    # Getter methods to access length and width
    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.__radius

    # Getter method to access radius
    def get_radius(self):
        return self.__radius

def calculate_area_and_perimeter(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    return area, perimeter

