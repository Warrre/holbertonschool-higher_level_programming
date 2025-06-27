#!/usr/bin/python3
"""
Script qui liste tous les états d'une base de données.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]  # Nom d'utilisateur MySQL
    password = sys.argv[2]  # Mot de passe MySQL
    db_name = sys.argv[3]   # Nom de la base de données

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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération et affichage des résultats
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Fermeture des ressources
    cursor.close()
