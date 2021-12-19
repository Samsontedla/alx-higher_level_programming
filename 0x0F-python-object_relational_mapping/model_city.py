#!/usr/bin/python3
"""class definition of a City and an instance Base"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        id (sqlalchemy.Integer): The City's id.
        name (sqlalchemy.String): The City's name.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
