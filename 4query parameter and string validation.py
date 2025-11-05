#fastapi allow you additional information and validation on parameters.


from fastapi import FastAPI,Query,Path,Body,Depends
from typing import Annotated,Literal,Optional
from pydantic import BaseModel,Field

app = FastAPI()

@app.get("/items/")
async def read_items(query:str | None = None):
    results = {
        "items" : [{"item_id" : "1"}, {"item_id" : "wine"}]
    }

    if query:
        results["items"].append({"query" : query})
    return results
    



@app.get("/items_with_annotation/")
async def read_item(query : Annotated[str | None, Query(max_length=50)]= None):
    results = {"items" : [{"product" : "mobile"}, {"item_id" : 420}]}
    if query:
        results["items"].append({"query" : query})

    return results    






#field(str,int) validation - 

class products(BaseModel):
    name_product : str = Field(min_length=5, max_length=50,example="camera")
    price : float = Field(gt= 0,example=5700.90)
    quentity : int = Field(ge=0, le=100)

        
@app.post("/data_validation/")
async def my_data(product_data:products):
    return {
        "product" : product_data.name_product,
        "price"   : product_data.price,
        "quentity": product_data.quentity
    }

 
# app = FastAPI()
#optional fields & default validation - 

@app.get("/items_data/")
async def read_items(query : Annotated[list[str]|None,Query()]=None):
    query_items = {"query" : query}
    return query_items


#query parameters with pydantic model

#nested model
class Address(BaseModel):
    street : str
    city : str
    zip_code : int

class Item(BaseModel):
    name : str
    price : float
    address : Address


@app.post("/my_data/")
async def creat_item(item:Item):
    return item


# query parameter with pydantic model
class FilterParams(BaseModel):
    limit : int
    offset : int 
    order_by : Literal["created_at", "updated_at"] = "created_at"
    tags : list[str] = []


@app.get("/new_items/")
async def read_items(filter_query: Annotated[FilterParams,Query()]):
    return filter_query


    
class ItemQueryParames(BaseModel):
    name : Optional[str] = None
    price_min : Optional[float] = None
    price_max : Optional[float] = None
    in_stak : float



@app.get("/Queryparams/")
def read_items(params:ItemQueryParames =Depends()):
    return {
        "filter " : params
    }



