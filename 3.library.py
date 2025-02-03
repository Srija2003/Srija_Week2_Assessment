class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print("The book details are")
        input(f"Book name:{self.title}\nauthor:{self.author}\nisbn:{self.isbn}")
b=Book(input("enter the name of the title:"),input("enter the author name:"),input("enter isbn:"))
b.display()