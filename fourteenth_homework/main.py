from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()
class BookCreate(BaseModel):
    title: str
    author: str

class Book(BookCreate):
    id: int

books: list[Book] = []
book_counter: int = 1

@app.get("/books", response_model=list[Book], status_code=status.HTTP_200_OK)
def get_books():
    """Returns a list of all books."""
    return books

@app.get("/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
def get_book(book_id: int):
    """Returns a specific book by its ID."""
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookCreate):
    """Creates a new book and adds it to the list."""
    global book_counter
    new_book = Book(id=book_counter, title=book_in.title, author=book_in.author)
    books.append(new_book)
    book_counter += 1
    return new_book

@app.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
def delete_book(book_id: int):
    """Deletes a book by its ID."""
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully", "book": book}
    raise HTTPException(status_code=404, detail="Book not found")
