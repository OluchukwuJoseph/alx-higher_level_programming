#!/usr/bin/python3
"""
This script takes in the name of a `state` as an argument and
lists all cities of that state
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve command line argument
    argument = sys.argv[4]
    # Establish connection with Database
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         port=3306,
                         db=sys.argv[3])
    # Get and Execute query
    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (argument,))

    # Print results
    rows = cursor.fetchall()
    if (rows):
        print(rows[0][0], end="")
        rows = rows[1:]
        for row in rows:
            print(f', {row[0]}', end="")
        print()

    # Close Connection
    cursor.close()
    db.close()
