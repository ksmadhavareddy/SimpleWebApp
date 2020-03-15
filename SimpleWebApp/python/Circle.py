class Circle:
    def __init__(self, radius =1):
        self.radius = radius;
    
    def _str__(self):
        return f" radius: {self.radius} " 
    
mycircle = Circle(10);
    
print(mycircle);