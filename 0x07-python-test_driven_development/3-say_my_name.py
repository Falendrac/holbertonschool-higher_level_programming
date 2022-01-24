#!/usr/bin/python3
"""
3-say_my_name - Task 3 with 1 method

...

Methods
-------

say_my_name(first_name, last_name)
    print who you are
"""


def say_my_name(first_name, last_name=""):
    """
    print who you are

    ...

    Parameters
    ----------
    first_name : str
        your first_name
    last_name : str
        your last_name

    Raises
    ------
    TypeError
        if first_name or last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
