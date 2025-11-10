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

        borrow_book_index = self.books.index(book_isbn)
        user_index = self.users.index(user_id)
        book = self.books[borrow_book_index]
        user = self.users[user_index]
        book.is_available = False
        user.borrowed_books.append(book)

    def return_book(self,user_id,book_isbn):
        book_index = self.books.index(book_isbn)
        user_index = self.users.index(user_id)
        book = self.books[book_index]
        user = self.users[user_index]
        book.is_available = True
        del user.borrowed_books[book_index]

    def list_available_books(self) -> list[Book]:
        available_books = []
        for book in self.books:
            if book.is_available:
                available_books.append(book)
        return available_books

    def search_book(self, search: str):
        for book in self.books:
            if book.title == search or book.title == search:
                return book

        return None

