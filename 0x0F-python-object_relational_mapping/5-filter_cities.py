#!/usr/bin/python3
"""
This script takes in the name of a `state` as an argument and
lists all cities of that state
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
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
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (argument,))

    # Print results
    rows = cursor.fetchall()

    for i, row in enumerate(rows):
        print("{}".format(row[0]), end="")
        if i < len(rows) - 1:
            print(', ', end="")
    print('\n', end="")
    # Close Connection
    cursor.close()
    db.close()
