#!/usr/bin/python3
"""
1-filter_states
that lists all states from the
database hbtn_0e_0_usa
where name starts with 'n'
and is ordered by id (ascending)
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    name_search = sys.argv[4]
    cursor = db_connection.cursor()
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id"
        .format(name_search))
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()
