#!/usr/bin/python3

"""print the first element of a database"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (MetaData, create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        resultCity = session.query(State).order_by(State.id)

        for rowState in resultCity:
            print("{}: {}".format(rowState.id, rowState.name))
            for rowCity in rowState.cities:
                print(
                    "\t{}: {}".format(rowCity.id, rowCity.name)
                    )
