#!/usr/bin/python3
"""
Module to list all states from a database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE CONVERT (`name` USING Latin1) \
                    COLLATE Latin1_General_CS \
                    LIKE 'N%' ORDER BY `id` ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
