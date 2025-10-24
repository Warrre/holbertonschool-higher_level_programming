#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
Takes 3 arguments: mysql username, mysql password and database name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
<<<<<<< HEAD
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE CONVERT (`name` USING Latin1) \
                    COLLATE Latin1_General_CS \
                    LIKE 'N%' ORDER BY `id` ASC")
    rows = cursor.fetchall()
=======

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
>>>>>>> 81e32a4ae05c85348b2bc3d1fb9671c67fda66d2

    for row in rows:
        print(row)

    cur.close()
    db.close()

