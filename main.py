
# app = FastAPI()

# SECRET_KEY = "my_TOKEN_akash_deshmukh_7566029853_from_nagpur_pin_code_123_akash@gmail.com"

# ALGORITHM = "HS256"

# api_key_header = APIKeyHeader(name="token",auto_error=True)



# # @app.put("/{name}")
# # def read_root(name:str):
# #     return {"Hello": name}


# # @app.get("/items/{item_id}")
# # def read_item(item_id: int,   q: Union[str, None] = None):
# #     return {"item_id": item_id, "q": q}


# # @app.put("/Rupees/{Rs}")
# # def update_chash(Rs: int,):
# #     x = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# #     rupe = {}

# #     for i in x:
# #         count = Rs // i
# #         if count > 0:
# #             rupe[i] = count
# #             Rs = Rs % i
# #         else:
# #             pass   

# #     return {"chash" : rupe }



# # @app.post("/items/")
# # async def create_item(item:Item):
# #     return item


# # @app.get("/users/{user_id}")    #path parameter
# # def get_user(user_id: int):
# #     return {"user_id": user_id}


# # @app.get("/items/")
# # def read_item(skip : int = 0, limit : int = 10):
# #     return {"skip":skip,"limit":limit}


# # @app.get("/items/{item_id}")
# # async def read_item(item_id: str, q: str | None = None, short: bool = False):
# #     item = {"item_id": item_id}
# #     if q:
# #         item.update({"q": q})
# #     if not short:
# #         item.update(
# #             {"description": "This is an amazing item that has a long description"}
# #         )
# #     return item

# # @app.get("/items/{item_id}")
# # async def read_item(item_id : str,q: str , short: bool=False):
# #     item = {"item_id":item_id}
# #     if q:
# #         item.update({"q":q})
# #     if not short:
# #         item.update(
# #             {"description":"this is an................"}
# #         )    
# #     return item 


# data_file = "users.json"
 

# # with open(data_file,"w") as f:
# #     json.dump({},f)


# # def read_user_data():
# #     with open(data_file,"r") as f:
# #         return json.load(f)           #json to dict

# # def write_user_data(data):
# #     with open(data_file,"w") as f:
# #         json.dump(data,f)            #dict to jsons




# # @app.post("/user_create/{user_id}")
# # def get_user(
# #     user_id : int, 
# #     name : str,
# #     Github :str, 
# #     Mobile : int,
# #     email : str, 
# #     Qualification : List[str] = Query(), 
# #     Skills : List[str] = Query(), 
# #     project : List[str] = Query()
# # ):
    
# #     users = read_user_data() 

# #     if user_id in users:
# #         return {"error : " : f"user {user_id} present.."}
    
# #     else:
# #         user_info = {
            
# #             "Name"          : name,
# #             "Github"        : Github,
# #             "Mobile"        : Mobile,
# #             "Email"         : email,
# #             "Qualification" : Qualification,
# #             "Skils"         : Skills,
# #             "Project"       : project

# #         }

# #         users[user_id] = user_info
# #         write_user_data(users)


# #         return {
# #             "message"   : f"user {name} create succesfull....",
# #             "user_id"   : user_id,
# #             "user_info" : user_info 
# #         }




# # @app.get("/user_resume")
# # def get_all_user():
# #     users= read_user_data()
# #     return {
# #         "total user"  : len(users),
# #         "users"  : users
# #     }
# # # print(get_all_user())

# # @app.get("/user/{user_id}")
# # def get_user(id):
# #     data = read_user_data()
# #     return {
# #         "user id"   : id,
# #         "user data" : data[id]
# #     }



# # data_dict = dict()

# # class info:
# #     name : str
# #     Github :str 
# #     Mobile : int
# #     email : str 
# #     Qualification : List[str] = Query()
# #     Skills : List[str] = Query()
# #     project : List[str] = Query()


# # @app.post("/data/")
# # def add_data(user_id:int,data:info):
# #     global data_dict
# #     my_key = []
# #     for key in data_dict.keys:
# #         my_key.append(key)

# #     if user_id in my_key:
# #         return {
# #             "massage" : f"user id : {user_id} present"
# #         }
# #     else:
# #         data_dict[user_id] = data
# #         return {
# #             "user_id" : user_id,
# #             "student_data" : data
# #         }
# # @app.get("/student_data/")
# # def all_data():
# #     global data_dict
# #     return {
# #         "all user data ":data_dict
# #         }


# # app = FastAPI()

