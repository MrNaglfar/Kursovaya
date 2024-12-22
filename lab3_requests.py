from models import *
from sqlmodel import Session, select

def get_reader_by_id(reader_id: int):
    with Session(engine) as session:
        statement = select(Reader).where(Reader.readerID == reader_id)
        return session.exec(statement).first()


def get_all_books():
    with Session(engine) as session:
        statement = select(Book)
        return session.exec(statement).all()

if __name__ == "__main__":
    reader = get_reader_by_id(1)
    if reader:
        print(f"Читатель: {reader}")
    else:
        print("Читатель не найден")

    books = get_all_books()
    print(f"Все книги: {books}")
