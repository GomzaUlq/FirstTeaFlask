from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from backend.db import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String, unique=True, index=True)
    slug = db.Column(db.String, unique=True, index=True)
    products = relationship('Product', back_populates='category')


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String, index=True)
    slug = db.Column(db.String, unique=True, index=True)
    category_id = db.Column(db.Integer, ForeignKey("categories.id"))
    price = db.Column(db.Integer)
    image = db.Column(db.String)
    description = db.Column(db.String(1000), nullable=True)
    category = relationship("Category", back_populates="products")
