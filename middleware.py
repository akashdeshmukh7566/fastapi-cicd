import time
from fastapi import FastAPI,Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()


class middlewareA(BaseHTTPMiddleware):
    def dispatch(self,request:Request,call_next):
        print("[Middleware A] - before route handler")
        start_time = time.time()

        response =  call_next(request)

        duration = time.time()-start_time

        print(f"[middleware A] - after rout handler | Duration : {duration:.4f} second")
        return response

class middlewareB(BaseHTTPMiddleware):
    def dispatch(self, request, call_next):
        print("[Middleware B] - before rout handler")
        responce =  call_next(request)
        print("[Middleware B] - after rout handler")
        return responce


app.add_middleware(middlewareA)
app.add_middleware(middlewareB)


@app.get("/")
async def read_root():
    print("[Rout Handle] - Handling request")
    return {"message ": "hello from Fastapi"}

