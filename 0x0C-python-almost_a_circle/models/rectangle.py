#!/usr/bin/python3
"""Models for a Rectangle object"""

from models.base import Base


class Rectangle(Base):
    """
    Define a rectangle with inheritance of Base class

    ...

    Attributes
    ----------
    width : int
        the width of the rectangle
    height : int
        the height of the rectangle
    x : int
        pos x
    y : int
        pos y
    id : int
        id of the istance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method for rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width"""
        self.__width = width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        self.__y = y
