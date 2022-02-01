#!/usr/bin/python3
'''
module for open and read a file given in name
'''


def read_file(filename=""):
    '''
    open and read a file given in parameter

    Parameter
    ---------
    filename : str
        the name of the file we want to open
    '''
    with open(filename) as fd:
        for line in fd:
            print("{}".format(line), end="")

    fd.close()
