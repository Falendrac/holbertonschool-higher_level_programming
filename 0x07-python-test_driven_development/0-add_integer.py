#!/usr/bin/python3
"""
This is the first task for the project 0x07 python

...

Methods
-------
add_integer(a, b=98)
    return the addition of two integer and/or float

Example for the function add_integer:

>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b

    ...

    Parameters
    ----------
    a : int/float
        first parameters to do addition
    b : int/float
        first parameters to do addition
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a + b)
