#!/usr/bin/python3
"""
10-model_state_my_get
that lists all State objects
from the database hbtn_0e_6_usa
where name matches the argument
and is ordered by id (ascending)
If no state matches the query, it prints "Not found"
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    name_search = sys.argv[4]
    state = session.query(State).filter(State.name == name_search).first()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()
