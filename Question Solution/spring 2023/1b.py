# Build in
print(len("Hello"))  # String length
print(len([1, 2, 3, 4, 5]))  # List length
print(len((10, 20, 30)))  # Tuple length

# --------------------------------------------------------------------------------------------------------------

# User Difine
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(10, 20), Circle(5)]

for shape in shapes:
    print(f"Area: {shape.area()}")
