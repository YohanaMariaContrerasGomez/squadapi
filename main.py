from fastapi import FastAPI

from app.v1.router.joke_router import router as joke_router
from app.v1.router.math_router import router as math_router

app = FastAPI()


app.include_router(joke_router)
app.include_router(math_router)