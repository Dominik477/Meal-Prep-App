from pydantic import BaseModel


class ProductOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
