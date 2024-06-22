#!/usr/bin/python3
"""
This script changes the name of the State object
with id = 2 to "New Mexico" in the database hbtn_0e_6_usa.

Arguments:
    username: name of the mysql user.
    password: password of the mysql user.
    database: name of the mysql database.

The script connects to a MySQL server running on localhost at port 3306.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) > 4 or ";" in sys.argv[3]:
        raise ValueError
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%')) \
        .all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()