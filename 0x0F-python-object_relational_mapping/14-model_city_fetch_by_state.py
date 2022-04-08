#!/usr/bin/python3

"""print the first element of a database"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (MetaData, create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        resultCity = session.query(City, State).filter(State.id == City.state_id).all()

        for rowCity, rowState in resultCity:
            print("{}: ({}) {}".format(rowState.name, rowCity.id, rowCity.name))
