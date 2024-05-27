# 2. Create a class hierarchy for different types of vehicles. Include a base class `Vehicle` and subclasses such as `Car`, `Motorcycle`, and `Truck`. Ensure that each subclass has appropriate attributes and methods.

class Vehicle():
    def __init__(self,type,model,color,price):
        self.type = type
        self.model = model
        self.color = color
        self.price = price
    def pri(self):
        print(f"{self.type}'s color is {self.color} and the model is {self.model} with the sell price {self.price}")

class Car(Vehicle):
    def __init__(self, type,model, color, price):
        super().__init__(type,model, color, price)

class Motorcycle(Vehicle):
    def __init__(self,type,model,color,price):
        super().__init__(type,model,color,price)

class turck(Vehicle):
    def __init__(self,type,model,color,price):
        super().__init__(type,model,color,price)
        
c1 = Car("Car","BMW10","Red",1500000)
c1.pri()
m1 = Motorcycle("Motorcycle","Honda 20","Black",150000)
m1.pri()
t1 = turck("Truck","Tata11w","Yellow",2000000)
t1.pri()