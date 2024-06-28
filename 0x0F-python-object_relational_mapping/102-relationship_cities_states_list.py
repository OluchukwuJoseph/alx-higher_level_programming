#!/usr/bin/python3
"""
This script lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Create engine
    DATABASE_URL = f"mysql+mysqldb://{sys.argv[1]}:\
            {sys.argv[2]}@localhost:3306/{sys.argv[3]}"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    # Create tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    # List Cities
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
