from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import joke_schema
from app.v1.service import joke_service

from app.v1.utils.db import get_db

router = APIRouter(prefix="/api/v1")

@router.post(
    "/joke/",
    tags=["jokes"],
    status_code=status.HTTP_201_CREATED,
    response_model=joke_schema.Joke,
    dependencies=[Depends(get_db)],
    summary="create a new joke"
)
def create_joke(joke: joke_schema.JokeBase = Body(...)):
    """
    ## Create a new joke in the app

    ### Args
    The app can recive next fields into a JSON
    - texto: 

    ### Returns
    - joke: Joke info
    """
    return joke_service.create_joke(joke)