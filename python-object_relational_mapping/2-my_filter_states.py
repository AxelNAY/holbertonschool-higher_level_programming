#!/usr/bin/python3
"""
Script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Args:
    username: name of the mysql user.
    password: password of the mysql user.
    database_name: name of the mysql database.
    state_name: name of the state searched.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = username,
        pwd = password,
        db_name = database_name
    )

    cursor = db.cursor()
    select = """SELECT * FROM states WHERE BINARY
            name = '{}' ORDER BY id ASC""".format(state_name)
    cursor.execute(select)
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()