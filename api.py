
from typing import Annotated
from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

# from main import get_curent_active_user, my_user
from schema import Token

router = APIRouter(prefix="/api", tags=["Api"])

@router.get("/users/me/items")
def read_own_items():
    return "done"


# @router.get("/users/me",response_model=my_user)
# def read_user_me(current_user:Annotated[my_user,Depends(get_curent_active_user)]):
#     return current_user



# @router.get("/users/me/items")
# def read_own_items(current_user:Annotated[my_user,Depends(get_curent_active_user)]):
#     return [{"item_id" : "xyz","owner":current_user.username}]

