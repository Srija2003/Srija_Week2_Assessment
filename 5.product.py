class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def display(self):
        print("The Product details are:")
        print(f"name:{self.name}\nprice:{self.price}\nstock:{self.stock}")
    def check_availability(self):
        q=int(self.stock)
        print("enter the quantity you need:")
        n=int(input())
        
        if n > q:
            print("the requested quantity is not available:")
        else:
            q-=n
            print(f"the remining quantity is:{q}")
p=Product(input("enter the product name:"),input("enter the price:"),input("enter the stock:"))
p.display()
p.check_availability()