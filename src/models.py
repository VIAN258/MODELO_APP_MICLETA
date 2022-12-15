import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
   

class Ships(Base):
    __tablename__ = 'ships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    ships_name = Column(String(250))
   

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters_name = Column(String(250))
  

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    ships_id = Column(Integer, ForeignKey('ships.id'), nullable=False)

class Type(Base):
    __tablename__ = 'type'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    ships_id = Column(Integer, ForeignKey('ships.id'))
    
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
