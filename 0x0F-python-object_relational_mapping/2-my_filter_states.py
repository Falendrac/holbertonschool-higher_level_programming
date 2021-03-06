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
        "SELECT * FROM states WHERE BINARY name = '%s' ORDER BY id"
        % sys.argv[4])

    result = cur.fetchall()
    for row in result:
        print("{}".format(row))

    cur.close()
    db.close()


if __name__ == "__main__":
    selectStates()
