class Person():
    def __init__(self,name,id,gender):
        self.name = name
        self.id = id
        self.gender = gender
        
    def P(self):
        pass

class SecL(Person):
    def __init__(self,name,id,gender,phone):
        super().__init__(name,id,gender)
        self.phone = phone
    def P(self):
        print(f"I am {self.name}. My Id {self.id}. Gender: {self.gender}.")
        
n = input()
id = int(input())
Abdullah = SecL("n",id,"male",17234542241)
Abdullah.P()
