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


def update_joke(joke_id:int, texto: str):
    joke = JokeModel.filter((JokeModel.id == joke_id)).first()

    if not joke:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Joke not found"
        )
    
    joke.texto = texto
    joke.save()
    
    return joke_schema.Joke(
        id = joke.id,
        texto = joke.texto
    )

def delete_joke(joke_id:int):
    joke = JokeModel.filter((JokeModel.id == joke_id)).first()

    if not joke:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Joke not found"
        )
    
    joke.delete_instance()