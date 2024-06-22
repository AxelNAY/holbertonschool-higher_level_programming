#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of the database hbtn_0e_0_usa where the name matches the argument.

Args:
    username (str): name of the mysql user.
    password (str): password of the mysql user.
    database (str): name of the mysql database.
    state_name (str): name of the state searched.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()