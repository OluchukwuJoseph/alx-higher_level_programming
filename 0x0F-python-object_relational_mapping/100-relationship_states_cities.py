#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
in the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Create a engine
    DATABASE_URL = f"mysql+mysqldb://{sys.argv[1]}:\
            {sys.argv[2]}@localhost:3306/{sys.argv[3]}"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    # Create tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City
    new_state = State(name="California")
    new_state.cities.append(City(name="San Francisco"))

    session.add(new_state)
    session.commit()

    # Close the connection
    session.close()
