from typing import List
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Database connection setup
DATABASE_URL = "mysql://admin:admin123+@127.0.0.1:3307/ecommerce_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our ORM models
Base = declarative_base()

# Product Model (SQLAlchemy ORM model)
class Product(Base):
    __tablename__ = "products_product"  # This is the table you're fetching data from
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Integer)  # Adjust according to your schema
    quantity = Column(Integer)

# Pydantic model for product responses
class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    quantity: int

    class Config:
        orm_mode = True

# Initialize FastAPI
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint for basic testing
@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

# API Endpoint to get product list with pagination
@app.get("/products/", response_model=List[ProductResponse])
def get_products(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, description="Maximum number of records to return"),
    db: Session = Depends(get_db)
):
    products = db.query(Product).offset(skip).limit(limit).all()  # Fetch paginated products
    return products

# API Endpoint to get a specific product by ID
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


### QUERY RESULT:
# http://127.0.0.1:8000/products/?skip=0&limit=2 for example with SKIP: 0 and LIMIT: 2