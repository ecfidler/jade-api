from fastapi import FastAPI, File, UploadFile, HTTPException, status
# from fastapi.responses import JSONResponse

from random import randint

from .filemanager import get_file_listing, read_file_from_filename, save_file

tags = [
    {
        "name": "Files",
        "description": "Files stored in storage on the printer"
    },
    {
        "name": "Status",
        "description": "Physical data collected by the printer"
    }
]

app = FastAPI(title="JADE API",
              description="The API that the JADE interface uses to interact with the printer",
              openapi_tags=tags)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/ping")
async def test():
    return {"message": "pong!"}


@app.get("/files", tags=["Files"])
async def files_listing():
    return get_file_listing()


# https://www.tutorialspoint.com/fastapi/fastapi_uploading_files.htm
@app.put("/file/{name}", tags=["Files"])
async def put_file(name: str, file: UploadFile):
    save_file(name, file.read())
    return {"file_size": len(file)}


@app.get("/file/{name}", tags=["Files"])
async def get_file(name: str):
    try:
        return {"name": name, "data": read_file_from_filename(name)}
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"File not found: {name}")


@app.get("/printerStatus", tags=["Status"])
async def get_printer_status():
    # send randomized value for temperatures
    return {"status": "randomzied Data", "bedTemperature": randint(0, 100), "hotEndTemperature": randint(0, 400)}
