#!/usr/bin/python3
"""
Script qui recherche un État par son nom dans la base de données.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupération des arguments, y compris le nom d'état à rechercher
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]  # Nom de l'état à rechercher

    # Établissement de la connexion à la base de données
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'état par son nom exact
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Fermeture de la session
    session.close()
