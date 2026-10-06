from fastapi import FastAPI
from database import engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Placement Guidance AI")

@app.get("/")
def root():
    return {"message": "Placement Guidance AI backend is running"}