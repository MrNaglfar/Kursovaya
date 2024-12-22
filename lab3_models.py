from typing import Optional, Enum
from sqlmodel import Field, SQLModel, Enum
from datetime import date

class Status(Enum):
    Available = "Available"
    Borrowed = "Borrowed"
    Damaged = "Damaged"
    Lost = "Lost"
    Active = "Active"
    Inactive = "Inactive"


class Reader(SQLModel, table=True):
    readerID: Optional[int] = Field(default=None, primary_key=True)
    firstName: str
    lastName: str
    address: str
    phoneNumber: str
    dateOfBirth: date
    registrationDate: date
    status: Status = Status.Active
    libraryCardNumber: str

class Book(SQLModel, table=True):
    bookID: Optional[int] = Field(default=None, primary_key=True)
    ISBN: str
    title: str
    authorID: int = Field(foreign_key="author.authorID")
    publisherID: int = Field(foreign_key="publisher.publisherID")
    publicationYear: int
    numberOfCopies: int
    availableCopies: int
    location: str
    status: Status = Status.Available

class Journal(SQLModel, table=True):
    journalID: Optional[int] = Field(default=None, primary_key=True)
    ISSN: str
    title: str
    publisherID: int = Field(foreign_key="publisher.publisherID")
    publicationYear: int
    issueNumber: int
    numberOfCopies: int
    availableCopies: int
    location: str
    status: Status = Status.Available

class Author(SQLModel, table=True):
    authorID: Optional[int] = Field(default=None, primary_key=True)
    firstName: str
    lastName: str
    dateOfBirth: date
    country: str

class Publisher(SQLModel, table=True):
    publisherID: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str

class Loan(SQLModel, table=True):
    loanID: Optional[int] = Field(default=None, primary_key=True)
    readerID: int = Field(foreign_key="reader.readerID")
    bookID: int = Field(foreign_key="book.bookID")
    loanDate: date
    returnDate: Optional[date] = None
    fine: Optional[float] = 0.0


from sqlmodel import Session, create_engine

engine = create_engine("sqlite:///library.db") 
