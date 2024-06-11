# Import necessary libraries and modules
from fastapi import FastAPI, HTTPException  # FastAPI framework and HTTP exception handling
from pydantic import BaseModel  # Data validation using Pydantic
import psycopg2  # PostgreSQL database adapter for Python
from psycopg2.extras import RealDictCursor  # Cursor to return dictionaries instead of tuples
from database import get_db_connection  # Custom module to get database connection
from typing import Optional  # Optional type for fields that can be None

# Initialize the FastAPI application
app = FastAPI()

# Define a Pydantic model for the Book entity
class Book(BaseModel):
    title: str  # Title of the book
    description: str  # Description of the book
    rating: int  # Rating of the book

# Define a Pydantic model for updating the Book entity
class BookUpdate(BaseModel):
    title: Optional[str] = None  # Title of the book (optional)
    description: Optional[str] = None  # Description of the book (optional)
    rating: Optional[int] = None  # Rating of the book (optional)

# Define an endpoint to create a new book
@app.post("/books/")
async def create_book(book: Book):
    # Get a database connection
    conn = get_db_connection()
    # To use sql statements/queries
    cursor = conn.cursor() 
    # Insert a new book into the books table and return the new book's ID
    cursor.execute(
        "INSERT INTO books (title, description, rating) VALUES (%s, %s, %s) RETURNING id",
        (book.title, book.description, book.rating)
    )
    book_id = cursor.fetchone()[0]  # Get the ID of the newly created book
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the connection
    return {"id": book_id, "title": book.title, "description": book.description, "rating": book.rating}

# Define an endpoint to retrieve a book by its ID
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    # Get a database connection
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    # Execute a query to find the book by its ID
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()  # Fetch the result as a dictionary
    cursor.close()  # Close the cursor
    conn.close()  # Close the connection
    if book is None:
        # If the book is not found, raise a 404 HTTP exception
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Define an endpoint to retrieve a book by its title
@app.get("/books/title/{title}")
async def get_book_by_title(title: str):
    # Get a database connection
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    # Execute a query to find the book by its title
    cursor.execute("SELECT * FROM books WHERE title = %s", (title,))
    book = cursor.fetchone()  # Fetch the result as a dictionary
    cursor.close()  # Close the cursor
    conn.close()  # Close the connection
    if book is None:
        # If the book is not found, raise a 404 HTTP exception
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Define an endpoint to retrieve all books
@app.get("/books/")
async def get_all_books():
    # Get a database connection
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    # Execute a query to get all books
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()  # Fetch all results as a list of dictionaries
    cursor.close()  # Close the cursor
    conn.close()  # Close the connection
    return books

# Define an endpoint to update a book
@app.patch("/books/{book_id}")
async def update_book(book_id: int, book: BookUpdate):
    # Get a database connection
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get the current state of the book
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    existing_book = cursor.fetchone()  # Fetch the current book details
    if existing_book is None:
        cursor.close()
        conn.close()
        # If the book is not found, raise a 404 HTTP exception
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Prepare the update fields, using existing values if no new values are provided
    updated_title = book.title if book.title is not None else existing_book[1]
    updated_description = book.description if book.description is not None else existing_book[2]
    updated_rating = book.rating if book.rating is not None else existing_book[3]

    # Execute the update query
    cursor.execute(
        "UPDATE books SET title = %s, description = %s, rating = %s WHERE id = %s",
        (updated_title, updated_description, updated_rating, book_id)
    )
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the connection
    return {"message": "Book updated successfully"}

# Define an endpoint to delete a book
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    # Get a database connection
    conn = get_db_connection()
    cursor = conn.cursor()
    # Execute a query to delete the book by its ID
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()  # Commit the transaction
    cursor.close()  # Close the cursor
    conn.close()  # Close the connection
    return {"message": "Book deleted successfully"}
