#!/usr/bin/python3
"""
Script qui filtre les états d'une base de données par nom.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]     # Nom d'utilisateur MySQL
    password = sys.argv[2]     # Mot de passe MySQL
    db_name = sys.argv[3]      # Nom de la base de données
    search_name = sys.argv[4]  # Nom d'état à rechercher

    # Établissement de la connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",      # Adresse du serveur MySQL
        port=3306,             # Port par défaut
        user=username,
        passwd=password,
        db=db_name
    )

    # Création du curseur et exécution de la requête
    cursor = db.cursor()
    query = "SELECT * FROM states" \
            " WHERE BINARY name = '{}' ORDER BY id ASC".format(search_name)
    cursor.execute(query)

    # Récupération et affichage des résultats
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Fermeture des ressources
    cursor.close()
    db.close()
