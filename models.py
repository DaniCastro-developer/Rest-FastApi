from pydantic import BaseModel

class BookModel(BaseModel):
    isbn: str
    name: str
    publisher: str
    year: int