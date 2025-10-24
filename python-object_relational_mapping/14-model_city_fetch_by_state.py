#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_6_usa,
displayed as <state name>: (<city id>) <city name>
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(
        State.name,
        City.id,
        City.name
    ).join(City).order_by(City.id).all()

    for state_name, city_id, city_name in results:
        print("{}: ({}) {}".format(state_name, city_id, city_name))
