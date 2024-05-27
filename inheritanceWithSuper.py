class ball():
    def __init__(self,name,shape,color,weight):
        self.shape = shape
        self.color = color
        self.weight = weight
        self.name = name
        
    def pr(self):
        print(f"I am a {self.name}")
        print(f"My shape is {self.shape}")
        print(f"My color is {self.color}")
        print(f"My weight is {self.weight}g")
    
class Cricket(ball):
    def __init__(self,name,shape,color,weight):
        super().__init__(name, shape, color, weight)  # Calling the parent class constructor
        

cr = Cricket("Cricket Ball", "Circle", "Red", 150)
cr.pr()
