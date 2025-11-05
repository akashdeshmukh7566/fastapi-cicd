# path parameters - a value that is part of the url use to identify a specific resource


from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {
        "item_id" : item_id
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
    
    
