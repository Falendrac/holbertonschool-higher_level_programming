#!/usr/bin/python3
'''
Task 4 to see if an instance is type of subclass
'''


def inherits_from(obj, a_class):
    '''return true if obj is a subclass of a_class, otherwise return false'''
    return issubclass(type(obj), a_class) and not type(obj) is a_class
