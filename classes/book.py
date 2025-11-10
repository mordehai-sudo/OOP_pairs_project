class Book:
    def __init__(self, title: str, auther: str, isbn,is_available:bool ):
        self.title = title
        self.auther = auther
        self.isnb = isbn
        self.is_available = True


    def __str__(self):
        print(f"title: {self.title} auther: {self.auther} ISBN : {self.isnb} is availabe: {self.is_available}")