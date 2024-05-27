# 4. Design a class hierarchy for different types of electronic devices. Include a base class `Device` and subclasses such as `Phone`, `Laptop`, and `Tablet`. Ensure that each subclass has specific attributes and methods.

class Device():
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price
    def pri(self):
        print(f"Color is {self.color} and the model is {self.model} with the sell price {self.price}")

class Phone(Device):
    def __init__(self,model, color, price):
        super().__init__(model, color, price)

class Laptop(Device):
    def __init__(self,model,color,price):
        super().__init__(model,color,price)

class Tablet(Device):
    def __init__(self,model,color,price):
        super().__init__(model,color,price)
        
c1 = Phone("Realme","Red",15000)
m1 = Laptop("Lenovo","Black",150000)
t1 = Tablet("Mi","Silver",20000)

for x in(c1,m1,t1):
    x.pri()