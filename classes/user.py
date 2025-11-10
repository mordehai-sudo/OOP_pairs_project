from classes.book import Book


class User:
    def __init__(self, name:str, id:str, borrowed_books:list[Book]):
        self.name = name
        self.id = id
        self.borrowed_books = []


