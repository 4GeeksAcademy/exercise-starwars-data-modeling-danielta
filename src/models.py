import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

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

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(50), unique = True)
    password = Column(String(50))

class Characters(Base):
    __tablename__ = 'characters'
    ID = Column(Integer, primary_key=True)
    name = Column(String(50))
    birth_year = Column(String(15))
    gender = Column(String(10))
    height = Column(Integer)
    skin_color = Column(String(15))
    eye_color = Column(String(15))

class Planets(Base):
    __tablename__ = 'planets'
    ID = Column(Integer, primary_key=True)
    name = Column(String(50))
    climate = Column(String(15))
    population = Column(Integer)
    orbital_period = Column(String(50))
    rotation_period = Column(String(15))
    diameter = Column(String(50))

class Favorites(Base):
    __tablename__ = 'favorites'
    ID = Column(Integer, primary_key=True)
    name = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user = relationship(User)
    characters = relationship(Characters)
    planets = relationship(Planets)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
