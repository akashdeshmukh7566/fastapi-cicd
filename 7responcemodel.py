#its way to control what the  api return to user validate and filter the output data , automatically generate document.


from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    tags: list[str]=[]

@app.post("/items/",response_model = Item)
async def create_items(item : Item) -> Any:
    return item

@app.get("/items/",response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name" : "portal gun", "price":42.0},
        {"name" : "plumbus" , "price" : 32.3},
    ]     



