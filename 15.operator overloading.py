class Book:
    def __init__(self,title,author):
        self.title=title
        self.author =author
        
    def __add__(self,other):
        if isinstance(other,Book):
            return Book(f"{self.title} & {other.title}", self.author)
        
    def __str__(self):
        return f"Book:{self.title}, Author :{self.author}"
    
book1 = Book("The Harry Porter","J.K Hary")
book2 = Book("The Island","J.K Hary")

series = book1+book2
print(series)