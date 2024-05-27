# Create a function calculate_volume(shape) that takes an object of a class derived from Shape (e.g., Cube or Cylinder) and returns the volume of the shape.

import math

class Shape:
    def volume(self):
        pass

class Cube(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length

    def volume(self):
        return self.__side_length ** 3

    def get_side_length(self):
        return self.__side_length

class Cylinder(Shape):
    def __init__(self, radius, height):
        self.__radius = radius
        self.__height = height

    def volume(self):
        return math.pi * self.__radius ** 2 * self.__height

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

def calculate_volume(shape):
    return shape.volume()

# Test the function
cube = Cube(3)
cylinder = Cylinder(2, 5)

print("Volume of the cube:", calculate_volume(cube))
print("Volume of the cylinder:", calculate_volume(cylinder))
