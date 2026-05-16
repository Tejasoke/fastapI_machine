from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud, schemas
from dependencies import get_db

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get("/", response_model=list[schemas.ProductResponse])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    limit = 5
    skip = (page - 1) * limit
    return crud.get_products(db, skip, limit)


@router.post("/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, data)


@router.get("/{id}", response_model=schemas.ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, id)


@router.put("/{id}", response_model=schemas.ProductResponse)
def update_product(id: int, data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db, id, data)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_product(id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, id)
