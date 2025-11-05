
from jose import JWTError,JWTError,jwt
from datetime import datetime,timedelta
from typing import Union,List,Annotated,Literal,Dict,Optional

from fastapi import FastAPI,Query,Form,UploadFile,File,Depends,HTTPException,status,Depends,HTTPException,Request
from fastapi.security import HTTPBasic,HTTPBasicCredentials,OAuth2PasswordBearer,OAuth2PasswordRequestForm
import secrets
from enum import Enum
import json
import os
from pydantic import BaseModel

from fastapi import FastAPI, status, HTTPException,Response,status
from fastapi.security import APIKeyHeader
from jose import JWTError, jwt
from pydantic import BaseModel
import secrets
from datetime import datetime, timedelta
import random,logging,bcrypt

app = FastAPI()
user_data_base = {}
otp_store = {}


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



SECRET_KEY = "my_TOKEN_akash_deshmukh_7566029853_from_nagpur_pin_code_123_akash@gmail.com"

ALGORITHM = "HS256"

api_key_header = APIKeyHeader(name="token",auto_error=True)

# class Token(BaseModel):
#     access_token: str
#     token_type: str


class createuser(BaseModel):
    mobile :str
    username:str
    password:str


class userlogin(BaseModel):
    mobile : str
    password: str


class Mobilelogin(BaseModel):
    mobile : str


class otpverify(BaseModel):
    mobile : str
    otp : int

class newpassword(BaseModel):
    mobile:str
    new_password : str

def send_massage(mobile:str,massage:str):
    logger.info(f"sending massae to {mobile} : {massage}")




def hash_password(password:str):
    return bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password:str,hashed_password:str):
    return bcrypt.hashpw(plain_password.encode('utf-8'),hashed_password.encode('utf-8'))


def create_access_token(data: dict):
    encode_data = data.copy()  
    expire = datetime.utcnow() + timedelta(minutes=59)
    encode_data.update({"exp": expire})
    encoded_jwt = jwt.encode(encode_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

@app.post("/create_user/")
def create_user(user:createuser):
    if user.mobile in user_data_base:
        raise HTTPException(status_code=400, detail="user already exist")
    

    hash_psw = hash_password(user.password)

    user_data_base[user.mobile]={
        "username" : user.username,
        "password" : hash_psw
    }

    send_massage(user.mobile,f"Hello {user.username}, your account create..")
    return {
        "massage" : "user created sussesfully"
    }


@app.post("/login/")
def login(user:userlogin):
    db_user = user_data_base.get(user.mobile)
    passwords = hash_password(user.password)
    if not db_user:
        raise HTTPException(status_code=400,detail="user not found")
    

    if not verify_password(user.password,db_user["password"]):
        raise HTTPException(status_code=401,detail="incorect password")
    if passwords != db_user["password"]:
        raise HTTPException(status_code=401,detail=["Incorrect password",db_user["password"],user.password])
    

    acces_token = create_access_token(data = user.mobile)
    return {
        "massage" : f"welcome back {db_user['username']} !",
        "access_token":acces_token,

    }


@app.post("/forget_password/")
def forgot_password(data:Mobilelogin):
    if data.mobile not in user_data_base:
        raise HTTPException(status_code=400,detail="user not found")

    otp = random.randint(1000,9999)
    expire_time = datetime.utcnow()+timedelta(minutes=4)


    otp_store[data.mobile] = {"otp":otp,"expire_at":expire_time}
    send_massage(data.mobile,f"your password resend is : {otp}")
    return {
        "massage" : "otp send to your mobile",
        "otp" : otp
    } 



@app.post("/verify_otp/")
def verify_otp(data:otpverify):
    saved_otp = otp_store.get(data.mobile)

    if not saved_otp:
        raise HTTPException(status_code=400,detail="otp not found")
    
    if datetime.utcnow()>saved_otp["expires_at"]:
        otp_store.pop(data.mobile,None)
        raise HTTPException(status_code =400,detail = "otp expired")
    
    if saved_otp["otp"] != data.otp:
        raise HTTPException(status_code=400, detail= " invalid otp")
    
    
    return {
        "massage" : "otp verify.."
    }

@app.post("/reset_password/")
def reset_password(data:newpassword):
    if data.mobile not in user_data_base:
        raise HTTPException(status_code=400,detail="user not present")
    
    user_data_base[data.mobile]["password"] = hash_password(data.new_password)
    otp_store.pop(data.mobile,None)
    return {
        "massage": "password reset..."
    }



@app.get("/user_data/")
def user_data():
    return {"data":user_data_base}

# @app.post("/create_user/")
# def create_user(user:createuser):
#     if user.mobile in user_data_base:
#         raise HTTPException(status_code=400, detail="user already exist")
    
#     user_data_base[user.mobile]={
#         "username" : user.username,
#         "password" : user.password
#     }
#     return {
#         "massage" : "user created sussesfully"
#     }

# @app.post("/login_user/")
# def login_user(user:userlogin):
#     user_mobile = user_data_base.get(user.mobile)
#     if not user_mobile:
#         raise HTTPException(status_code=400, detail="user not found")
    
#     if user_mobile["password"] != user.password:
#         new_password = secrets.token_hex(4)
#         user_data_base[user.mobile]["password"] = new_password
#         send_massage(user.mobile, f"you password wass incorect , yur new password is : {new_password}")
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail = "incorect password. new password send to you mobile"
#         )
#     return {
#         "massage": f"wellcome back {user_data_base['username']}"
#     }



# @app.post("/create_user/")
# def create_user(user:createuser):
#     if user.mobile in user_data_base:
#         raise HTTPException(status_code=400,detail="user present")
#     user_data_base[user.mobile] = {
#         "username" : user.username,
#         "password" : user.password
#     }
#     send_massage(user.mobile,f"hello {user.username}, your account created..")
#     return {
#         "massage":"user created"
#     }


































def create_access_token(data: dict):
    to_encode = data.copy()  
    expire = datetime.utcnow() + timedelta(minutes=59)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

class fill_Data(BaseModel):
    name : str
    age  : int
    technology : str
    department : str
    

@app.post("/get_token/")
async def get_token(data:fill_Data,response:Response):

    data = {
        "name":data.name,
        "age" : data.age,
        "technology" : data.technology,
        "department" : data.department
    }

    token = create_access_token(data)

    return {
        "message":"Token store in cookie",
        'token': token
        }

@app.post("/verify_token/")
async def verify_token(token: str):
    try:
        MY_decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return MY_decode_jwt
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Bro caredential not match")
    
def data_chack(token:str = Depends(api_key_header)):
    try:
        MY_decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if MY_decode_jwt["age"] <18:
            return f"oops\nsorry you not valid for vote"
        else:

            return "thanks for voter id application",MY_decode_jwt    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Bro caredential not match")
    



@app.post("/vote_api_data/")
async def user_data(token: str = Depends(data_chack)):
    return {
        "detail": True,
        "data":token
        }







