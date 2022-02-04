#!/usr/bin/python3
"""The base of the module models"""

import json


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

    Methods
    -------
    to_json_string(list_dictionaries)
        static method that return a json string representation
    save_to_file(cls, list_objs)
        class method to create a json file
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries[0]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        create a file with the name
        of the class and the json representation of this class
        """
        json_dict = ""
        for obj in list_objs:
            json_dict += obj.to_json_string([obj.to_dictionary()])
        filename = cls.__name__ + ".json"
        with open(filename, "w+") as fd:
            fd.write(json_dict)
