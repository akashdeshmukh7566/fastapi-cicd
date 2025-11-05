#cookie - small piece of data store in your browser by a website.
#it sent automaticlly with every request to the same website.



from typing import Annotated

from fastapi import Cookie, FastAPI,Response,Depends,Header

app = FastAPI()


@app.get("/items/")
async def set_cookie(cookie,response:Response):
    response.set_cookie(key = "ads_id",value = cookie)
    print(response)
    return {"message" : f"Cookie set successfully!\n{cookie}"}


@app.get("/items_new/")
async def read_items(ads_id:Annotated[str,Cookie(), None] = None):
    return {"ads_id" : ads_id}

