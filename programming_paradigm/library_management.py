class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
class Library(Book):
    def __init__(self):
        super().__init__()
        self._books = []
          
    def add_book(self, *args):
        book = self._books.append(Book(args))
        return f'addbook {book}'
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return f'{self.title} is'
        pass
    def return_book(self, title):
        pass
    def list_available_books(self):
        pass
    