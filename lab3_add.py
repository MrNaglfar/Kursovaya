from models import *
from sqlmodel import Session, select
from datetime import date

with Session(engine) as session:
    # Добавление издателей
    publisher1 = Publisher(name="Манн, Иванов и Фербер", address="Москва")
    publisher2 = Publisher(name="Альпина Паблишер", address="Санкт-Петербург")
    session.add(publisher1)
    session.add(publisher2)
    session.commit()
    session.refresh(publisher1)
    session.refresh(publisher2)

    # Добавление авторов
    author1 = Author(firstName="Стивен", lastName="Кинг", dateOfBirth=date(1947, 9, 21), country="США")
    author2 = Author(firstName="Джоанн", lastName="Роулинг", dateOfBirth=date(1965, 7, 31), country="Великобритания")
    session.add(author1)
    session.add(author2)
    session.commit()
    session.refresh(author1)
    session.refresh(author2)

    # Добавление книг
    book1 = Book(title="Оно", ISBN="978-5-00110-172-2", authorID=author1.authorID, publisherID=publisher1.publisherID, publicationYear=1986, numberOfCopies=5, availableCopies=3, location="Стеллаж А1")
    book2 = Book(title="Гарри Поттер и философский камень", ISBN="978-5-17-073429-8", authorID=author2.authorID, publisherID=publisher2.publisherID, publicationYear=1997, numberOfCopies=10, availableCopies=7, location="Стеллаж B2")
    session.add(book1)
    session.add(book2)
    session.commit()
    session.refresh(book1)
    session.refresh(book2)


    # Добавление читателей
    reader1 = Reader(firstName="Иван", lastName="Иванов", address="ул. Ленина, 1", phoneNumber="+79123456789", dateOfBirth=date(1990, 5, 10), registrationDate=date(2023, 10, 26), libraryCardNumber="12345")
    session.add(reader1)
    session.commit()
    session.refresh(reader1)

    # Добавление выдачи
    loan1 = Loan(readerID=reader1.readerID, bookID=book1.bookID, loanDate=date(2023,10,27))
    session.add(loan1)
    session.commit()
    session.refresh(loan1)
