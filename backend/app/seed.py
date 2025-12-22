from sqlalchemy.orm import Session

from app.models import Product


def seed_products(db: Session):
    exists = db.query(Product).first()
    if exists:
        return

    db.add_all(
        [
            Product(name="Ryż biały"),
            Product(name="Pierś z kurczaka"),
            Product(name="Brokuł"),
        ]
    )
    db.commit()
