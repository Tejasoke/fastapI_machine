# FastAPI Machine Test

## Features
- FastAPI REST API for categories and products
- PostgreSQL and SQLAlchemy ORM
- Category ↔ Product one-to-many relationship
- Server-side pagination on list endpoints
- Product detail includes associated category data

## API Endpoints
### Category
- `GET /api/categories?page=1` - list categories
- `POST /api/categories` - create category
- `GET /api/categories/{id}` - fetch category by ID
- `PUT /api/categories/{id}` - update category by ID
- `DELETE /api/categories/{id}` - delete category by ID

### Product
- `GET /api/products?page=1` - list products
- `POST /api/products` - create product
- `GET /api/products/{id}` - fetch product by ID 
- `PUT /api/products/{id}` - update product by ID
- `DELETE /api/products/{id}` - delete product by ID

## Database Design
- Table: `categories`
  - `id` INT PRIMARY KEY
  - `name` TEXT NOT NULL
- Table: `products`
  - `id` INT PRIMARY KEY
  - `name` TEXT NOT NULL
  - `price` INT NOT NULL
  - `category_id` INT NOT NULL FOREIGN KEY REFERENCES categories(id)

Relationship: One Category → Many Products
Each Product belongs to one Category.

## Run Instructions
1. Create and activate virtual environment:
   ```bash
   cd fastapi_machine
   source bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary
   ```
3. Ensure PostgreSQL is running and the database exists:
   - URL: `postgresql://postgres:root@localhost:5432/fastapi_machine`
   - Create the database if needed:
     ```bash
     createdb -U postgres fastapi_machine
     ```
4. Start the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Open docs at `http://127.0.0.1:8000/docs`
