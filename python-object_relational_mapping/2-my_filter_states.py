#!/usr/bin/python3
"""
Script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Args:
    username: name of the mysql user.
    password: password of the mysql user.
    database: name of the mysql database.
    state_name: name of the state searched.

The script connects to a MySQL server running on localhost at port 3306
and fetches all rows in the `states` table with the name matching the argument,
sorted in ascending order by `id`.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
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
    query = """SELECT * FROM states WHERE
    BINARY name = '{}' ORDER BY id ASC""".format(
        state_name)
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()