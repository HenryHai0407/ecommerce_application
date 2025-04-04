from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# Database connection setup
DATABASE_URL = "mysql://admin:admin123+@127.0.0.1:3307/ecommerce_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our ORM models
Base = declarative_base()

# Product Model (you can adjust the fields as per your actual database structure)
class Product(Base):
    __tablename__ = "products_product"  # This is the table you're fetching data from

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Integer)  # Adjust according to your schema
    quantity = Column(Integer)

# Initialize FastAPI
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoint to get product list
@app.get("/products/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()  # Fetch all products from the database
    return products

# API Endpoint to get a specific product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
