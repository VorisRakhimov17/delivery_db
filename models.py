from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')  # Backref o'zgartirildi

    def __repr__(self):
        return f'<User {self.username}>'


class Order(Base):
    ORDERS_STATUSES = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered')
    )
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    status = Column(ChoiceType(ORDERS_STATUSES), default='PENDING')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')  # Backref o'zgartirildi
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', back_populates='orders')  # Backref o'zgartirildi

    def __repr__(self):
        return f'<Order {self.id}>'


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    price = Column(Integer, nullable=False)
    orders = relationship('Order', back_populates='product')

    def __repr__(self):
        return f'<Product {self.name}>'
