#!/usr/bin/python3
"""
This script prints all City objects from the database `hbtn_0e_14_usa`
"""
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":
    # Create an engine
    DATABASE_URL = f"mysql+mysqldb://{argv[1]}:\
            {argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    State.cities = relationship("City", back_populates="state")
    # Create state table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve states
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
