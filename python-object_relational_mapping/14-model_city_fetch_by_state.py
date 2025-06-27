#!/usr/bin/python3
"""
Script qui affiche toutes les villes par état de la base de données.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Établissement de la connexion à la base de données
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour obtenir toutes les villes avec leur état associé
    results = session.query(
        City,
        State).filter(
        City.state_id == State.id).order_by(
            City.id).all()

    # Affichage des résultats
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Fermeture de la session
    session.close()
