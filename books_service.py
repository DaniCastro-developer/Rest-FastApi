books = [
    {
    "isbn": "19920043920-1",
    "name": "API Design Patterns",
    "publisher": "Talento Futuro",
    "year": "2024",
    "details": "The book provides a comprehensive introduction to the API design paterns that are industry-wide use these days."
    },
    {
    "isbn": "99293948392-1",
    "name": "Backend Software Engineering",
    "publisher": "Talento Futuro",
    "details": "This best-selling book on backend software development in the industry standard for guiding the development of such applications"
    }
]

def get_book_by_isbn(isbn):
    for book in books:
        if book["isbn"] == isbn:
            return {
                "isbn": book["isbn"],
                "name": book["name"],
                "publisher": book["publisher"],
                "year": book["year"]
                }
        
        else:
            return None
        
def get_a_book_details(isbn):
    for book in books:
        if book["isbn"] == isbn:
            return book["details"]