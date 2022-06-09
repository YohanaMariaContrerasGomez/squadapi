from fastapi import HTTPException, status

from app.v1.model.joke_model import Joke as JokeModel
from app.v1.schema import joke_schema

import requests
import random

dad_url = "https://icanhazdadjoke.com/slack"
chuck_url = "https://api.chucknorris.io/jokes/random"

def randon_joke():
    names = ['chuck', 'dad']
    name = random.choice(names)
    return name


def get_joke(name: str = None):

    if (name is None):
        name = randon_joke()

    url = select_joke(name)
    r = joke_response(url)

    return joke_schema.JokeBase(
        texto = r
    )


def select_joke(name):
    if name.lower() == "chuck":
        url = chuck_url
    elif name.lower() == "dad":
        url = dad_url
    else:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Word not found"
        ) 

    return url 



def joke_response(url):
    r = requests.get(url)
    r = r.json()

    if url == dad_url:
        r = r["attachments"][0]["text"]
    elif url == chuck_url:
        r =  r["value"]
    else:
        r = url

    return r



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