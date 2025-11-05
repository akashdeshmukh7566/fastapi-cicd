# files that send by client to api 

from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/files/",tags=["user"])
async def create_file(file:Annotated[bytes, File()]):
    return {"file_text_len" : len(file),
            "data" : file}



@app.post("/uploadfiles/",tags=["file user"])
async def create_upload_files(files : list[UploadFile]):
    return {"filename" : [file.filename and file for file in files]}

