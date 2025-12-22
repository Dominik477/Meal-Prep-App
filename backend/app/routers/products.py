from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product
from app.schemas import ProductOut

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).order_by(Product.id).all()


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: str, db: Session = Depends(get_db)):
    try:
        pid = int(product_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="product_id must be an integer")

    product = db.query(Product).filter(Product.id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product
