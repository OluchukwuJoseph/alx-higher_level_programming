#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`
"""
import sys
import MySQLdb


if __name__ == '__main__':
    # Get database credentials from Command Line Argruments
    DB_USER = sys.argv[1]
    DB_PASSWORD = sys.argv[2]
    DB = sys.argv[3]

    # Connect with Database
    db = MySQLdb.connect(host='localhost',
                         user=DB_USER,
                         passwd=DB_PASSWORD,
                         port=3306,
                         db=DB)
    cursor = db.cursor()
    query = """
        SELECT *
        FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close Connection
    cursor.close()
    db.close()
