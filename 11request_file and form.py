# handling both form data and file upload together in fastapi

from fastapi import FastAPI, Form,File,UploadFile,status
from pydantic import BaseModel


app = FastAPI()

@app.post("/submit/",tags=["user"],status_code=status.HTTP_201_CREATED)
async def submit_form(
    user_name : str = Form(...),
    description : str = Form(None),
    file : UploadFile = File(...)
):
    
    return {
        "user name" : user_name,
        "description" : description,
        "content_type" : file.filename,
        "content_type" : file.content_type
    }



class Item(BaseModel):
    name:str
    description : str | None = None
    price : float
    tax : float | None = None
    tags : set[str] = set()


@app.post("/items/",response_model = Item,summary = "Create an item")
async def create_item(item : Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """    
    return item


@app.post("/item/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item