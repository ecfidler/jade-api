from fastapi import FastAPI, File, UploadFile, HTTPException, status, Response
# from fastapi.responses import JSONResponse

from random import randint

from filemanager import get_file_listing, read_file_from_filename, save_file

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


@app.put("/file/", tags=["Files"])
async def put_file(file: UploadFile):
    try:
        save_file(file.filename, file.file.read())
        return Response(status_code=status.HTTP_200_OK)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid file. Accepted file types: .stl, .gcode")


@app.get("/file/{name}", tags=["Files"])
async def get_file(name: str):
    try:
        data, suffix = read_file_from_filename(name)
        return Response(content=data, headers={"name": name, "extension": suffix})
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"File not found in directory: {name}")


@app.get("/printerStatus", tags=["Status"])
async def get_printer_status():
    # send randomized value for temperatures
    return {"status": "randomzied Data", "bed_temperature": randint(0, 100), "hot_end_temperature": randint(0, 400)}
