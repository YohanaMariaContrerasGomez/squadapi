from pydantic import Field
from pydantic import BaseModel

class JokeBase(BaseModel):
    texto: str = Field(
        ...,
        min_length=3,
        example= "The other day, my wife asked me to pass her lipstick but I accidentally passed her a glue stick. She still isn't talking to me."
    )

class Joke(JokeBase):
    id: int = Field(
        ...,
        Example="5"
    )
