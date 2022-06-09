from app.v1.model.joke_model import Joke

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([Joke])