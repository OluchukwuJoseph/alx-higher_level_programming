#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`
"""
import sys
import MySQLdb


# Get database credentials from Command Line Argruments
DB_USER = sys.argv[1]
DB_PASSWORD = sys.argv[2]
DB = sys.argv[3]

try:
    # Connect with Database
    with MySQLdb.connect(host='localhost',
                         user=DB_USER,
                         passwd=DB_PASSWORD,
                         db=DB, port=3306) as db:
        cursor = db.cursor()
        sql_query = 'SELECT * FROM states WHERE name LIKE "N%"'
        cursor.execute(sql_query)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as error:
    print(error)
