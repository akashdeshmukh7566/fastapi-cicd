from jose import JWTError,jwt
from datetime import datetime,timedelta
from typing import Annotated

from fastapi import FastAPI,Depends,HTTPException,status,Body
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm,APIKeyHeader

from pydantic import BaseModel
from passlib.context import CryptContext



app = FastAPI()

SECRET_KEY = "my_TOKEN_akash_deshmukh_7566029853_from_nagpur_pin_code_123_akash@gmail.com"

ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")



user_database = {
    "akash": {
        "username" : "akash",
        "fullname" : "akash deshmukh",
        "email"    : "akash123@gmail.com",
        "disable": False,
        "hashed_password": pwd_context.hash("123")

    },
    "ramu": {
        "username" : "ramu",
        "fullname" : "ramu deshmukh",
        "email"    : "ramu123@gmail.com",
        "disable": False,
        "hashed_password": pwd_context.hash("1234")
    }
}



class Token(BaseModel):
    access_token: str
    token_type  : str

class tokenData(BaseModel):
    username : str|None


class user(BaseModel):
    username:str
    fullname:str
    email:str
    disable:bool

class UserInDb(user):
    hashed_password:str


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)



def get_user(db,username:str):
    if username in db:
        user_dict = db[username]
        return UserInDb(**user_dict) 
    
    return None       #not currect
    
def authenticat_user(db,username:str,password:str):
    user = get_user(db,username)
    if not user:
        return False
    
    if not verify_password(password,user.hashed_password):
        return False
    return user



def create_access_token(data: dict):
    to_encode = data.copy()  
    expire = datetime.utcnow() + timedelta(minutes=59)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def get_current_user(token:Annotated[str,Depends(outh2_scheme)]):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail = "Could not valid credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )
    try:
        paylod =jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=paylod.get("sub")
        if username is None:
            raise credential_exception
        token_data = tokenData(username=username)
    except JWTError:
        raise credential_exception
    user = get_user(user_database,token_data.username)
    if user is None:
        raise credential_exception
    return user


def get_curent_active_user(curent_user : Annotated[user,Depends(get_current_user)]):
    if curent_user.disable:
        raise HTTPException(status_code=400,detail="Inactive") 
    return curent_user




@app.post("/token/",response_model=Token)
def loggin_for_accesstoken(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    user = authenticat_user(user_database,form_data.username,form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorect user or password",
            headers={"WWW-Authenticate":"Bearer"},
        )   

    access_token = create_access_token(data={"sub":user.username})
    return {"access_token":access_token,"token_type":"bearer"}




@app.get("/users/me",response_model=user)
def read_user_me(current_user:Annotated[user,Depends(get_curent_active_user)]):
    return current_user



@app.get("/users/me/items")
def read_own_items(current_user:Annotated[user,Depends(get_curent_active_user)]):
    return [{"item_id" : "xyz","owner":current_user.username}]




@app.post("/create_user/")
def create_user(user_data:Annotated[UserInDb,Body(...)]):

    if user_data.username in user_database:
        raise HTTPException(status_code=400,detail="user already exist")
    
    
    hash_password= pwd_context.hash(user_data.hashed_password)
    user_data.hashed_password = hash_password
    
    user_database[user_data.username] = user_data.dict()
    return {
        "masagge":f"user {user_data.username} created"
    }


@app.get("/all_user/")
def all_user():
    return {
        "user data" : user_database
    }