# # data_dict: Dict[int, 'Info'] = {}

# # # Define the data model using Pydantic
# # class Info(BaseModel):
# #     name: str
# #     Github: str
# #     Mobile: int
# #     email: str
# #     Qualification: List[str] = Query(default=[])
# #     Skills: List[str] = Query(default=[])
# #     project: List[str] = Query(default=[])

# # @app.post("/data/")
# # def add_data(user_id: int, data: Info):
# #     if user_id in data_dict:
# #         return {
# #             "message": f"user_id: {user_id} already exists"
# #         }
# #     else:
# #         data_dict[user_id] = data
# #         return {
# #             "user_id": user_id,
# #             "student_data": data
# #         }

# # @app.get("/student_data/")
# # def all_data():
# #     return {
# #         "all_user_data": data_dict
# #     }







# # def create_stu(stu_id,data):
# #     for key in data_dict.keys():
# #         if stu_id == key:
# #             return "user present"
# #     else:
# #         data_dict[stu_id] = data


# # def get_all_data():
# #     data = []
# #     for key,value in data_dict.items():
# #         data.append([key,":",value])

        
# # def get_stu_data():
# #     data_dict


# stu_data = {}

# class UserData(BaseModel):
#     name: Optional[str] = None
#     age: Optional[str] = None
#     Class: Optional[str] = None
#     section: Optional[str] = None
#     subject: Optional[str] = None
#     grade: Optional[str] = None

# @app.post("/student/{id}")
# def create_student(id: int, data: UserData):
#     if id in stu_data:
#         return {
#             "message": f"Student ID {id} is already present."
#         }
    
#     stu_data[id] = data
#     return {
#         "message": f"User {data.name} created.",
#         "data": stu_data[id]
#     }

# @app.get("/stu_data/")
# def get_students():
#     return {
#         "message": f"Total {len(stu_data)} students present.",
#         "data": stu_data
#     }

# @app.delete("/student/{id}")
# def delete_student(id: int):
#     if id not in stu_data:
#         return {"message": "Student not present."}
#     del stu_data[id]
#     return {"message": f"Student ID {id} deleted."}



# @app.patch("/student/{id}")
# def update_student(id: int, data: UserData):
#     global stu_data
#     if id not in stu_data:
#         return {"message": f"Student ID {id} not present."}
    
#     temo_data = stu_data[id]
#     update = data.model_dump(exclude_unset=True)
#     for key,value in update.items():
#         setattr(temo_data,key,value)
#     return {
#         "message": f"Student ID {id} updated.",
#         "data": stu_data[id]
#     }



# class UserData(BaseModel):
#     name: Optional[str] = None
#     age: Optional[str] = None
#     Class: Optional[str] = None
#     section: Optional[str] = None
#     subject: Optional[str] = None
#     grade: Optional[str] = None

# @app.post("/student/")
# def create_student(data: Annotated[UserData,Query()], request: Request):
#     return {
#         "Clientip": request.client.host,
#         "clientport": request.client.port,
#         "Methods": request.method,
#         "Urls": str(request.url),
#         "Baseurl": str(request.base_url),
#         "header": dict(request.headers),
#         "queryparams": request.query_params,


#         "message": f"User {data.name} created.",
#         "Data_student": data
#     }

# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == "alexnet":
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


# @app.get("/items/")
# async def read_time(items_id:str="ex 1",a:str|None="ex als"):
#     return {
#         "massage" : items_id,
#         "massage1": a
#     }


# from pydantic import BaseModel
# from fastapi import FastAPI

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float

# @app.post("/items/")
# async def create_item(item: Item):
#     if item.name != str:
#         raise {
#             "massage" : "data not safr"
#         }
#     return item



# from typing import Annotated

