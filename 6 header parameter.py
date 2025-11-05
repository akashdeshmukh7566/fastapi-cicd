# header parameter - data that come from the HTTP request header.



from fastapi import FastAPI,Header
from typing import Annotated

app = FastAPI()
@app.get("/custom/")
async def get_header(user_agent: Annotated[str|None, Header()]=None):
    
    return {
        "user_Agent" : user_agent
    }


