from fastapi import FastAPI

app = FastAPI(title="JADE api")

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/ping")
async def test():
    return {"message": "pong!"}