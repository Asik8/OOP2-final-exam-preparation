# 7. Design a class hierarchy for different types of employees in a company. Include a base class Employee and subclasses such as Manager, Engineer, and Salesperson. Each subclass should have attributes specific to their role and appropriate methods.

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

class Engineer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def pri(self):
        print(f"{self.name} Knows {self.programming_language} Programming Language and gets the salary {self.salary}Tk. He Works as a Developer.")

class SalesPerson(Employee):
    def __init__(self, name, salary,total_sales):
        super().__init__(name, salary)
        self.total_sales = total_sales
    
    def pri(self):
        print(f"{self.name} gets the salary {self.salary}Tk. His total sales {self.total_sales}.")
        
m1 = Manager("Siddiq",50000,"Project Manager")
d1 = Engineer("Mahtaf",30000,"Python")
s1 = SalesPerson("Masrafi",25000,'10k')

for x in(m1,d1,s1):
    x.pri()
