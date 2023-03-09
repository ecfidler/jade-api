from fastapi import FastAPI
from random import randint

app = FastAPI(title="JADE api")

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/ping")
async def test():
    return {"message": "pong!"}

@app.get("/files")
async def filesListing():
    tempfiles = [
        { "name": "fileone.stl" },
        { "name": "filetwo.stl" },
        { "name": "filethree.stl" },
        { "name": "3dBenchy.stl" },
    ]

    return tempfiles

# @app.get("/file/{name}")
# async def getFile():
#     # load and send stl file
#     return

@app.get("/printerStatus")
async def printerStatus():
    # send randomized value for temperatures
    return {"status": "randomzied Data", "bedTemperature": randint(0,100), "hotEndTemperature": randint(0, 400)}