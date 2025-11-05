#request body - when you send data from client(browser) to api, you send it as a request body
# request body - a data send by client to api.
# responce body - data send by api to client.


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    product_name : str
    price : float
    tax : float | None = None


@app.post("/items/")
async def GST_data(data:Item,name:str):
    item_dict = dict(data)

    if data.tax != 0:
        price_with_GST = data.price + data.price*data.tax/100
        item_dict.update({"price with GST " : price_with_GST})
        return item_dict
    return item_dict


# @app.post("/items/")
# async def create_item(item:Item):
#     item_dict = item.dict()
#     if item.tax is not None:
#         price_with_tax = item.price + item.price * item.tax/100
#         item_dict.update({"price with tax" : price_with_tax})
#         print(item_dict)

#     return  item_dict


