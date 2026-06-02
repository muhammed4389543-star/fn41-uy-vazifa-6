from sqlalchemy.orm import Session
from app.db import models
from app.schemas import books_schemas


def get_all_books(db: Session):
    return db.query(models.Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_book(db: Session, book: books_schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        published_year=book.published_year,
        pages=book.pages
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, db_book: models.Book, book_update: books_schemas.BookCreate):
    db_book.title = book_update.title
    db_book.author = book_update.author
    db_book.published_year = book_update.published_year
    db_book.pages = book_update.pages
    
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, db_book: models.Book):
    db.delete(db_book)
    db.commit()
    return True


def search_by_author(db: Session, author_name: str):
    return db.query(models.Book).filter(models.Book.author.ilike(f"%{author_name}%")).all()