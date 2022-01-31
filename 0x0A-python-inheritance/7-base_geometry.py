#!/usr/bin/python3
'''
File of the class BaseGeometry

That define the base of the Geometry
'''


class BaseGeometry():
    '''
    Define the base of the Geometry

    ...

    Attributes
    ----------

    Methods
    -------
    area(self)
        calculate the area

    integer_validator(self, name, value)
        validates value
    '''
    def area(self):
        '''
        Calculate the area

        ...

        Raises
        ------
        Exception
            not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Validate a value associate with a name

        ...

        Parameters
        ----------
        name : string
            The name of the value
        value : int
            the value we validate

        Raises
        ------
        TypeError
            if value is not an integer
        ValueError
            if value is less or equal at 0
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
