from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import crud, schemas
from dependencies import get_db

router = APIRouter(prefix="/api/categories", tags=["Categories"])


@router.get("/", response_model=list[schemas.CategoryResponse])
def list_categories(page: int = 1, db: Session = Depends(get_db)):
    limit = 5
    skip = (page - 1) * limit
    return crud.get_categories(db, skip, limit)


@router.post("/", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, data)


@router.get("/{id}", response_model=schemas.CategoryResponse)
def get_category(id: int, db: Session = Depends(get_db)):
    return crud.get_category(db, id)


@router.put("/{id}", response_model=schemas.CategoryResponse)
def update_category(id: int, data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.update_category(db, id, data)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_category(id: int, db: Session = Depends(get_db)):
    return crud.delete_category(db, id)
