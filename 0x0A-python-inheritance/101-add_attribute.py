#!/usr/bin/python3
'''
module for the last advanced of the project
adding a new attribute in an object
'''


def add_attribute(obj, notname, value):
    '''
    Add a new attribute in obj

    Parameters
    ----------
    obj : obj
        the obj we add a new attribute
    notname : string
        the name of the attribute
    value : string
        the value of the new attribute

    Raise
    -----
    TypeError
        if the obj is protected
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, notname, value)
