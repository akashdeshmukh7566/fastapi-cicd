from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class FormData(BaseModel):
    username : str
    password : str
    

@app.post("/login/")
async def login(data:Annotated[FormData,Form()]):
    return {"massage" : data}


class option(str,Enum):
    option1 = "active"
    option2 = "deactive"

class FormData(BaseModel):
    username : str
    password : str
    choice : option

    model_config = {"extra" : "forbid"}    

@app.post("/login_new/")
async def login(
    username : Annotated[str,Form(...)],
    password : Annotated[str,Form(...)],
    choice   : Annotated[str,Form(...)]
):
    data = FormData(usernames=username,passwords=password,choices=choice) 
    return data
   