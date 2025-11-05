# it convert non json compatible python objects into json-serilizable format.

from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    name : str
    age : int

@app.post("/convert/")
async def convert_user(data:User):
    user = User(name=data.name,age = data.age)
    json_data = jsonable_encoder(user)
    return {"encoded_data":json_data}

    

@app.get("/time/")
def get_time():
    data = {"time" : datetime.now()}
    # encoded_data = jsonable_encoder(data)
    return data    


