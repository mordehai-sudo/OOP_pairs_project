from classes.book import Book
from classes.user import User


class Library:
    def __init__(self):
        self.users = []
        self.books = []

    def add_book(self, book:Book):
        self.books.append(book)


    def add_use(self,user:User):
        self.users.append(user)

    def borrow_book(self,user_id,book_isbn):
        pass

    def return_book(self,user_id,book_isbn):
        pass

    def list_available_books(self) -> list[Book]:
        pass

    def search_book(self,search):
        pass


