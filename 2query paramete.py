# Query parameter - use to provide optional information for filtering and sorting , define in function parameter


from pydantic import BaseModel
from fastapi import FastAPI
from enum import Enum


app = FastAPI()



class data(str,Enum):
    active = "active",
    deactive = "deactive"

@app.get("/items/")
async def get_user(status:data,user:str):
        return {
            "user name" : user,
            "status"  : f"you are {status} user."
        }
    
    



