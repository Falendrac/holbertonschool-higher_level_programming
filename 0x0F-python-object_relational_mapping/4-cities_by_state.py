#!/usr/bin/python3

"""Script that select states starting with N in a MySQL db"""

import MySQLdb
import sys


def selectStates():
    """Connect to the DB, select states and print all states"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id"
        )

    for row in cur:
        print("{}".format(row))

    cur.close()
    db.close()


if __name__ == "__main__":
    selectStates()
