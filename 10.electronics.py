class electronics:
    def __init__(self,brand,battery):
        self.brand=brand
        self.battery=battery
    def power_on(self):
        print("the battery is full")
    def power_off(self):
        print("the battery if 0")
        
class mobiledevice(electronics):
    def display(self):
        print("mobile devices")
    def power_on(self):
        print("mobile is in power on mode")
    
class smartphone(mobiledevice):
    def display(self):
        print("smart phones")
    def power_on(self):
        print("smart phone is in power on mode")
        
s=smartphone(input("enter brand:"),input("enter battery:"))

s.display()
s.power_on()

