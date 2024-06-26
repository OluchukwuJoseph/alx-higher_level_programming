#!/usr/bin/python3
"""
This script contains the class definition of a City and
an instance Base = declarative_base()
"""
from sqlalchemy.orm import relationship
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class definition cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")
