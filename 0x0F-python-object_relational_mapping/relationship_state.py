#!/usr/bin/python3
"""
This script contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


# Create Base class
Base = declarative_base()


# Create City class
class State(Base):
    """class definition for states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
