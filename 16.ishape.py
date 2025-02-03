from abc import ABC,abstractmethod

class IShape():
    def calculate_area():
        pass
    
class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        area=self.length*self.breadth
        return f"the area of rectangle is {area}"
    
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        area=3.14*self.radius*self.radius
        return f"the area of circle is {area}"
    
c=Circle(3)
print(c.calculate_area())
r=Rectangle(2,3)
print(r.calculate_area())
        
        