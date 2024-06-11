CREATE DATABASE library_db;

\c library_db;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    rating INTEGER CHECK (rating >= 0 AND rating <= 10)
);
