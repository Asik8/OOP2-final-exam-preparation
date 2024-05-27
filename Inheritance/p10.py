# 10. Define a class Person with attributes name and age. Create subclasses Teacher and Student. Teachers have an additional attribute subject, while students have grade. Implement appropriate methods for each subclass.

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    def pri(self):
        print(f"Teacher name: {self.name}. Tacher age {self.age}. Subject {self.subject}")
        
class Students(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def pri(self):
        print(f"Student name: {self.name}. Tacher age {self.age}. grade {self.grade}")
        
t = Teacher("Siddiq",40,"History")
s = Students("Asik",23,3.80)

for x in(t,s):
    x.pri()