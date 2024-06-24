#!/usr/bin/python3
"""
This script takes in the name of a `state` as an argument and
lists all cities of that state
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve command line argument
    argument = sys.argv[4].split(';')
    # Establish connection with Database
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         port=3306,
                         db=sys.argv[3])
    # Get and Execute query
    cursor = db.cursor()
    query = """
        SELECT name
        FROM cities
        WHERE state_id = (
            SELECT id
            FROM states
            WHERE name = '{}')
        ORDER BY cities.id ASC
    """.format(argument[0].strip("\'\""))
    cursor.execute(query)

    # Print results
    rows = cursor.fetchall()
    if (rows):
        print(rows[0][0], end="")
        rows = rows[1:]
        for row in rows:
            print(f' ,{row[0]}', end="")
        print()

    # Close Connection
    cursor.close()
    db.close()
