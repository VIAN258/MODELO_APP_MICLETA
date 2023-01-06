import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class UserWs(Base):
    __tablename__ = 'userws'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    bikerws = Column(String(250), nullable=False)

class WsItem(Base):
    __tablename__ = 'wsitem'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    category = Column(String(250), nullable=False)
    product = Column(String(250), nullable=False)
    url_picture = Column(String(250), nullable=False)
    product = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    price = Column(String(250), nullable=False)
    userws_id = Column(Integer, ForeignKey('userws.id'), nullable=False)
    userws = relationship(UserWs)
   

class Open_Close_Ws(Base):
    __tablename__ = 'open_close_ws'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    start_hour = Column(String(250), nullable=False)
    end_hour = Column(String(250), nullable=False)
    day = Column(String(250), nullable=False)
    userws_id = Column(Integer, ForeignKey('userws.id'), nullable=False)
    userws = relationship(UserWs)
   

class OrderItem(Base):
    __tablename__ = 'orderitem'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship(Order)
    wsitem_id = Column(Integer, ForeignKey('wsitem.id'), nullable=False)
    wsitem = relationship(WsItem)
  

class Order(Base):
    __tablename__ = 'order'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userws_id = Column(Integer, ForeignKey('userws.id'), nullable=False)
    userws = relationship(UserWs)
    total_price = Column(String(250), nullable=False)
    transaction = Column(String(250), nullable=False)
    status = Column(String(250), nullable=False)
    
    
 
class User_Item(Base):
    __tablename__ = 'user_item'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    price = Column(String(250), nullable=False)
    user_ws.id = Column(Integer, ForeignKey('user_ws.id'), nullable=False)
    user_ws = relationship(User_Ws)
    description = Column(String(250), nullable=False)
    ws_item.id = Column(Integer, ForeignKey('ws_item.id'), nullable=False)
    ws_item = relationship(Ws_Item)


class Payment_Method(Base):
    __tablename__ = 'payment_method'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_ws.id = Column(Integer, ForeignKey('user_ws.id'), nullable=False)
    user_ws = relationship(User_Ws)
    cash = Column(String(250), nullable=False)
    order.id = Column(Integer, ForeignKey('order.id'), nullable=False)
    order = relationship(Order) 
       

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
