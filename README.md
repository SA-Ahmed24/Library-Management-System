**Library Management System**

**Project Description**
This Library Management System (LMS) is a backend-focused project designed to facilitate the management of book information in a library. The LMS allows users to add, retrieve, update, and delete book records, with each book containing a title, description, and rating out of 10. This system is built using Python with FastAPI for the web framework and PostgreSQL as the database. The database operations are handled using raw SQL queries to provide a clear understanding of database interactions.

**Features**
- Add Book: Allows users to add a new book with a title, description, and rating. Each book is assigned a unique ID that increments with each new entry.
- Get Book by ID: Retrieve detailed information about a specific book using its unique ID.
- Get Book by Title: Retrieve detailed information about a specific book using its title.
- Get All Books: Retrieve information about all books in the library.
- Update Book: Allows users to update the description and rating of a specific book. Users can choose to update one or both fields without needing to provide the title again.
- Delete Book: Allows users to delete a book from the library using its unique ID.

**Technologies Used**
- Python: The primary programming language used for developing the backend.
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- PostgreSQL: An advanced, open-source relational database used for storing book information.
- Raw SQL: Direct SQL queries are used for database operations, providing clear insights into the interactions with the database.
- Pydantic: Used for data validation and settings management using Python type annotations.

**Project Structure**
- main.py: The main file containing the FastAPI application and endpoint definitions.
- database.py: A module responsible for establishing a connection to the PostgreSQL database.
- init_db.sql: A SQL script for initializing the database and creating the required tables.

**Usage**
The Library Management System can be accessed via HTTP requests using tools like Postman or curl. The API endpoints provide functionality to add, retrieve, update, and delete book records.

**Endpoints**
- Add a Book: POST /books/
- Get Book by ID: GET /books/{book_id}
- Get Book by Title: GET /books/title/{title}
- Get All Books: GET /books/
- Update Book: PATCH /books/{book_id}
- Delete Book: DELETE /books/{book_id}
