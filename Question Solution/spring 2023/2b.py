class StudentManagement():
    def __init__(self,name,id,email):
        self.name = name
        self.id  = id
        self.email = email
    
    def getStudentInfo(self):
        print(f"Name: {self.name} id: {self.id} email: {self.email}")
    
    def courseInfo(self):
        pass
    
    def result(self):
        pass

class examController(StudentManagement):
    def __init__(self,name,id,email,cgpa,duration):
        super().__init__(name,id,email)
        self.cgpa = cgpa
        self.duration = duration
    
    def result(self):
        pass
    
    def examDetails(self):
        pass
    
    def tutionfee(self,fee):
        if self.cgpa>= 3.5 and self.cgpa<3.75:
            fee *= .80
        elif self.cgpa>3.75: 
            fee*= .75
        return fee

s = examController("Asik",4976,"asik@gmail.com",3.0,4)
new_fee = s.tutionfee(100000)
print(f"Tution fee will be {new_fee}")


            
        