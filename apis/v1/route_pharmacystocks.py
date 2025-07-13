from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.pharmacystocks import PharmacyStockCreate, PharmacyStockShow
from core.security import get_current_user

from db.repository.pharmacystocks import (
    create_pharmacy_stock,
    get_all_pharmacy_stocks,
    get_pharmacy_stock_by_id,
    update_pharmacy_stock,
    delete_pharmacy_stock,
)

router = APIRouter()


@router.post("/", response_model=PharmacyStockShow, status_code=status.HTTP_201_CREATED)
def create_stock(
    stock_data: PharmacyStockCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    return create_pharmacy_stock(
        stock_data=stock_data,
        pharmacy_id=pharmacy_id,
        db=db,
    )


@router.get("/{stock_id}", response_model=PharmacyStockShow)
def read_stock(
    stock_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    stock = get_pharmacy_stock_by_id(stock_id, db, pharmacy_id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock


@router.get("/", response_model=list[PharmacyStockShow], status_code=status.HTTP_200_OK)
def read_stocks(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    return get_all_pharmacy_stocks(db, pharmacy_id)


@router.put("/{stock_id}", response_model=PharmacyStockShow)
def update_stock_data(
    stock_id: int,
    stock: PharmacyStockCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    updated_stock = update_pharmacy_stock(stock_id, stock, db, pharmacy_id)
    if not updated_stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return updated_stock


@router.delete("/{stock_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_stock(
    stock_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    pharmacy_id = current_user.get("pharmacy_id")
    deleted_stock = delete_pharmacy_stock(db, stock_id, pharmacy_id)
    if not deleted_stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return {"message": "Stock deleted successfully"}
