from models import User, Book, Author, Genre, BookIssue
from sqlmodel import Session, select
from datetime import date

with Session(engine) as session:
    author1 = Author(surname="Толстой", name="Лев", patronymic="Николаевич")
    author2 = Author(surname="Достоевский", name="Фёдор", patronymic="Михайлович")
    session.add(author1)
    session.add(author2)
    session.commit()
    session.refresh(author1)
    session.refresh(author2)

    genre1 = Genre(genre_name="Роман")
    genre2 = Genre(genre_name="Повесть")
    session.add(genre1)
    session.add(genre2)
    session.commit()
    session.refresh(genre1)
    session.refresh(genre2)

    book1 = Book(title="Война и мир", isbn="978-5-17-091266-1", publication_year=1869, quantity=10, available_copies=5, author_id=author1.author_id, genre_id=genre1.genre_id)
    book2 = Book(title="Преступление и наказание", isbn="978-5-17-091173-2", publication_year=1866, quantity=8, available_copies=3, author_id=author2.author_id, genre_id=genre1.genre_id)
    session.add(book1)
    session.add(book2)
    session.commit()
    session.refresh(book1)
    session.refresh(book2)


    user1 = User(surname="Иванов", name="Иван", patronymic="Иванович", address="ул. Пушкина, 1", phone_number="+79123456789", registration_date=date(2023, 10, 26), email="ivanov@example.com")
    session.add(user1)
    session.commit()
    session.refresh(user1)

    book_issue1 = BookIssue(user_id=user1.user_id, book_id=book1.book_id, issue_date=date(2023, 10, 27))
    session.add(book_issue1)
    session.commit()
    session.refresh(book_issue1)
