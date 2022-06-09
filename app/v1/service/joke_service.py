from fastapi import HTTPException, status

from app.v1.model.joke_model import Joke as JokeModel
from app.v1.schema import joke_schema

def create_joke(joke: joke_schema.JokeBase):
    
    db_joke = JokeModel(
        texto = joke.texto
    )

    db_joke.save()

    return joke_schema.Joke(
        id = db_joke.id,
        texto = db_joke.texto
    )