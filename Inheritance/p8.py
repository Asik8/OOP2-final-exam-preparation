# 8. Create a class Vehicle with attributes make and model. Create subclasses Car and Bike that inherit from Vehicle and have additional attributes like num_doors for cars and num_gears for bikes.

class Vehicle():
    def __init__(self,type,model,color,price):
        self.type = type
        self.model = model
        self.color = color
        self.price = price
    def pri(self):
        print(f"{self.type}'s color is {self.color} and the model is {self.model} with the sell price {self.price}")

class Car(Vehicle):
    def __init__(self, type,model, color, price,num_doors):
        super().__init__(type,model, color, price)
        self.num_doors = num_doors
    
    def pri(self):
        print(f"{self.type}'s color is {self.color} and the model is {self.model} with the sell price {self.price}, No of doors {self.num_doors}")
    

class Bike(Vehicle):
    def __init__(self,type,model,color,price,num_gears):
        super().__init__(type,model,color,price)
        self.num_gears = num_gears
    
    def pri(self):
        print(f"{self.type}'s color is {self.color} and the model is {self.model} with the sell price {self.price}, No of gears {self.num_gears}")

        
c1 = Car("Car","BMW10","Red",1500000,4)
c1.pri()
m1 = Bike("Motorcycle","Honda 20","Black",150000,4)
m1.pri()
