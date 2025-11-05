#fastapi allow you additional information and validation on parameters.


from fastapi import FastAPI,Query,Path,Body,Depends
from typing import Annotated,Literal,Optional
from pydantic import BaseModel,Field
from enum import Enum
app = FastAPI()

class choose(Enum):
    good = "good"
    average="average"
    bad = "bad"

@app.post("/items/")
async def read_items(item_id:str,item:str,review:choose,suggetion:str):
    results = {
        "item_data" : [{"item_id" : item_id}, {"item" : item}]
    }

    print(review)
    if review == choose.good :
        results["item_data"].append("thank sir for your feedback.We are try to work on your valubal sugetion.")
        return results
    elif review == choose.average:
        results["item_data"].append("soory sir! for our average servise.our team work on your suggesion for improve our servise quality")
        return results
    elif review == choose.bad:
        results["item_data"].append(f"sorry sir, we are appologise on our bad servise. we are immediatly work on your suggetion.")
        return results
    

# @app.get("/items/")
# async def read_items(query:str | None = None):
#     results = {
#         "items" : [{"item_id" : "1"}, {"item_id" : "wine"}]
#     }

#     if query:
#         results["items"].append({"query" : query})
#     return results
    
class data(BaseModel):
    product : Annotated[str | None, Query(max_length=50)]=None
    item_id : Annotated[int | None, Query(max_digits=10000)]=None
    review : Annotated[str | None, Query(max_length=50)]=None


@app.get("/items_with_annotation1/")
async def read_item1(id:int,DATA:data):
    results = {"items" : [{"item_id" : 420,"product" : DATA.product}]}
    if DATA.review:
        results["items"].append({"review" : DATA.review})
    return results


@app.get("/items_with_annotation/")
async def read_item(query : Annotated[str | None, Query(max_length=50)]= None,item_id : Annotated[int | None, Query(max_digits=10000)]=None,review : Annotated[str | None, Query(max_length=50)]=None
):
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



