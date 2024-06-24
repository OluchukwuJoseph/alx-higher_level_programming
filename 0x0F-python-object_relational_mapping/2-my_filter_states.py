#!/usr/bin/python3
"""
    This script takes in an argument and displays all values in the `states`
    table where `name` matches the argument.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    # Retrieve Command line Arguments
    argument = sys.argv[4]

    # Establish database connection
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    # Get and Execute query
    cursor = db.cursor()
    query = """
        SELECT *
        FROM states
        WHERE name = '{}'
        ORDER BY id ASC
    """.format(argument)

    cursor.execute(query)

    # Get and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close Connection
    cursor.close()
    db.close()
