from typing import Optional
from fastapi import APIRouter, Path, Query
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import joke_schema
from app.v1.service import joke_service

from app.v1.utils.db import get_db

router = APIRouter(prefix="/api/v1/joke",  tags=["jokes"])

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=joke_schema.JokeBase,
    summary="Get a Joke"
)
def get_joke(
    name: Optional[str] = Query(None)
    ):
    """
    ## Get a Joke

    ### Args
    The app can recive next fields into a JSON
    - name:  value type ['chuck', 'dad']

    ### Returns
    - joke: JokeBase info
    """
    return joke_service.get_joke(name)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=joke_schema.Joke,
    dependencies=[Depends(get_db)],
    summary="create a new joke"
)
def create_joke(joke: joke_schema.JokeBase = Body(...)):
    """
    ## Create a new joke in the app

    ### Args
    The app can recive the next fields into a JSON
    - texto: content

    ### Returns
    - joke: Joke info
    """
    return joke_service.create_joke(joke)

@router.put(
    "/{joke_id}",
    status_code=status.HTTP_200_OK,
    response_model=joke_schema.Joke,
    dependencies=[Depends(get_db)],
    summary="update a joke"
)
def update_joke(
     joke_id: int = Path(
         ...,
         gt=0
     ),
     joke: joke_schema.JokeBase = Body(...)
    ):
    """
    ## update a joke in the app

    ### Args
    The app can recive next fields into a JSON
    - texto: content

    ### Returns
    - joke: Joke info
    """
    return joke_service.update_joke(joke_id,joke.texto)


@router.delete(
    "/{joke_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="delete a joke"
)
def delete_joke(
     joke_id: int = Path(
         ...,
         gt=0
     )
    ):
    """
    ## delete a joke in the app

    ### Args
    The app can recive next fields into a JSON
    - id: Joke Id
    """
    joke_service.delete_joke(joke_id)

    return {
        'msg': 'Joke has been deleted successfully'
    }