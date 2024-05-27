# 3. Create a class `Employee` with attributes `name` and `salary`. Create subclasses `Manager` and `Developer`. Managers have an additional attribute `department`, while Developers have `programming_language`. Implement appropriate methods for each subclass.

class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    
    def pri(self):
        print(f"{self.name} works on the {self.department} and gets the salary {self.salary}Tk. He Works as a Manager.")

class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def pri(self):
        print(f"{self.name} Knows {self.programming_language} Programming Language and gets the salary {self.salary}Tk. He Works as a Developer.")
        
m1 = Manager("Siddiq",50000,"Project Manager")
d1 = Developer("Mahtaf",30000,"Python")

for x in(m1,d1):
    x.pri()
