from fastapi import FastAPI, HTTPException
import books_service 
from models import BookModel, BookReviewModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

#HATEOAS (hipervinculos)
@app.get("/book/{book_id}")
def get_book(book_id: str):
    if not 10 <= len(book_id) <=13:
          raise HTTPException(status_code=400, detail="Invalid ISBN format")
    
    book_data = books_service.get_book_by_isbn(book_id)
    if not book_data:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book_data["details"] = "http://localhost:8000/book/details/" + book_id
    return book_data


@app.get("/book/details/{book_id}")
def get_book_details(book_id: str):
    book_details = books_service.get_a_book_details(book_id)
    book_data = {"isbn": book_id, "details": book_details}
    return book_data

@app.post("/book")
def add_new_book(book: BookModel):
    return books_service.add_a_book(book)

@app.delete("/book/{book_id}", status_code=204)
def delete_a_book(book_id:str):
    if not 10 <= len(book_id) <=13:
        raise HTTPException(status_code=400, detail="Invalid ISBN format")
    
    if books_service.delete_book(book_id):
        return True
    else:
        raise HTTPException(status_code=400, detail="Problems deleting book")


#Reviews books async action
@app.post("/book/review", status_code=202)
def add_book_review(book_review: BookReviewModel):
    review_temporary_id = books_service.add_book_review_to_validation(book_review.isbn, book_review.review)
    response_content = {
        "review_id": review_temporary_id,
        "status": "http://localhost:8000/book/review/" + str(review_temporary_id) + "/status"
    }
    return response_content

@app.post("/book/review/{temporary_review_id}", status_code= 201)
def validate_book_review(temporary_review_id:int):
    review_id = books_service.validate_book_review(temporary_review_id)


@app.get("/book/review/{review_id}/status", status_code=303)
def get_book_review_status(review_id: str):
    # if review is validated...
    return {
        "review_id": review_id,
        "review": "http://localhost:8000/book/review/" + review_id
    }


@app.get("/book/review/{review_id}")
def get_book_review(review_id: str):
    review = books_service.review_by_id(review_id)
    return {
        "review_id": review_id,
        "review": review
    }