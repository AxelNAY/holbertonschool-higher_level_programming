#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.

Args:
    mysql_username: name of the mysql user.
    mysql_password: password of the mysql user.
    database_name: name of the mysql database.
    state_name: name of the state searched.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host = "localhost",
        user = username,
        pwd = password,
        db_name = database_name,
        port = 3306
    )

    cursor = db.cursor()
    select = cursor.execute("SELECT * FROM states WHERE name = state_name")
    cursor.execute(select)
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()