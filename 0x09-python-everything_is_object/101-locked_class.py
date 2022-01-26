#!/usr/bin/python3
"""
Second avanced task securise a class
to prevent the user from dynamically creating new instance attributes
"""


class LockedClass:
    """
    An empty class with a protect attribute slots
    that autorize only one dynamic attribute
    """
    __slots__ = ['first_name']
