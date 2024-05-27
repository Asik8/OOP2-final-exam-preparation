

class Shape():
    def area(self):
        pass
    
class Rectangle(Shape):
    def area(self,a,b):
        self.a = a
        self.b = b
    
    def pri(self):
        print(self.a*self.b)
    
class Triangle(Shape):
    def area(self,a,b):
        self.a = a
        self.b = b
    
    def pri(self):
        print(self.a*self.b*0.5)
        
r = Rectangle(10,5)
t = Triangle(10,5)

for x in(r,t):
    x.pri()