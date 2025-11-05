# clas use as a dependency by declaring with depends()

from fastapi import FastAPI,Depends

app = FastAPI()

class user:
    def __init__(self,username:str="",age:int = 0):
        self.username = username
        self.age = age

@app.get("/items/") 
def list_items(User_data:user = Depends()):
    return {
            "name" : User_data.username,
            "age"  : User_data.age
            }       
