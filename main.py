from fastapi import FastAPI

import models
from database import Base, engine
from routers import category, product

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(category.router)
app.include_router(product.router)