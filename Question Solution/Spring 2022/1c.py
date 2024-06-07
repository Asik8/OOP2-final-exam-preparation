class Employee:
    def __init__(self,name,email,salary):
        self.name = name
        self.email = email
        self.salary = salary
    
    def checkin(self):
        print("Check in at 9am")
    def checkout(self):
        print("Check Out at 5pm")
    
class Admin(Employee):
    def __init__(self,name,email,salary):
        super().__init__(name,email,salary)
    
    def Management(self):
        pass
    def Monitoring(self):
        pass
    def checkin(self):
        print("Check in at 8am")
    def checkout(self):
        print("Check Out at 6pm")
    def RaiseSalary(self):
        up = self.salary*.15
        self.salary+=up
        print(self.salary)
        
class Faculty(Employee):
    def __init__(self,name,email,salary):
        super().__init__(name,email,salary)
    
    def COnductingClass(self):
        pass
    def Councelling(self):
        pass
    def checkin(self):
        print("Check in at 9:30 am")
    def checkout(self):
        print("Check Out at 5:30 pm")
    def RaiseSalary(self):
        up = self.salary*.10
        self.salary+=up
        print(self.salary)
        
# e1 = Employee("Asik","agdhgvggs",100000)
# e1.checkin()
# e1.checkout()

a1 = Admin("Asik","agdhgvggs",100000)
a1.RaiseSalary()