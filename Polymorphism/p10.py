# Define a class Operation with a method perform(). Create subclasses Addition, Subtraction, Multiplication, and Division. Each subclass should override the perform() method to perform the respective arithmetic operation.

class Operation:
    def perform(self, x, y):
        pass

class Addition(Operation):
    def perform(self, x, y):
        return x + y

class Subtraction(Operation):
    def perform(self, x, y):
        return x - y

class Multiplication(Operation):
    def perform(self, x, y):
        return x * y

class Division(Operation):
    def perform(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
