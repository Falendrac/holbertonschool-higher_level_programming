#!/usr/bin/python3
'''
Module for the class Square
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Define a square

    ...

    Attribute
    ---------
    size : int
        the size of the square

    Methods
    -------
    init(self, size)
        init the square

    area(self)
        return the area of the square

    str(self)
        return the definition of the square
    '''

    def __init__(self, size):
        '''
        init the instance square

        ...

        Parameters
        ----------
        size : int
            the size of the square
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''return the area of the square'''
        return self.__size ** 2

    def __str__(self):
        '''return the definition of the square'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
