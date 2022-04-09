#!/usr/bin/python3

"""print the first element of a database"""

import sys
from model_state import Base, State
from sqlalchemy import (MetaData, create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        result = session.query(State)

        if result.count() == 0:
            print("Nothing")
        else:
            result = session.query(State).first()
            print("{}: {}".format(result.id, result.name))
