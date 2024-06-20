#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.

Args:
    mysql_username: name of the mysql user.
    mysql_password: password of the mysql user.
    database_name: name of the mysql database.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host = "localhost",
        user = username,
        pwd = password,
        db_name = database_name,
        port = 3306
    )
        
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    if states:
        for state in states:
            print(state)
    else:
        print("Error: Data not found.")

    cursor.close()
    db.close()