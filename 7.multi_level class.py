class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print("the person details: ")
        print(f"name:{self.name},age:{self.age}")


class Employee(Person):
    def __init__(self,name,age,id,salary,position,experience):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
        self.position=position
        self.experience=experience
        
    def details(self):
        print("the employee details:")
        print(f"name:{self.name},id:{self.id},salary:{self.salary},position:{self.position},experience:{self.experience}")
        
class Manager(Employee):
    def __init__(self,name,age,id,salary,position,experience):
        super().__init__(name,age,id,salary,position,experience)
        
    def details(self):
        print("the manager details:")
        print(f"name:{self.name},id:{self.id},salary:{self.salary},position:{self.position},experience:{self.experience}")
        
    def approv_leave(self):
        print("Leave has been approved")
        
m=Manager(input("enter name:"),input("enter age:"),input("enter id:"),input("enter salary:"),input("enter position:"),input("enter experience:"))
m.details()
m.approv_leave()

e=Employee(input("enter name:"),input("enter age:"),input("enter id:"),input("enter salary:"),input("enter position:"),input("enter experience:"))
e.details()

p=Person(input("enter name:"),input("enter age:"))
p.details()
