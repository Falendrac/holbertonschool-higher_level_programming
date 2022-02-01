#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as fd:
        for line in fd:
            print("{}".format(line), end="")
