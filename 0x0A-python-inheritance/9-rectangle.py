#!/usr/bin/python3
'''
Task 8 for Rectangle class

import
------
BaseGeometry class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Define a Rectangle

    Attribute
    ---------
    width : int
        the width of the rectangle
    height : int
        the height of the rectangle

    Methods
    -------
    init(self, width, height)
        the init methods for class Rectangle
    area(self)
        return the area of the rectangle
    str(self)
        return the rectangle definition
    '''

    def __init__(self, width, height):
        '''
        Init method

        Parameters
        ----------
        width : int
            the width of the rectangle
        height : int
            the height of the rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Return the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Return the definition of the rectangle'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
