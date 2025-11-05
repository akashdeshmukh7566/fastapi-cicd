from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type  : str

class tokenData(BaseModel):
    username : str|None


class user(BaseModel):
    username:str
    email:str
    full_name:str|None=None
    disable:bool|None=None

class UserInDb(user):
    hashed_password:str