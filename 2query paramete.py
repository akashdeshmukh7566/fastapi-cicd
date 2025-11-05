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
    
    

class perent_data(BaseModel):
    street : str
    city   : str
    zip_code:int

class child_data(BaseModel):   
    full_name :str
    mob_num   : int
    Class     : str
    email     : str
    address   : perent_data


@app.post("/student_data/")
async def stu_data(my_data:child_data):
     return {
          "full name" : my_data.full_name,
          "mob number": my_data.mob_num,
          "Class"     : my_data.full_name,
          "email"     : my_data.email,
          "address"   : my_data.address,
          "street"    : my_data.address.city[1]
     }



