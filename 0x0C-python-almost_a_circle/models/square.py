#!/usr/bin/python3
"""Models for a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Define a Square with inheritance of Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """init method for square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )
