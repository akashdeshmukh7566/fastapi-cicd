

from sqlalchemy import Table,Column,String,MetaData,Select,create_engine,Integer,insert,Update,Delete,func,JSON,Boolean
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from fastapi import FastAPI,Depends
from pydantic import BaseModel
from enum import Enum
import requests
import random
from twilio.rest import Client
from pwdlib import PasswordHash

# from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm,APIKeyHeader
from jose import JWTError,jwt
from datetime import datetime,timedelta
import os


app = FastAPI()



# database_url = "postgresql+psycopg2://postgres:newpassword@localhost:5432/mydatabase"
# database_url = "postgresql+psycopg2://postgres:newpassword@my_postgres:5432/mydatabase"
# database_url = "postgresql+psycopg2://postgres:newpassword@localhost:5433/mydatabase"
# database_url = "postgresql+psycopg2://postgres:newpassword@my_postgres:5432/mydatabase"
# database_url = "postgresql+psycopg2://postgres:newpassword@host.docker.internal:5433/mydatabase"
# database_url = "postgresql+psycopg2://postgres:newpassword@host.docker.internal:5433/mydatabase"
import os
from sqlalchemy import create_engine

db_url = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:newpassword@db:5432/mydatabase")
engine = create_engine(db_url)

# engine = create_engine(database_url)

Base = declarative_base()
password_hash = PasswordHash.recommended()

ACCOUNT_SID = "ACafe9fafb439e0483059e5b8770118afd"
AUTH_TOKEN = "91ad22baffdad2a006cbadf3c4bf21fe"
TWILIO_PHONE_NUMBER = "+15077131149"

SECRET_KEY = "MY_NAME_IS_AKASH_7566029853_hello_hy_BY_BY"
ACCESS_TOKEN_EXPIRE_MIN = 5900
ALGORITHM = "HS256"


class User_info(Base):
    __tablename__ = "users_info"
    user_name = Column(String)
    password = Column(String)
    email = Column(String,primary_key=True)
    mobile = Column(String)

class User_history(Base):
     __tablename__ = "user_history"
     id = Column(Integer,primary_key=True, autoincrement=True)
     email = Column(String,ForeignKey("users_info.email"))    
     pro_servise = Column(Boolean)
     history = Column(JSON)


Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def verify_password(plain_password, hashed_password):
     return password_hash.verify(plain_password,hashed_password)


def get_password_hash(password):
     return password_hash.hash(password)


def create_access_token(data:dict):
     to_encode = data.copy()
     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN)
     to_encode.update({"exp" : expire})
     return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)



# def decode_access_token(token:str):
#      try:
#           return jwt.decode(token,) 


class user_create(BaseModel):
    name : str
    email : str
    password : str
    mobile:str

data_user = {}

@app.post("/sms_send/")
async def sms_send(data: user_create):
    global data_user
    
    try:
        verification_code = random.randint(1000,9999)

        client = Client(ACCOUNT_SID,AUTH_TOKEN)
        message = client.messages.create(
            body = f"hello {data.name}, Your verification code is {verification_code}",
            from_=TWILIO_PHONE_NUMBER,
            to=data.mobile
        )

        data_user = {
            "name" : data.name,
            "email" : data.email,
            "password":data.password,
            "mobile" : data.mobile,
            "code" : verification_code
        }

        return {
            "status" : "success",
            "massage" : "verification code genrate",
            "info" : data_user
        }
        
    except Exception as e:
        return {"status" : "failed", "error":str(e)}
    

@app.post("/verification/")
async def verify(code:int):
        user = data_user
        print("\n"*7, "asdsacddf@@@@@", "\n"*7)
        print("\n"*10,"@@@@@@@@@@","\n"*10)
        user_email = session.query(User_info.email).all()
        print(user_email) 
        print(user["email"])
        print("\n"*7, "asdsacddf@@@@@", "\n"*7,user["email"])
        for i in user_email:
            if i[0] == user["email"]:
                print("user not present")
                return {"massage user present"}
  
  

        if code != user["code"]:
             return {"message verification code not currect plz try again"}
        
        
        
        else:
            hashpassword = get_password_hash(user["password"])
            user["password"] = hashpassword
            user_name = user["name"]

            client = Client(ACCOUNT_SID,AUTH_TOKEN)

            message = client.messages.create(
                body = f"Account creation done. Thanks {user_name} for create your account on SKED AI.",
                from_=TWILIO_PHONE_NUMBER,
                to=user["mobile"]
            )
            


            new_user = User_info(user_name=user["name"],password=user["password"],email=user["email"],mobile=user["mobile"])

            print(new_user)
            session.add(new_user)
            session.commit()


            return {
                 "massae" : "user create",
                 "username" : user["name"],
                 "password" : user["password"],
                 "email"    : user["email"],
                 "mobile"   : user["mobile"]
            }

             


@app.post("/loggin/")
async def loggin_user(user_email:str,password:str):
    print("\n"*6,"heloo","\n"*6)
    user = session.query(User_info).filter_by(email=user_email).first()

 
    if not user:
         return {
              "massage" : "wrong email"
         }
    
    
    else:
        print(password,user.password)
        verify_pass = verify_password(password, user.password)
        print(verify_pass)
        if  verify_pass:
            return {"massage" : "user are valid"}




        else:
            return{
                    "sorry password wrong"
                }
    
    



     
     




