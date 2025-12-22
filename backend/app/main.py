from fastapi import FastAPI

from app.database import engine, Base
from app import models 
from app.routers.products import router as products_router

app = FastAPI(title="MealPrep API")

Base.metadata.create_all(bind=engine)

app.include_router(products_router)


@app.get("/health")
def health():
    return {"status": "ok"}
