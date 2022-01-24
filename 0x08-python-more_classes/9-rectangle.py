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
    number_of_instances : int
        the current number of instance of rectangle object
    print_symbol : any type
        the symbol that str prints
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
    area(self)
        return the area of the rectangle (height * width)
    perimeter(self)
        return the perimeter of the rectangle ( 2 * (height + width))
    bigger_or_equal(rect_1, rect_2)
        compare two rectangle and return the bigger
    """
    __height = None
    __width = None
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init methods for class Rectangle
        ...
        Parameters
        ----------
        width : int
            the width of the rectangle
        height : int
            the height of the rectangle
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter for width in class rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width in class rectangle
        ...
        Parameter
        ---------
        value : int
            the value of width we test and set
        Raises
        ------
        TypeError
            if value is not an int
        ValueError
            if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height in class rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height in class rectangle
        ...
        Parameter
        ---------
        value : int
            the value of height we test and set
        Raises
        ------
        TypeError
            if value is not an int
        ValueError
            if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        return the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        return the rectangle in format #
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            str = ""
            for loop in range(self.__height):
                str += format(self.print_symbol) * self.__width
                if loop != self.__height - 1:
                    str += "\n"
            return str

    def __repr__(self):
        """
        return the representation of the rectangle
        Example:
        return "Rectangle(2, 4)
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when an instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compare two object of type Rectangle
        return the bigger one
        ...
        Parameters
        ----------
        rect_1 : Rectangle
            the first rectangle to compare
        rect_2 : Rectangle
            the second rectangle to compare
        Raises
        ------
        TypeError
            If one variable is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        class method for create a new instance of a rectangle object
        """
        return Rectangle(size, size)
