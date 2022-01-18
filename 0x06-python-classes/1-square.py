#!/usr/bin/python3
"""1-square.py:
    The second task for the first project with the POO in python.

    Here we define a square
"""


class Square:
    """
    square is aclass that defines a square

    ...

    Attributes
    ----------

    __size : int
        define the size of the square, that a private class attribute
    """
    def __init__(self, size):
        """
        Parameters
        ----------
        __size: int
            the size of the square
        """
        self.__size = size
