#!/usr/bin/python3
"""
103-magic_class
---------------

This task is a retranscription of Bytecode into python
"""
import math


class MagicClass:
    """
    MagicClass - This is the Magic class produce with Bytecode

    ...

    Attributes
    ----------
    _MagiClass__radis : int or float
        The radius of magicclass

    Methods
    -------
    area(self)
        The area of the magic class
    circumference(self)
        The circumference of the magic class
    """
    def __init__(self, radius=0):
        """
        Parameters
        ----------
        radius : int or float
            radius define the magicclass
        """
        self._MagicClass__radius = 0

        if type(radius) is not int and type(radius) is not int:
            raise TypeError('radius must be a number')
        else:
            self._MagicClass__radius = radius

    def area(self):
        """
        area - define an area
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """
        circumference - define the circumference
        """
        return 2 * math.pi * self._MagicClass__radius
