# 9. Implement a class hierarchy for different types of shapes. Include a base class Shape and subclasses such as Rectangle, Circle, and Triangle. Each subclass should have methods to calculate its area.
# 6. Define a class Shape with a method area(). Create subclasses Rectangle and Triangle. Override the area() method in each subclass to calculate the area of a rectangle and triangle respectively.

class Shape():
    def area(self):
        raise NotImplementedError("You have to calculate area")
    
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def calculate_area(self):
        print(self.a*self.b)
        
class Circle(Shape):
    def __init__(self,a):
        self.a = a
    
    def calculate_area(self):
        print(self.a*self.a*3.1416)
    
class Triangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def calculate_area(self):
        print(self.a*self.b*0.5)
        
r = Rectangle(10,5)
c = Circle(5)
t = Triangle(10,5)

for x in(r,c,t):
    x.calculate_area()