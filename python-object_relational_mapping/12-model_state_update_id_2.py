#!/usr/bin/python3
"""
12-model_state_update_id_2
that changes the name of the State
object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa
If the table is empty, it prints "Nothing"
If the state with id = 2 does not exist, it does nothing
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
    state = session.query(State).where(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
