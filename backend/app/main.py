from fastapi import FastAPI

from app.database import engine, Base
from app import models  

app = FastAPI(title="MealPrep API")

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}
