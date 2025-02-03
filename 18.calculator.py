from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    def subtract(self,a,b):
        pass
    def multiply(self,a,b):
        pass
    def divide(self,a,b):
        pass
class BasicCalculator():
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def  divide(self,a,b):
        return a/b
    
c=BasicCalculator()
print(c.add(10,3))
print(c.subtract(10,5))
print(c.multiply(2,3))
print(c.divide(10,5))
    