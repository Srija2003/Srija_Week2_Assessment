class car:
    def move(self):
        print("car moves on road")
        
class airplane():
    def move(self):
        print("airplanes move in air")
class FlyingCar(car,airplane):
    def move(self):
        print("Car moves on road and aeroplanes move in the sky")
        
a=airplane()
c=car()
f=FlyingCar()
a.move()
c.move()
f.move()