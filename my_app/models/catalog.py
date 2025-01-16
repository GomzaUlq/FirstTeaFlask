from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from backend.models import Base


class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, index=True, primary_key=True)
    name = mapped_column(String, unique=True, index=True)
    slug = mapped_column(String, unique=True, index=True)
    products = relationship('Product', back_populates='category')


class Product(Base):
    __tablename__ = 'products'

    id = mapped_column(Integer, index=True, primary_key=True)
    name = mapped_column(String, index=True)
    slug = mapped_column(String, unique=True, index=True)
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    price = mapped_column(Integer)
    image = mapped_column(String)
    description = mapped_column(String(1000), nullable=True)
    category = relationship("Category", back_populates="products")
