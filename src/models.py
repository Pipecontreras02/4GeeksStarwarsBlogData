import os
import sys
from sqlalchemy import  Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_table = Table('user_favorites', Base.metadata,
    Column('user_id', ForeignKey('user.id')),
    Column('character_id', ForeignKey('character.id')),
    Column('planet_id', ForeignKey('planet.id')),
    Column('starship_id', ForeignKey('starship.id'))
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    character = relationship("Character",
                    secondary=association_table)
    starship = relationship("Starship",
                    secondary=association_table)
    planet = relationship("Planet",
                    secondary=association_table)


class Starship(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(String(250))
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    hyperdrive_rating = Column(Integer)
    mglt = Column(Integer)
    starship_class = Column(String(250))
    pilots = Column(String(250))
    films = Column(String(250))

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(Integer)
    terrain = Column(String(250))
    surface_water = Column(Integer)
    population = Column(Integer)
    residents = Column(String(250))
    films = Column(String(250))

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(20))
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(25))
    homeworld = Column(String(250))
    films = Column(String(250))
    species = Column(String(250))
    vehicles = Column(String(250))
    starships = Column(String(250))
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')