from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session


DATABASE_URL = "sqlite:///./library.db"
engine = create_engine(DATABASE_URL)


Base = declarative_base()


def get_db():
    return Session(bind=engine)