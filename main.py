from fastapi import FastAPI

from app.v1.router.joke_router import router as joke_router

app = FastAPI()


app.include_router(joke_router)