#!/usr/bin/python3
"""
9-model_state_filter_a
that lists all State objects
from the database hbtn_0e_6_usa
where name contains the letter 'a'
and is ordered by id (ascending)
If no state matches the query, it doesn't print anything.
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
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id)
    for row in states:
        print("{}: {}".format(row.id, row.name))
    session.close()
