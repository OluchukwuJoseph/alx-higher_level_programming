#!/usr/bin/python3
"""
This script adds the State object “Louisiana” the database `hbtn_0e_6_usa`
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine
    DATABASE_URL = f"mysql+mysqldb://{argv[1]}:\
            {argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    # Create state table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add new state
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
