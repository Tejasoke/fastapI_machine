from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload
import models
import schemas


def get_categories(db: Session, skip: int, limit: int):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, data: schemas.CategoryCreate):
    obj = models.Category(name=data.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_category(db: Session, id: int):
    obj = db.query(models.Category).filter(models.Category.id == id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return obj


def update_category(db: Session, id: int, data: schemas.CategoryCreate):
    obj = get_category(db, id)
    obj.name = data.name
    db.commit()
    db.refresh(obj)
    return obj


def delete_category(db: Session, id: int):
    obj = get_category(db, id)
    db.delete(obj)
    db.commit()
    return {"message": "Deleted Category"}



def get_products(db: Session, skip: int, limit: int):
    return (
        db.query(models.Product)
        .options(joinedload(models.Product.category))
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_product(db: Session, data: schemas.ProductCreate):
    category = db.query(models.Category).filter(models.Category.id == data.category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    obj = models.Product(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_product(db: Session, id: int):
    obj = (
        db.query(models.Product)
        .options(joinedload(models.Product.category))
        .filter(models.Product.id == id)
        .first()
    )
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return obj


def update_product(db: Session, id: int, data: schemas.ProductCreate):
    obj = get_product(db, id)
    category = db.query(models.Category).filter(models.Category.id == data.category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    obj.name = data.name
    obj.price = data.price
    obj.category_id = data.category_id
    db.commit()
    db.refresh(obj)
    return obj


def delete_product(db: Session, id: int):
    obj = get_product(db, id)
    db.delete(obj)
    db.commit()
    return {"message": "Deleted Product"}
