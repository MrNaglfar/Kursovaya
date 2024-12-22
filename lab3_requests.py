from models import User, Book, Author, Genre, BookIssue
from sqlmodel import Session, select

def get_user_by_id(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.user_id == user_id)
        return session.exec(statement).first()

def get_all_books():
    with Session(engine) as session:
        statement = select(Book)
        return session.exec(statement).all()

def get_books_by_author(author_id: int):
    with Session(engine) as session:
        statement = select(Book).where(Book.author_id == author_id)
        return session.exec(statement).all()


if __name__ == "__main__":
    user = get_user_by_id(1)
    if user:
        print(f"Пользователь: {user}")
    else:
        print("Пользователь не найден")

    books = get_all_books()
    print(f"Все книги: {books}")

    books_by_author = get_books_by_author(1) 
    print(f"Книги автора с id=1: {books_by_author}")
