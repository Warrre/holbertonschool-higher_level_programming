#!/usr/bin/python3
"""
Script that takes the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Création du curseur et exécution de la requête SQL
    cursor = db.cursor()

    # Utilisation de paramètres pour éviter les injections SQL
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (search_name,))

    # Récupération et formatage des résultats
    results = cursor.fetchall()
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Fermeture des ressources
    cursor.close()
    db.close()
