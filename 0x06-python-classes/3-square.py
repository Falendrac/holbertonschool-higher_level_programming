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

    Methods
    -------
    area(self)
        return the current square area
    """

    def __init__(self, size=0):
        """
        Parameters
        ----------
        __size: int
            the size of the square

        Raises
        ------
        Typerror
            If size is not an integer
        ValueError:
            If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the value of the current square area"""
        return self.__size * self.__size
