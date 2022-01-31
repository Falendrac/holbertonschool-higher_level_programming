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
