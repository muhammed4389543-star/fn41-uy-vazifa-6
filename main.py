import uvicorn
from fastapi import FastAPI
from app.db.base import engine, Base
from app.apis import books_api


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(books_api.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    