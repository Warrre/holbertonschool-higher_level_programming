#!/usr/bin/python3
"""
Module to list all cities from a database
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
    cursor.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = '{}' \
                ORDER BY cities.id ASC;".format(sys.argv[4]))
    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()
    