from fastapi import FastAPI

app = FastAPI(title="Fin-Ops Sentinel")

@app.get("/")
def home():
    return {"message": "Fin-Ops Sentinel API is running"}