from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from app.backend.models import Base
from sqlalchemy.schema import CreateTable


class Cart(Base):
    __tablename__ = 'carts'

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    products = relationship('CartItem', backref='cart', lazy=True)

    def total_quantity(self):
        return sum(item.quantity for item in self.products)


class CartItem(Base):
    __tablename__ = 'cart_items'

    id = mapped_column(Integer, primary_key=True)
    cart_id = mapped_column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = mapped_column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = mapped_column(Integer, nullable=False, default=1)

    product = relationship('Product', backref='cart_items', lazy=True)

    def update_quantity(self, new_quantity):
        if new_quantity > 0:
            self.quantity = new_quantity
        else:
            raise ValueError("Quantity must be greater than zero.")


