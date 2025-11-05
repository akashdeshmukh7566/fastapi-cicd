from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel,Field


class product(BaseModel):
    name : str = Field(min_length=3, max_length=100)
    price : str = Field(gt = 0)
    quentity : int = Field(ge = 0, le = 1000)

    




class ModelName(str,Enum):
    akash = "akash",
    sahil = "sahil",
    joy  = "joy"


app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name.value == "akash":
        return {
            "model name" : model_name,
            "massage" : "jay shree ram"
        }
    elif model_name.value == "sahil":
        return {
            "model name" : model_name,
            "massage" : "allah is great"
        }

    else:
        return {
            "model name" : model_name,
            "massages" : "good id great"
        }

    
    
