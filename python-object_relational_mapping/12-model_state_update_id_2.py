#!/usr/bin/python3
"""
Script qui change le nom d'un State dans la base de données.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Établissement de la connexion à la base de données
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'état avec id=2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Modification du nom de l'état
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Fermeture de la session
    session.close()
