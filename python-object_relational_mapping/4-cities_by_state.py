#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.

Args :
    username (str) : name of the mysql user.
    password (str) : password of the mysql user.
    database (str) : name of the mysql database.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) > 4 or ";" in sys.argv[3]:
        raise ValueError
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database,
                         port=3306)

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities,
                 states WHERE states.id = cities.state_id
                 ORDER BY cities.id ASC""")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()