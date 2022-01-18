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

    my_print(self)
        print in stdout the square with the character #
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

    def my_print(self):
        """
        my_print - Print the square with the character #
        """
        for loopw in range(0, self.__size):
            for looph in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
