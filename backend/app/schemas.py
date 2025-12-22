from pydantic import BaseModel


class ProductOut(BaseModel):
    id: int
    name: str
    calories_per_100g: float

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    name: str
    calories_per_100g: float


class ProductUpdate(BaseModel):
    name: str | None = None
    calories_per_100g: float | None = None
