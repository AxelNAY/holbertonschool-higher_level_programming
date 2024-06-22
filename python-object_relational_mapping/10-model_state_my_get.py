#!/usr/bin/python3
"""Script prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa.

Args:
    mysql_username: name of the mysql user.
    mysql_password: password of the mysql user.
    database_name: name of the mysql database.
    state_name: name of the state searched.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name).first()
    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()