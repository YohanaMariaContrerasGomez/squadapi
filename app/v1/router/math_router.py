from turtle import st
from fastapi import APIRouter, Path
from fastapi import status
from typing import List

from app.v1.service import math_service

router = APIRouter(prefix="/api/v1",  tags=["numbers"])

@router.get(
    "/number/{number}",
    status_code=status.HTTP_200_OK,
    summary="Get Plus one"
)
def get_plus_one(
    number: int = Path(
         ...,
         gt=0
     )):
    """
    ## Get Plus one

    ### Args
    The app can recive next fields into a JSON
    - number:  Given number

    ### Returns
    - Given number plus one
    """
    return {
        'msg': number + 1
    }


@router.get(
    "/numbers/{numbers}",
    status_code=status.HTTP_200_OK,
    summary="Get LCM from an integer list of numbers"
)
def get_plus_one(
    numbers: str = Path(
         ...
     )):

    return math_service.CalculateLCM(numbers)