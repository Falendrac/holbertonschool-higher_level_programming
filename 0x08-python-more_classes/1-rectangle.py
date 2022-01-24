#!/usr/bin/python3
"""
File for the class rectangle.

That define a rectangle.
"""


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
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
