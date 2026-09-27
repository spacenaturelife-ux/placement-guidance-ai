from fastapi import FastAPI

app = FastAPI(title="Placement Guidance AI")

@app.get("/")
def root():
    return {"message": "Placement Guidance AI backend is running"}
