from sqlalchemy.orm import Session, selectinload
from schemas.pharmacystocks import PharmacyStockCreate
from db.models.pharmacystocks import PharmacyStock


def create_pharmacy_stock(
    stock_data: PharmacyStockCreate,
    db: Session,
    pharmacy_id: int,
):
    new_stock = PharmacyStock(
        **stock_data.dict(),
        pharmacy_id=pharmacy_id,
    )
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock


def get_all_pharmacy_stocks(
    db: Session, pharmacy_id: int, skip: int = 0, limit: int = 100
):
    return (
        db.query(PharmacyStock)
        .filter(PharmacyStock.pharmacy_id == pharmacy_id)
        .offset(skip)
        .limit(limit)
        .options(
            selectinload(PharmacyStock.pharmacy),
            selectinload(PharmacyStock.medicine),
        )
        .all()
    )


def get_pharmacy_stock_by_id(stock_id: int, db: Session, pharmacy_id: int):
    return (
        db.query(PharmacyStock)
        .filter(
            PharmacyStock.stock_id == stock_id,
            PharmacyStock.pharmacy_id == pharmacy_id,
        )
        .first()
    )


def update_pharmacy_stock(stock_id: int, update_data, db: Session, pharmacy_id: int):
    if isinstance(update_data, PharmacyStockCreate):
        update_data = update_data.dict(
            exclude_unset=True
        )  # Convert Pydantic model to dict

    stock = (
        db.query(PharmacyStock)
        .filter(
            PharmacyStock.stock_id == stock_id,
            PharmacyStock.pharmacy_id == pharmacy_id,
        )
        .first()
    )
    if stock:
        for key, value in update_data.items():
            setattr(stock, key, value)
        db.commit()
        db.refresh(stock)
    return stock


def delete_pharmacy_stock(db: Session, stock_id: int, pharmacy_id: int):
    stock = (
        db.query(PharmacyStock)
        .filter(
            PharmacyStock.stock_id == stock_id,
            PharmacyStock.pharmacy_id == pharmacy_id,
        )
        .first()
    )
    if stock:
        db.delete(stock)
        db.commit()
    return stock
