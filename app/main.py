from fastapi import FastAPI, Request
from socket import gethostname
from app.api.routes import router
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = FastAPI()

app.include_router(router)


@app.get("/")
async def get_clientip(request: Request):
    hostname = gethostname()
    client_ip = request.client.host
    message = "Hello " + client_ip + " From " + hostname
    return message


HOST = getenv("HOST", "0.0.0.0")
PORT = getenv("PORT", "8000")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
