# path parameters - a value that is part of the url use to identify a specific resource
from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {
        "item_id" : item_id
    }


class user_Data(BaseModel):
    name : str
    full_name : str
    Class : int
    email : str
    mob_num:int



@app.post("/user/")
async def fill_data(data:user_Data):
    return {
        "name" : data.name,
        "full_name" : data.full_name,
        "class"  : data.Class,
        'email' : data.email,
        'mob_num' : data.mob_num
    }


from enum import Enum


class ModelName(str, Enum):
    roy = "roy",
    sahil = "sahil",
    komal = "komal"


    
@app.get("/models/{ModelName}")
async def get_model(model_name:ModelName):
    if model_name.name == "roy":
        return {
            "model name" : model_name,
            "massage" : "good is great"
        }    
    elif model_name.name == "sahil":
        return {
            "model name" : model_name,
            "massage" : "hello sahil"
        }
    else:
        return{
            "model name" : model_name,
            "massage" : "hello miss komal"
        }
    
    
