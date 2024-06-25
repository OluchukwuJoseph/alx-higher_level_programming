#!/usr/bin/python3
"""
This script contains the class definition of a State and
an instance Base = declarative_base()
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


# Create Base class
Base = declarative_base()


class State(Base):
    """class definition states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
