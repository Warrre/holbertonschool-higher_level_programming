#!/usr/bin/python3
"""
1-filter_states
that lists all states from the
database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    name_search = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id;"
    cursor.execute(query, (name_search,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
