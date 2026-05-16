from pydantic import BaseModel


# CATEGORY
class CategoryCreate(BaseModel):
    name: str


class CategoryResponse(CategoryCreate):
    id: int

    class Config:
        from_attributes = True


# PRODUCT
class ProductCreate(BaseModel):
    name: str
    price: int
    category_id: int


class ProductResponse(ProductCreate):
    id: int
    category: CategoryResponse

    class Config:
        from_attributes = True