from fastapi import APIRouter, Path
from fastapi import status

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
         gt=0,
         example=66
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
        'number_plus_one': number + 1
    }


@router.get(
    "/numbers/{numbers}",
    status_code=status.HTTP_200_OK,
    summary="Get LCM from an integer list of numbers"
)
def get_plus_one(
    numbers: str = Path(
         ...,
         example="2,4,8,16,32,64,7"
     )):

    """
    ## Get LCM from an integer list of numbers

    ### Args
    The app can recive next fields into a JSON
    - numbers:  Given integer an positive numbers list

    ### Returns
    - Lcm for the given list
    """

    lcm = math_service.CalculateLCM(numbers)
    return {
        'least_common_multiple': lcm
    }