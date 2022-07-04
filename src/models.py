import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column (Integer, primary_key = True)
    user_name = Column (String(250), nullable = False)
    email = Column (String(250), nullable = False, unique = True)
    password = Column(String(250), nullable = False, unique = True)
   
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Characters (Base):
    __tablename__ = 'character'
    id = Column (Integer, primary_key = True)
    name = Column (String(50), nullable = False, unique = True)
    birth_day = Column(Integer, nullable = False)
    gender = Column (String(20), nullable = False)
    heigth = Column (Integer, nullable = False )
    hair_color = Column (String(25), nullable = False)
    eye_color = Column (String(25), nullable = False)
    uid = Column (Integer) 
    
class Vehicles (Base):
    __tablename__ = 'vehicle'
    id = Column (Integer, primary_key = True)
    name = Column (String (205), Integer, nullable = False, unique = True)
    model = Column (String (250), Integer, nullable = False)
    crew = Column (String (250), nullable = False, unique = True)
    passenger = Column(String(80), nullable=False)
    vehicle_class = Column(String(80), nullable=False)
    model = Column(String(80), nullable=False)
    manufacturer = Column(String(80), nullable=False)
    uid = Column (Integer) 

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    climate = Column(String(80), nullable=False)
    terrain = Column(String(80), nullable=False)
    gravity = Column(String (80), nullable=False) 
    diameter = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False) 
    uid = Column (Integer) 

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
