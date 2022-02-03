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
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """return the string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
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
                    self.size = val
                elif get == 2:
                    self.x = val
                elif get == 3:
                    self.y = val
                get += 1

    def to_dictionary(self):
        """return the the dictionnary representation of Rectangle"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
