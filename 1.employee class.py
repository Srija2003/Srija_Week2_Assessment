class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def display(self):
        self.name=input("enter the name:")
        self.id=input("enther the employee id:")
        self.department=input("enter the department:")
        
    
obj=Employee("","","")
obj.display()
print(f"employee name:{obj.name}\nemployee id:{obj.id}\nemployee department:{obj.department}")

            