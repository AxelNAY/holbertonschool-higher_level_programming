#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!

Args:
    username: name of the mysql user.
    password: password of the mysql user.
    database: name of the mysql database.
    state_name: name of the state searched.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = username,
        pwd = password,
        db_name = database
    )

    cursor = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()