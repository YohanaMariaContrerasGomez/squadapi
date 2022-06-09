import peewee

from app.v1.utils.db import db

class Joke(peewee.Model):
    texto = peewee.CharField()

    class Meta:
        database = db