class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f'Book: {self.title} {self.author}'

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"PrintBook: {self.title} {self.author}, Page Count: {self.page_count}"

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} {self.author}, File Size: {self.file_size}KB"
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        return self.books.append(book)
        
    def list_books(self):
        for item in self.books:
            print(item)
    