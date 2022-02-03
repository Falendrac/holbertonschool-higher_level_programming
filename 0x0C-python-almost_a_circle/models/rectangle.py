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
        """setter for width

        ...

        Raises
        ------
        TypeError
            if the parameter is not an int
        ValueError
            if the parameter is less or equal to 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height

        ...

        Raises
        ------
        TypeError
            if the parameter is not an int
        ValueError
            if the parameter is less or equal to 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x

        ...

        Raises
        ------
        TypeError
            if the parameter is not an int
        ValueError
            if the parameter is less to 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y

        ...

        Raises
        ------
        TypeError
            if the parameter is not an int
        ValueError
            if the parameter is less to 0
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle with # character"""
        for row in range(self.__height + self.__y):
            if row < self.__y:
                print()
            else:
                print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """return the string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
            )

    def update(self, *args, **kwargs):
        """update attribute with value in args"""
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            get = 0
            for val in args:
                if get == 0:
                    self.id = val
                elif get == 1:
                    self.width = val
                elif get == 2:
                    self.height = val
                elif get == 3:
                    self.x = val
                elif get == 4:
                    self.y = val
                get += 1
