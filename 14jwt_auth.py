

from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException,Response, FastAPI,Depends
from fastapi.security import APIKeyHeader
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime,timedelta


app = FastAPI()


SECRET_KEY = "my_TOKEN_akash_deshmukh_7566029853_from_nagpur_pin_code_123_akash@gmail.com"

ALGORITHM = "HS256"

api_key_header = APIKeyHeader(name="token",auto_error=True)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=59)
    to_encode.update({"exp" : expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt


class Data_schema(BaseModel):
    name : str
    age  : int
    technology : str
    department : str

@app.post("/get_token/")
async def get_token(data:Data_schema,response:Response):
    data = {
        "name" : data.name,
        "age"  : data.age,
        "technology" : data.technology,
        "department" : data.department
    } 

    token = create_access_token(data)

    return {
        'token': token
        }


@app.post("/verify_token/")
async def verify_token(token : str):
    try :
        MY_decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return MY_decode_jwt
    except JWTError:
        return {"massage" : "data not found"}
    



# @app.post("/verify_token/")
# async def verify_token(token: str):
#     try:
#         MY_decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return MY_decode_jwt
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Bro caredential not match")
    


def data_chack(token:str = Depends(api_key_header)):
    try:
        My_decode_jwt = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        if My_decode_jwt["age"] < 18:
            return f"oops\n sorry you not valid for vote"
        else:
            return "thanks for voter id application",My_decode_jwt
    except JWTError:
        return {
            "massage" : "soory data not found."
        }    


@app.post("/vote_api_data/")
async def user_data(token: str = Depends(data_chack)):
    return {
        "data":token
        }




