from models import *
from sqlmodel import Session, select
from datetime import date

with Session(engine) as session:
    # ���������� ���������
    publisher1 = Publisher(name="����, ������ � ������", address="������")
    publisher2 = Publisher(name="������� ��������", address="�����-���������")
    session.add(publisher1)
    session.add(publisher2)
    session.commit()
    session.refresh(publisher1)
    session.refresh(publisher2)

    # ���������� �������
    author1 = Author(firstName="������", lastName="����", dateOfBirth=date(1947, 9, 21), country="���")
    author2 = Author(firstName="������", lastName="�������", dateOfBirth=date(1965, 7, 31), country="��������������")
    session.add(author1)
    session.add(author2)
    session.commit()
    session.refresh(author1)
    session.refresh(author2)

    # ���������� ����
    book1 = Book(title="���", ISBN="978-5-00110-172-2", authorID=author1.authorID, publisherID=publisher1.publisherID, publicationYear=1986, numberOfCopies=5, availableCopies=3, location="������� �1")
    book2 = Book(title="����� ������ � ����������� ������", ISBN="978-5-17-073429-8", authorID=author2.authorID, publisherID=publisher2.publisherID, publicationYear=1997, numberOfCopies=10, availableCopies=7, location="������� B2")
    session.add(book1)
    session.add(book2)
    session.commit()
    session.refresh(book1)
    session.refresh(book2)


    # ���������� ���������
    reader1 = Reader(firstName="����", lastName="������", address="��. ������, 1", phoneNumber="+79123456789", dateOfBirth=date(1990, 5, 10), registrationDate=date(2023, 10, 26), libraryCardNumber="12345")
    session.add(reader1)
    session.commit()
    session.refresh(reader1)

    # ���������� ������
    loan1 = Loan(readerID=reader1.readerID, bookID=book1.bookID, loanDate=date(2023,10,27))
    session.add(loan1)
    session.commit()
    session.refresh(loan1)
