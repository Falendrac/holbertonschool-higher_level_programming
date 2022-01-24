#!/usr/bin/python3
"""
File for the class rectangle.

That define a rectangle.
"""


from turtle import width


class Rectangle:
    """
    Define a Rectangle

    ...

    Attributes
    ----------

    __width : int
        the width of the rectangle

    __height : int
        the height of the rectangle

    Methods
    -------

    width(self)
        the getter of width

    width(self, value)
        the setter of width

    height(self)
        the getter of height

    height(self, value)
        the setter of height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise TypeError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def haight(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
