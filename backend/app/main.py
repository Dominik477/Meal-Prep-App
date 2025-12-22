from fastapi import FastAPI

from app.database import engine, Base, SessionLocal
from app import models  
from app.routers.products import router as products_router
from app.routers.auth import router as auth_router
from app.seed import seed_products

app = FastAPI(title="MealPrep API")

Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    seed_products(db)

app.include_router(auth_router)
app.include_router(products_router)


@app.get("/health")
def health():
    return {"status": "ok"}
