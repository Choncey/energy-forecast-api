from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Energy Predictor API")
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Hello, Energy Predictor!"}
