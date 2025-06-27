#!/usr/bin/python3
"""
Script qui filtre les états d'une base de données par nom de manière sécurisée.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]     # Nom d'utilisateur MySQL
    password = sys.argv[2]     # Mot de passe MySQL
    db_name = sys.argv[3]      # Nom de la base de données
    search_name = sys.argv[4]  # Nom d'état à rechercher

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",      # Adresse du serveur MySQL
        port=3306,             # Port par défaut
        user=username,
        passwd=password,
        db=db_name
    )

    # Création du curseur et exécution de la requête
    # Utilisation de %s comme paramètre pour éviter les injections SQL
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (search_name,)
    )
    results = cursor.fetchall()

    # Affichage des résultats
    for row in results:
        print(row)

    # Fermeture des ressources
    cursor.close()
    db.close()
