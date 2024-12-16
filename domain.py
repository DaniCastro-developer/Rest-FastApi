class Book:
    def __init__(self, isbn, name, publisher, year):
        self.isbn = isbn
        self.name = name
        self.publisher = publisher
        self.year = year

def __dict__(self):
    return {
    "isbn": self.isbn,
    "name": self.name,
    "publisher": self.publisher,
    "year": self.year
    }