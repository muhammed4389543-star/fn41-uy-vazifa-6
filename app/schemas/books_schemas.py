from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int
    pages: int


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    published_year: int
    pages: int