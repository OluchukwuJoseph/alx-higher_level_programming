#!/usr/bin/python3
"""
This script prints the first `State` object from the database `hbtn_0e_6_usa`
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
first_state = session.query(State).order_by(State.id).first()

if (first_state is not None):
    print(f"{first_state.id}: {first_state.name}")
else:
    print("Nothing")

session.close()
