from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr,constr
from enum import Enum
from typing import Optional



app = FastAPI()

class role(str,Enum):
    admin : "Admin"         #type: ignore
    hr    : "HR"            # type: ignore
    employee:"Employee"     # type: ignore



class admin(BaseModel):
    name : str
    admin_id : str
    password : constr(min_length=6)        # type: ignore
    email_id : EmailStr
    mobile   : constr(min_length=10, max_length=10)  # type: ignore



class hr(BaseModel):
    name : str
    hr_id : str
    password : str    
    email_id : EmailStr
    qualification : str=Field(...)
    mobile : constr(min_length=10,max_length=10) # type: ignore
    experience_year : Optional[int]



class Employee(BaseModel):
    name  : str
    emp_id: str
    password : constr(min_length=6)      # type: ignore
    email : EmailStr
    mobile : constr(min_length=10,max_length=10) # type: ignore
    qualification : str= Field(...)

    experience_year : Optional[int]
    technology : str = Field(...)
    position   : str




