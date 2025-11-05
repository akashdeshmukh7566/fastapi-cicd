from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime


app = FastAPI()

class User(BaseModel):
    username : str
    email : str
    age : int
    creat_at : datetime = datetime.now()

db = {}

@app.post("/users/")
def create_user(user:User):
    user_data = jsonable_encoder(user)
    user_id = len(db)+1
    db[user_id] = user_data
    return {"id" : user_id, "data" : user_data}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in db:
        raise HTTPException(status_code=404, detail = "user not preasent")
    
    return db[user_id]



@app.get("/users/")
def get_all_users():
    return db

@app.put("/users/{user_id}")
def update_user(user_id : int , update_user : User):
    if user_id not in db:
        raise HTTPException(status_code=404, detail = "user not present")
    store_user_data = db[user_id]
    update_user = update_user.model_dump(exclude_unset=True)
    store_user_data.update(update_user)
    db[user_id] = jsonable_encoder(store_user_data)

    return { 
            "message" : "user update",
            "data"    : db[user_id]
            }

@app.delete("/users/{user_id}")
def delete_user(user_id : int):
    if user_id not in db:
        raise HTTPException(status_code=4004, detail="user not present")
    del db[user_id]
    return {
        "message" : f"user {user_id} delete done"
    }

