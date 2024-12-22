from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Reader, Book, Author, Loan, Status, engine
from sqlmodel import Session, select, insert, update, delete

app = FastAPI()

class ReaderCreate(BaseModel):
    firstName: str
    lastName: str
    address: str
    phoneNumber: str
    dateOfBirth: str
    libraryCardNumber: str

class LoanCreate(BaseModel):
    readerID: int
    bookID: int


@app.get("/readers/{reader_id}", response_model=Reader)
def get_reader(reader_id: int):
    with Session(engine) as session:
        reader = session.exec(select(Reader).where(Reader.readerID == reader_id)).first()
        if reader is None:
            raise HTTPException(status_code=404, detail="Reader not found")
        return reader


@app.get("/readers", response_model=List[Reader])
def get_all_readers():
    with Session(engine) as session:
        readers = session.exec(select(Reader)).all()
        return readers


@app.post("/readers", response_model=Reader, status_code=201)
def create_reader(reader: ReaderCreate):
    with Session(engine) as session:
        new_reader = Reader(firstName=reader.firstName, lastName=reader.lastName, address=reader.address,
                             phoneNumber=reader.phoneNumber, dateOfBirth=reader.dateOfBirth, libraryCardNumber=reader.libraryCardNumber, registrationDate=date.today())
        session.add(new_reader)
        session.commit()
        session.refresh(new_reader)
        return new_reader

@app.get("/books", response_model=List[Book])
def get_all_books():
    with Session(engine) as session:
        books = session.exec(select(Book)).all()
        return books

@app.post("/loans", response_model=Loan, status_code=201)
def create_loan(loan: LoanCreate):
    with Session(engine) as session:
        new_loan = Loan(readerID=loan.readerID, bookID=loan.bookID, loanDate=date.today())
        session.add(new_loan)
        session.commit()
        session.refresh(new_loan)
        return new_loan

@app.get("/authors", response_model=List[Author])
def get_all_authors():
    with Session(engine) as session:
        authors = session.exec(select(Author)).all()
        return authors
