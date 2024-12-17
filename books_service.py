from models import BookModel
from fastapi import HTTPException
import random

temporary_reviews = []

books = [
    {
    "isbn": "19920043920-1",
    "name": "API Design Patterns",
    "publisher": "Talento Futuro",
    "year": "2024",
    "details": "The book provides a comprehensive introduction to the API design paterns that are industry-wide use these days.",
    "reviews" : []
    },
    {
    "isbn": "99293948392-1",
    "name": "Backend Software Engineering",
    "publisher": "Talento Futuro",
    "details": "This best-selling book on backend software development in the industry standard for guiding the development of such applications",
     "reviews" : []
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
        
def add_a_book(book_request: BookModel):
    for book in books:
        if book["isbn"] == book_request.isbn:
            raise HTTPException(
                status_code=400, detail=f"Book with ISBN {book_request.isbn} already exists."
            )
        
    books.append(book)
    return book

def delete_book(isbn):
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            return True
        else:
            return False

def add_book_review_to_validation(isbn, review):
    # add to review
    temporary_review_id = random.randint(0,1000)
    temporary_reviews.append(
        {
            "isbn": isbn,
            "temporary_review_id": temporary_review_id,
            "review": review,
        }
    )
    # after review validation...
    for book in books:
        if book["isbn"] == isbn:
            if "reviews" not in book:
                book["reviews"] = []
            book["reviews"].append({
                "review_id": temporary_review_id,
                "review": review,
            })

    return temporary_review_id



def review_by_id(review_id):
    for book in books:
        for review in book["reviews"]:
            if str(review["review_id"]) == str(review_id):
                return review["review"]
            

def validate_book_review(temporary_review_id):
    review_id = None
    review_book_isbn = None
    review = None

    for index, temporary_review in enumerate(temporary_reviews):
        if temporary_review["temporary_review_id" == temporary_review_id]:
            temporary_review_index = index
            review_id = temporary_review_id
            review_book_isbn = temporary_review["isbn"]
            review = temporary_review["review"]
        if not review_id:
            return None
        
        for book in books:
            if book["isbn"] not in book:
                if "reviews" not in book:
                    book["reviews"] = []

                book["reviews"].append(
                    {
                        "review_id": review_id,
                        "review": review
                    }
                )
    
    return review_id