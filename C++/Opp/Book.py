

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show(self):
        print(f"title :{self.title} author {self.author} pages {self.pages}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.title)

    def search_book_title(self,title):
        for book in self.books:
            if book.title == title:
                print("encontrado")

    def search_book_author(self,author):
        for book in self.books:
            if book.author == author:
                print("encontrado")


harry = Book("Harry","Kevin", 250)
KevinLibrary = Library()



KevinLibrary.add_book(harry)
KevinLibrary.show_books()
KevinLibrary.search_book_title("Harry")
KevinLibrary.search_book_author("Kevin")