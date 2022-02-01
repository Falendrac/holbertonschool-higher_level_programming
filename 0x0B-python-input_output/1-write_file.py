#!/usr/bin/python3
'''
module for write or create a new file with content
'''


def write_file(filename="", text=""):
    '''
    write or create a file with given text

    Parameters
    ----------
    filename : str
        the name of the file
    text : str
        the text added into the file
    '''
    with open(filename, 'w+') as fd:
        return fd.write(text)
