#!/usr/bin/python3
"""4-square.py:
    The Fifth task for the first project with the POO in python.

    Here we define a square
"""


class Square:
    """
    square is a class that defines a square

    ...

    Attributes
    ----------

    __size : int
        define the size of the square, that a private class attribute

    size : int
        the size of the square

    Methods
    -------
    size(self)
        that the getter of the class

    size(self, value)
        that the setter of the class

    area(self)
        return the current square area
    """

    def __init__(self, size=0):
        """
        Parameters
        ----------
        size: int
            the size of the square
        """
        self.size = size

    @property
    def size(self):
        """The getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter of size

        Parameters
        ----------
        value: int
            the size of the square

        Raises
        ------
        Typerror
            If size is not an integer
        ValueError:
            If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the value of the current square area"""
        return self.__size * self.__size

    def __eq__(self, other):
        """
        eq - Compare two square object if is it equal

        ...

        Parameter
        ---------
        other : Square
            the other object we compare
        """
        if isinstance(other, Square):
            return self.__size == other.size
        else:
            return False

    def __lt__(self, other):
        """
        lt - Compare two square object if is lower than

        ...

        Parameter
        ---------
        other : Square
            the other object we compare
        """
        if isinstance(other, Square):
            return self.__size < other.size
        else:
            return False

    def __le__(self, other):
        """
        le - Compare two square object if is lower or equal

        ...

        Parameter
        ---------
        other : Square
            the other object we compare
        """
        if isinstance(other, Square):
            return self.__size <= other.size
        else:
            return False

    def __gt__(self, other):
        """
        gt - Compare two square object if is grander than

        ...

        Parameter
        ---------
        other : Square
            the other object we compare
        """
        if isinstance(other, Square):
            return self.__size > other.size
        else:
            return False

    def __ge__(self, other):
        """
        ge - Compare two square object if is grander or equal

        ...

        Parameter
        ---------
        other : Square
            the other object we compare
        """
        if isinstance(other, Square):
            return self.__size >= other.size
        else:
            return False
