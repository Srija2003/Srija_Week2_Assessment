class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print("the student details are:")
        print(f"Name:{self.name}\nRoll_no:{self.roll_no}")
        
s=student(input("enter the student name:"),input("enter the roll_no:"))
s.display()