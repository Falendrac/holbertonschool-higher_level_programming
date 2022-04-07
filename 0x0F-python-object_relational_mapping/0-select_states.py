#!/usr/bin/python3

"""Script that select states in a MySQL db"""

import MySQLdb
import sys

def selectStates():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    for row in cur:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    selectStates()
