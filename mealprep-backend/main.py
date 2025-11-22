from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="MealPrep API",
    version="0.1.0",
)



class Product(BaseModel):
    id: int
    name: str
    calories: int



PRODUCTS_DB = {
    1: Product(id=1, name="Ryż biały 100g", calories=360),
    2: Product(id=2, name="Pierś z kurczaka 100g", calories=165),
    3: Product(id=3, name="Brokuł 100g", calories=35),
}




@app.get("/api/products", response_model=List[Product])
def get_products():

    return list(PRODUCTS_DB.values())




@app.get("/api/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: str):

    try:
        pid = int(product_id)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Parametr 'product_id' musi być liczbą całkowitą.",
        )

    product = PRODUCTS_DB.get(pid)
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Produkt o ID {pid} nie istnieje.",
        )

    return product
