#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

Args:
    username: name of the mysql user.
    password: password of the mysql user.
    database_name: name of the mysql database.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
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
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()