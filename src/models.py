import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class  User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_character = relationship('Character', backref='user',uselist='false' )
    planet_character = relationship('Planet', backref='user',uselist='false' )

class Favorites(Base):
    __tablename__ = 'favorites'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey('user.id'))
    

class  Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('favorites.id'))

class Character(Base):
    __tablename__ = 'character'
  
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey('favorites.id'))

    
class  Vehicle(Base):
    __tablename__ = 'vehicle'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('favorites.id'))

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
