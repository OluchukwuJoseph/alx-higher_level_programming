#!/usr/bin/python3
"""
This script lists all `cities` from the database `hbtn_0e_4_usa`
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Establish connection with Database
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         port=3306,
                         db=sys.argv[3])
    # Get and Execute query
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    if (rows):
        for row in rows:
            print(row)

    # Close Connection
    cursor.close()
    db.close()
