from fastapi import FastAPI, HTTPException
from books_service import get_book_by_isbn, get_a_book_details

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

#HATEOAS (hipervinculos)
@app.get("/book/{book_id}")
def get_book(book_id: str):
    if not 10 <= len(book_id) <=13:
          raise HTTPException(status_code=400, detail="Invalid ISBN format")
    
    book_data = get_book_by_isbn(book_id)
    if not book_data:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book_data["details"] = "http://localhost:8000/book/details/" + book_id
    return book_data


@app.get("/book/details/{book_id}")
def get_book_details(book_id: str):
    book_details = get_a_book_details(book_id)
    book_data = {"isbn": book_id, "details": book_details}
    return book_data
