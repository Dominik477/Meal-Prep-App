from sqlalchemy.orm import Session

from app.models import Product


def seed_products(db: Session):
    exists = db.query(Product).first()
    if exists:
        return

    db.add_all(
        [
            Product(name="Ryż biały", calories_per_100g=360),
            Product(name="Pierś z kurczaka", calories_per_100g=165),
            Product(name="Brokuł", calories_per_100g=35),
        ]
    )
    db.commit()
