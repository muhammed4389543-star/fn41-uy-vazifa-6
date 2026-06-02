from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas import books_schemas
from app.services import books_service
from app.db.base import get_db

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=books_schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def add_book(book: books_schemas.BookCreate):
    with get_db() as db:
        return books_service.create_book(db=db, book=book)


@router.get("/", response_model=List[books_schemas.BookResponse])
def get_books():
    with get_db() as db:
        return books_service.get_all_books(db)


@router.get("/search", response_model=List[books_schemas.BookResponse])
def search_books(author: str):
    with get_db() as db:
        return books_service.search_by_author(db, author_name=author)


@router.get("/{book_id}", response_model=books_schemas.BookResponse)
def get_book(book_id: int):
    with get_db() as db:
        db_book = books_service.get_book_by_id(db, book_id=book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail="Kitob topilmadi!")
        return db_book


@router.put("/{book_id}", response_model=books_schemas.BookResponse)
def edit_book(book_id: int, book_update: books_schemas.BookCreate):
    with get_db() as db:
        db_book = books_service.get_book_by_id(db, book_id=book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail="Tahrirlash uchun kitob topilmadi!")
        return books_service.update_book(db, db_book=db_book, book_update=book_update)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_book(book_id: int):
    with get_db() as db:
        db_book = books_service.get_book_by_id(db, book_id=book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail="O'chirish uchun kitob topilmadi!")
        books_service.delete_book(db, db_book=db_book)
        return None