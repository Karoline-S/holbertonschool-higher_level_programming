#!/usr/bin/python3

"""defines class definition for State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """create class State with tablename, id,
    and name"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
