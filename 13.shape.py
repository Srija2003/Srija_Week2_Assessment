class shape():
    def area(self):
        pass      
        
class Square(shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        a=self.a*self.a
        return f"area of square is:{a}"
        
class triangle(shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        a=0.5*self.b*self.h
        return f"the area of triangle is:{a}"
    
t=triangle(2,3)
print(t.area())
s=Square(4)
print(s.area())
    