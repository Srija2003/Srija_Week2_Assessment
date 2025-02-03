class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def display(self):
        print(f"Brand:{self.brand}\nmodel:{self.model}")
        
class car(Vehicle):
    def __init__(self,brand,model,doors):
        self.brand=brand
        self.model=model
        self.doors=doors
    def display(self):
        print(f"car doors:{self.doors}\ncar model:{self.model}\ncar brand:{self.brand}")    
        
        
class electriccar(car):
    def __init__(self,brand,model,battery_capacity):
        self.brand=brand
        self.model=model
        self.battery_capacity=battery_capacity
    def display(self):
        print("electric car details")
        print(f"brand:{self.brand},model:{self.brand},battery:{self.battery_capacity}")
        
class bike(Vehicle):
    def __init__(self,brand,model,gears):
        self.brand=brand
        self.model=model
        self.gears=gears
    def display(self):
        print(f"bike model:{self.model}\nbike brand:{self.brand}\nbike gears:{self.gears}")
        
b=bike(input("enter bike brand:"),input("enter bike model:"),input("enter gears:"))
c=car(input("enter car brand:"),input("enter car model:"),input("enter number of doors:"))
e=electriccar(input("enter brand:"),input("enter model:"),input("enter battery:"))
print("the bike details are:")
b.display()
print("the car details are:")
c.display()
print("the electric car details are:")
e.display()
        