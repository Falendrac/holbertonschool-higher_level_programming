#!/usr/bin/python3
"""The base of the module models"""


class Base():
    """
    Base of all class the module

    ...

    Attribute
    ---------
    __nb_objects : int
        number of objects base created without specific id
    id : int
        the id of the instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method, if id is none increment the object attribute nb_object
        and assign it to id. Otherwise, id is set in public attriubte

        ...

        Parameter
        ---------
        id : int
            can be None or int
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
