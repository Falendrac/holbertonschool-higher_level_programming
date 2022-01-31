#!/usr/bin/python3
'''
file with only one method with the task 0

...

Method
------
lookup(obj)
    return a list of valid attributes of a class
'''


def lookup(obj):
    '''Return a list of valod attributes of a class obj.'''
    return dir(obj)
