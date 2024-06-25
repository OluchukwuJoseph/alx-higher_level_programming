#!/usr/bin/python3
"""
This script lists all State objects that contains the letter `a`
from the database `hbtn_0e_6_usa`
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


# Create an engine
DATABASE_URL = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Create Tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query table and print result
states = session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id).all()

for state in states:
    print(f"{state.id}: {state.name}")

session.close()
