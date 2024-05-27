# Define a class Vehicle with a method drive(). Create subclasses Car and Motorcycle. Each subclass should override the drive() method to simulate driving the respective vehicle.

class Vehicle:
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Car is being driven"

class Motorcycle(Vehicle):
    def drive(self):
        return "Motorcycle is being driven"