# from fastapi import FastAPI, Path, Query

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(

#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str,
#     size: Annotated[float, Query(gt=0, lt=10.5)],
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if size:
#         results.update({"size": size})
#     return results

# from fastapi import FastAPI,Depends,Query,Body
# from pydantic import BaseModel,Field
# from typing import Optional

# app = FastAPI()

# class Image(BaseModel):
#     url : str
#     name  : str
# class Item(BaseModel):
#     name:str
#     price:float
#     image:Image|None=None

# @app.put("/items/{item_id}")
# async def update_item(item_id:int,item:Item):
#     results = {"item_id" : item_id , "item" : item} 

#     return results       


# from typing import Annotated

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name : str
#     price: str
#     tax  : float|None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id : int,
#     item : Annotated[
#         Item,
#         Body(
#             openapi_examples={
#                 "normal" : {
                    
#                     "summary":"a normal example",
#                     "description":"A **new description",
#                     "value" : {
#                         "name" : "foo",
#                         "price": 232.23,
#                         "tax" : 3.3,
                        
#                     },
#                 },

#                 "new_normal" :{
#                     "sumary" : "new sammary",
#                     "describ" : "new discrib",
#                     "value" : {
#                         "name" : "akash",
#                         "class" : "12th",
#                     },
#                 },
#             },
#         ),
#     ],
# ):


#     result = {"item_id":item_id,"item":item}
#     return result

# from typing import Annotated

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Annotated[
#         Item,
#         Body(
#             openapi_examples={
#                 "normal": {
#                     "summary": "A normal example",
#                     "description": "A **normal** item works correctly.",
#                     "value": {
#                         "name": "Foo",
#                         "description": "A very nice Item",
#                         "price": 35.4,
#                         "tax": 3.2,
#                     },
#                 },
#                 "converted": {
#                     "summary": "An example with converted data",
#                     "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
#                     "value": {
#                         "name": "Bar",
#                         "price": "35.4",
#                     },
#                 },
#                 "invalid": {
#                     "summary": "Invalid data is rejected with an error",
#                     "value": {
#                         "name": "Baz",
#                         "price": "thirty five point four",
#                     },
#                 },
#             },
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


# from datetime import datetime, time, timedelta
# from typing import Annotated
# from uuid import UUID

# from fastapi import Body, FastAPI

# app = FastAPI()


# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: int,
#     start_datetime: Annotated[datetime, Body()],
#     end_datetime: Annotated[datetime, Body()],
#     process_after: Annotated[timedelta, Body()],
#     repeat_at: Annotated[time | None, Body()] = None,
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "process_after": process_after,
#         "repeat_at": repeat_at,
#         "start_process": start_process,
#         "duration": duration,
#     }
# from fastapi import FastAPI, Cookie, HTTPException,Header
# from typing import Annotated
# app = FastAPI()

# @app.get("items/")
# async def read_item(
#     strange_header : Annotated[str|None,Header(convert_underscores=False)]=None,):
#     return {"user_agent":strange_header}


# from fastapi import FastAPI, Cookie
# from fastapi.responses import Response

# app = FastAPI()

# # Route to set a cookie
# @app.get("/set-cookie")
# def set_cookie(response: Response):
#     response.set_cookie(key="username", value="Alice")
#     return {"message": "Cookie has been set!"}

# # Route to read the cookie
# @app.get("/get-cookie")
# def get_cookie(username: str = Cookie(default=None)):
#     return {"cookie_username": username}




# from typing import Annotated

# from fastapi import Cookie, FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Cookies(BaseModel):
#     session_id: str
#     fatebook_tracker: str | None = None
#     googall_tracker: str | None = None


# @app.get("/items/")
# async def read_items(cookies: Annotated[Cookies, Cookie()]):
#     return cookies

# from typing import Annotated, Union

# from fastapi import Cookie, FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name : str
#     price: float
#     tax  : float|None=None
#     tag  : list[str]=[]

# @app.post("/items/")
# async def create_item(item:int):
#     return item

# @app.get("/items/")
# async def readtimes()->list[Item]:
#     return [
#         Item(name = "poal_gun",price=12.12),
#         Item(name="akash",price=12.12),
#     ]


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# # Extra model for address
# from fastapi import FastAPI, Form

# app = FastAPI()

# @app.post("/login")
# def login(username: str = Form(...), password: str = Form(...)):
#     return {"username": username, "password": password}



# from typing import Annotated

# from fastapi import FastAPI, Form
# from pydantic import BaseModel

# app = FastAPI()


# class FormData(BaseModel):
#     username: str
#     password: str


# @app.post("/login/")
# async def login(data: Annotated[FormData, Form()]):
#     return data

# from typing import Annotated

# from fastapi import FastAPI, Form
# from pydantic import BaseModel

# app = FastAPI()


# # class FormData(BaseModel):
# #     username: str
# #     password: str
# #     model_config : list=str["extra", "forbid"]


# # @app.post("/login/")
# # async def login(data: Annotated[FormData, Form(...)]):
# #     return data


# from typing import Annotated,Literal

# # from fastapi import FastAPI, Form
# # from pydantic import BaseModel

# # app = FastAPI()


# # class FormData(BaseModel):
# #     username: str
# #     password: str
# #     model_config : Literal["extra": "forbid"]="sd"


# # @app.post("/login/")
# # async def login(data: Annotated[FormData, Form()]):
# #     return data

# from fastapi import FastAPI, Form
# from pydantic import BaseModel, ConfigDict

# app = FastAPI()

# class FormData(BaseModel):
#     username: str
#     password: str
#     model_config = ConfigDict(extra="forbid")

# @app.post("/login/")
# async def login(
#     username: str = Form(...),
#     password: str = Form(...)
# ):
#     data = FormData(username=username, password=password)
#     return data


# from typing import Annotated
# from enum import Enum

# from fastapi import FastAPI, Form
# from pydantic import BaseModel

# # app = FastAPI()


# # class FormData(BaseModel):
# #     username: str
# #     password: str
# #     model_config : Enum["extra", "forbid"]


# # @app.post("/login/")
# # async def login(data: Annotated[FormData, Form()]):
# #     return data



# from enum import Enum
# from typing import Annotated

# from fastapi import FastAPI, Form
# from pydantic import BaseModel, ConfigDict

# app = FastAPI()

# # Step 1: Define a valid Enum
# class Options(str, Enum):
#     option1 = "option1"
#     option2 = "option2"

# # Step 2: Optional Pydantic model for validation (not used directly in route)
# class FormData(BaseModel):
#     username: str
#     password: str
#     choice: Options

#     model_config = ConfigDict(extra="forbid")  # Only in Pydantic v2

# # Step 3: Accept form inputs directly
# @app.post("/login/")
# async def login(
#     username: Annotated[str, Form(...)],
#     password: Annotated[str, Form(...)],
#     choice: Annotated[Options, Form(...)]
# ):
#     # Optionally validate with Pydantic model
#     data = FormData(username=username, password=password, choice=choice)
#     return data


# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     contents = await file.read()
#     return {
#         "filename": file.filename,
#         "content_type": contents
#     }





# from typing import List

# @app.post("/upload-multiple/")
# async def upload_multiple(files: List[UploadFile] = File(...)):
#     return [{"filename": f.filename} for f in files]




# from typing import Annotated

# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import HTMLResponse

# app = FastAPI()


# @app.post("/files/")
# async def create_files(files: Annotated[list[bytes], File()]):
#     return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfiles/")
# async def create_upload_files(files: list[UploadFile]):
#     return {"filenames": [file.filename for file in files]}


# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)



# from fastapi import FastAPI, Form, File, UploadFile

# app = FastAPI()

# @app.post("/submit/")
# async def submit_form(
#     username: str = Form(...),
#     description: str = Form(None),
#     file: UploadFile = File(...)
# ):
#     return {
#         "username": username,
#         "description": description,
#         "filename": file.filename,
#         "content_type": file.content_type
#     }


# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     if item_id != 1:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item_id": item_id}
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/users/")
# async def create_user(user: User):
#     return user


# from fastapi import FastAPI, Request,HTTPException
# from fastapi.responses import JSONResponse

# from pydantic import BaseModel
# from typing import Optional
# app = FastAPI()

# class MyCustomError(Exception):
#     def __init__(self, name: str):
#         self.name = name

# @app.exception_handler(MyCustomError)
# async def my_custom_error_handler(request: Request, exc: MyCustomError):
#     return JSONResponse(
#         status_code=418,
#         content={"error": f"Oops! {exc.name} did something wrong."}
#     )

# @app.get("/test/")
# async def test():
#     raise MyCustomError("CustomExceptionTest")


# from fastapi import FastAPI

# app = FastAPI()

# @app.get(
#     "/items/{item_id}",
#     summary="Get an item by ID",
#     description="This operation fetches an item using its unique ID.",
#     response_model=dict,
#     status_code=200,
#     tags=["Items"],
#     deprecated=False
# )
# async def get_item(item_id: int):
#     return {"item_id": item_id, "name": "Example Item"}



# # from pydantic import BaseModel
# # app = FastAPI()
# # class Item(BaseModel):
# #     id: int
# #     name: str

# # @app.get("/item/{item_id}")
# # async def read_item(item_id: int):
# #     return Item(id=item_id, name="Test Item")




# # # from fastapi import FastAPI, status
# # # from pydantic import BaseModel

# # # app = FastAPI()


# # # class Item(BaseModel):
# # #     name: str
# # #     description: str | None = None
# # #     price: float
# # #     tax: float | None = None
# # #     tags: set[str] = set()


# # # @app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
# # # async def create_item(item: Item):
# # #     return item



# from fastapi import FastAPI, Depends, HTTPException, Header

# def verify_token(x_token: str = Header(...)):
#     if x_token != "secret-token":
#         raise HTTPException(status_code=403, detail="Invalid token")

# # Add global dependency here
# app = FastAPI(dependencies=[Depends(verify_token)])

# @app.get("/public")
# def public_data():
#     return {"message": "This is public"}

# @app.get("/private")
# def private_data():
#     return {"message": "This is private"}



# from fastapi import Depends
# from sqlalchemy.orm import Session
# # from database import SessionLocal

# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()


# from datetime import datetime, timedelta

# print(data.copy())


# def create_access_token(data: dict):
#     to_encode = data.copy()  
#     expire = datetime.utcnow() + timedelta(minutes=59)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
#     return encoded_jwt

# class fill_Data(BaseModel):
#     name : str
#     age  : int
#     technology : str
#     department : str
    

# @app.post("/get_token/")
# async def get_token(data:fill_Data,response:Response):

#     data = {
#         "name":data.name,
#         "age" : data.age,
#         "technology" : data.technology,
#         "department" : data.department
#     }

#     token = create_access_token(data)

#     return {
#         # "message":"Token store in cookie",
#         'token': token
#         }

# @app.post("/verify_token/")
# async def verify_token(token: str):
#     try:
#         MY_decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return MY_decode_jwt
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Bro caredential not match")
    
# def data_chack(token:str = Depends(api_key_header)):
#     try:
#         MY_decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         if MY_decode_jwt["age"] <18:
#             return f"oops\nsorry you not valid for vote"
#         else:

#             return "thanks for voter id application",MY_decode_jwt    
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Bro caredential not match")
    



# @app.post("/vote_api_data/")
# async def user_data(token: str = Depends(data_chack)):
#     return {
#         "detail": True,
#         "data":token
#         }

# from fastapi import FastAPI
# from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
# outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# from api import router
# app = FastAPI()

# pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


# outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# app.include_router(router)


# user_database = {
#     "akash": {
#         "username" : "akash",
#         "fullname" : "akash deshmukh",
#         "email"    : "akash123@gmail.com",
#         "hashed_password": pwd_context.hash("123"),
#         "disabled": False,


#     },
#     "ramu": {
#         "username" : "ramu",
#         "fullname" : "ramu deshmukh",
#         "email"    : "ramu123@gmail.com",
#         "hashed_password": pwd_context.hash("1234"),
#         "disabled": True,


#     }
# }


# def verify_password(plain_password,hashed_password):
#     return pwd_context.verify(plain_password,hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def get_user(db,username:str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDb(**user_dict) 
    
#     return None       #not currect
    
# def authenticat_user(db,username:str,password:str):
#     user = get_user(db,username)
#     if not user:
#         return False
#     if not verify_password(password,user.hashed_password):
#         return False
#     return user

# def create_access_token(data: dict):
#     to_encode = data.copy()  
#     expire = datetime.utcnow() + timedelta(minutes=59)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)    
#     return encoded_jwt




# def get_current_user(token:Annotated[str,Depends(outh2_scheme)]):
#     credential_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail = "Could not valid credentials",
#         headers={"WWW-Authenticate":"Bearer"},
#     )
#     try:
#         paylod =jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
#         username:str=paylod.get("sub")
#         if username is None:
#             raise credential_exception
#         token_data = tokenData(username=username)
#     except JWTError:
#         raise credential_exception
#     user = get_user(user_database,token_data.username)
#     if user is None:
#         raise credential_exception
#     return user


# # def get_curent_active_user(curent_user : Annotated[user,Depends(get_current_user)]):
# #     if curent_user.disable:
# #         raise HTTPException(status_code=400,detail="Inactive") 
# #     return curent_user




# class my_user(BaseModel):
#     username : str
#     full_name: str|None
#     email    : str|None
#     hashed_password : str
#     disable  : bool|None


# def get_user(db,username:str):
#     if username in db:
#         user_dict = db[username]
#         return user_dict
    
# def decode_token(token):
#     MY_decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  
#     return {
#         "data" : MY_decode_jwt
#     }



# def get_curent_user(token:Annotated[str,Depends(outh2_scheme)]):
#     user = decode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authantication credential",
#             headers={"WWW-Authentication":"bearer"})
#     return user


# # def get_curent_active_user(curent_user:Annotated[my_user,Depends(get_curent_user)]):
# #     if curent_user.disable:
# #         raise HTTPException(status_code=400,detail="inactive user")
# #     return curent_user


# @app.post("/token/")
# def loggin(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
#     user_dict = user_database.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400,detail="Incorect password")
#     user = user_dict
#     password = form_data.password
#     if not password == user["hashed_password"]:
#         raise HTTPException(status_code=400, detail = ["Incorrect user or password",password,user["hashed_password"]])
#     return {"massage":"user pass","username":user["username"],"token_type":"for login"}


# # @app.get("/users/me")
# # def read_user_me(current_user:Annotated[my_user,Depends(get_curent_active_user)]):
# #     return current_user


# # $2b$12$JQljNDy9I/01AOvZEPG2r.qjqzQ5peQZrXcA/hKBRhBBn6ENnBS/C





from fastapi import FastAPI, HTTPException, Depends, status, Form
from pydantic import BaseModel, Field, EmailStr, constr
from enum import Enum
from typing import Optional
from pymongo import MongoClient
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# JWT settings
SECRET_KEY = "my_name_akash_I_am_from_......."
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 59

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hashed(password):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None



# Models

class LoginRequest(BaseModel):
    email: str
    password: str


class Role(str, Enum):
    admin = "Admin"
    hr = "HR"
    employee = "Employee"


class Admin(BaseModel):
    name: str
    admin_id: str
    password: constr(min_length=6) # type: ignore
    email_id: str
    mobile: constr(min_length=10, max_length=10) # type: ignore


class HR(BaseModel):
    name: str
    hr_id: str
    password: constr(min_length=6) # type: ignore
    email_id: str
    qualification: str = Field(...)
    mobile: constr(min_length=10, max_length=10) # type: ignore
    experience_year: Optional[int]


class Employee(BaseModel):
    name: str
    emp_id: str
    password: constr(min_length=6) # type: ignore
    email: str
    mobile: constr(min_length=10, max_length=10) # type: ignore
    qualification: str = Field(...)
    experience_year: Optional[int]
    technology: str = Field(...)
    position: str


# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["sked_group"]
admin_collection = db["ADMIN"]
hr_collection = db["HR"]
employee_collection = db["EMPLOYEES"]
assets_collection = db["ASSETS"]


# Get current user
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return payload


# Routes
@app.post("/admin/create")
def create_admin(admin: Admin):
    if admin_collection.find_one({"admin_id": admin.admin_id}):
        raise HTTPException(status_code=400, detail="Admin already exists")

    admin_dict = admin.dict()
    admin_dict["password"] = get_password_hashed(admin_dict["password"])
    result = admin_collection.insert_one(admin_dict)
    admin_dict["_id"] = str(result.inserted_id)
    return {"msg": "Admin created successfully", "data": admin_dict}



@app.post("/login")
def login_user(data: LoginRequest):
    email = data.email
    password = data.password
    user = admin_collection.find_one({"email_id": email})
    role = "Admin"
    
    if not user:
        user = hr_collection.find_one({"email_id": email})
        role = "HR"

    if not user:
        user = employee_collection.find_one({"email": email})
        role = "Employee"

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token({"sub": email, "role": role})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/hr/create")
def create_hr(hr: HR, current_user=Depends(get_current_user)):
    if current_user["role"] != "Admin":
        raise HTTPException(status_code=403, detail="Only admin can create HR")

    if hr_collection.find_one({"hr_id": hr.hr_id}):
        raise HTTPException(status_code=400, detail="HR already exists")

    hr_dict = hr.dict()
    hr_dict["password"] = get_password_hashed(hr_dict["password"])
    result = hr_collection.insert_one(hr_dict)
    hr_dict["_id"] = str(result.inserted_id)
    return {"msg": "HR created successfully", "data": hr_dict}


@app.post("/employee/create")
def create_employee(employee: Employee, current_user=Depends(get_current_user)):
    if current_user["role"] != "HR":
        raise HTTPException(status_code=403, detail="Only HR can create Employee")

    if employee_collection.find_one({"emp_id": employee.emp_id}):
        raise HTTPException(status_code=400, detail="Employee already exists")

    emp_dict = employee.dict()
    emp_dict["password"] = get_password_hashed(emp_dict["password"])
    result = employee_collection.insert_one(emp_dict)
    emp_dict["_id"] = str(result.inserted_id)
    return {"msg": "Employee created successfully", "data": emp_dict}
