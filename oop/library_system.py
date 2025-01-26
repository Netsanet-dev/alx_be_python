class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
        
class Library:
    def add_book(self, book):
        new_book = len(book)
        books = Book(book)
        return books
    
    def list_books(self):
        pass    
    