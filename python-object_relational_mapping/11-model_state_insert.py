#!/usr/bin/python3
"""
Script qui ajoute l'état "Louisiana" à la base de données.
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

    # Création et ajout du nouvel état
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Affichage de l'ID du nouvel état
    print("{}".format(new_state.id))

    # Fermeture de la session
    session.close()
    