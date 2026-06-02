from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()
    published_year: Mapped[int] = mapped_column()
    pages: Mapped[int] = mapped_column()