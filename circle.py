class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calarea(self):
        return (22/7)*self.radius **2
    
    def calperimeter(self):
        return 2 * (22/7)* self.radius



    
c1 = Circle(21)  
print (c1.calarea())
print(c1.calperimeter())     
    
