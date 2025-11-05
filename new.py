from sqlalchemy import Table,Column,String,MetaData,Select,create_engine,Integer,insert,Update,Delete,func
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from fastapi import FastAPI,Depends
from pydantic import BaseModel,EmailStr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from enum import Enum
import requests
import random,smtplib
from twilio.rest import Client
from pwdlib import PasswordHash
import pandas as pd
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm,APIKeyHeader
from jose import JWTError,jwt
from datetime import datetime,timedelta


app = FastAPI()


SENDER_EMAIL = "akashdeshmukh7455@gmail.com"
SENDER_PASSWORD = "akash7566"




# def send_email(receiver_email:EmailStr,subject:str,message:str):
#     msg = MIMEMultipart()
#     msg["From"] = SENDER_EMAIL
#     msg["To"] = receiver_email
#     msg["Subject"] = subject
#     msg.attach(MIMEText(message,"plain"))
#     print(' '*4, receiver_email,SENDER_EMAIL,subject,' '*4)
#     try :
#         print(' '*4, receiver_email,SENDER_EMAIL,subject,' '*4)
   
#         with smtplib.SMTP("smtp.gmail.com",587) as server:
#             server.starttls()
#             server.login(SENDER_EMAIL,SENDER_PASSWORD)
#             server.send_message(msg)
#             print(' '*4, receiver_email,SENDER_EMAIL,subject,' '*4)
   

#     except Exception as e:
#         return f"function not work {e}"
    

print("hello")
def send_email(receiver_email: str, subject: str, message: str):
    msg = MIMEMultipart()
    msg["From"] = "dev@example.local"   # any from address (for dev)
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # send via local debugging SMTP server (no auth)
    with smtplib.SMTP("localhost", 1025) as server:
        server.send_message(msg)
    print(f"Email 'sent' to {receiver_email} (captured by local SMTP server)")


class user_create(BaseModel):
    name : str
    email : EmailStr
    password : str
    mobile:str
    subject : str
    message : str


data_user = {}

@app.post("/sms_send/")
async def sms_send(data: user_create):
    global data_user
    

    try:
        otp = random.randint(1000,9999)
        subject = data.subject
        message = data.message

        send_email(data.email,subject,message)

        return {
            "massage" : "massage send"
            }


        
    except Exception as e:
        return {"status" : "failed", "error":str(e)}
    


