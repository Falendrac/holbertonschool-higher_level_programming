#!/usr/bin/python3
'''
module for append or create a new file with content
'''


def append_write(filename="", text=""):
    '''
    append or create a file with given text

    Parameters
    ----------
    filename : str
        the name of the file
    text : str
        the text added into the file
    '''
    with open(filename, 'a+') as fd:
        return fd.write(text)
