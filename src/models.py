import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)
    product = Column(String(250), nullable=False)
    picture = Column(String(250), nullable=False)
    product = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    price = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
   

class Scheduling(Base):
    __tablename__ = 'scheduling'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    start_hour = Column(String(250), nullable=False)
    end_hour = Column(String(250), nullable=False)
    day = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
   

class OrderItem(Base):
    __tablename__ = 'orderitem'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    inventory = relationship(Inventory)
  

class Order(Base):
    __tablename__ = 'order'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    total_price = Column(String(250), nullable=False)
    status = Column(String(250), nullable=False)
    paymentmethod_id = Column(Integer, ForeignKey('paymentmethod.id'), nullable=False)
    
    
 
class Shopingcar(Base):
    __tablename__ = 'user_item'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    status = Column(String(250), nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.id'), nullable=False)
    inventory = relationship(Inventory)


class PaymentMethod(Base):
    __tablename__ = 'paymentmethod'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    payment_type = Column(String(250), nullable=False)
    transaction = Column(String(250), nullable=False)
    amount_transaction = Column(String(250), nullable=False)
   
       

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
