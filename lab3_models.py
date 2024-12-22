from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date

class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    surname: str
    name: str
    patronymic: str
    address: str
    phone_number: str
    registration_date: date
    email: str

class Book(SQLModel, table=True):
    book_id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    isbn: str
    publication_year: int
    quantity: int
    available_copies: int
    author_id: int = Field(foreign_key="author.author_id")
    genre_id: int = Field(foreign_key="genre.genre_id")

class Author(SQLModel, table=True):
    author_id: Optional[int] = Field(default=None, primary_key=True)
    surname: str
    name: str
    patronymic: str

class Genre(SQLModel, table=True):
    genre_id: Optional[int] = Field(default=None, primary_key=True)
    genre_name: str

class BookIssue(SQLModel, table=True):
    issue_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    book_id: int = Field(foreign_key="book.book_id")
    issue_date: date
    return_date: Optional[date] = None

from sqlmodel import Session, create_engine

engine = create_engine("postgresql://postgres:6462523509@localhost:4578/postgres")
