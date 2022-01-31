#!/usr/bin/python3
'''
Module of the rebel MyInt
Reverse equal and not equal
'''


class MyInt(int):
    '''
    MyInt class is a rebel

    ...

    Methods
    -------
    eq(self, other)
        reverse the equal operator

    ne(self, other)
        reverse the not equal operator
    '''

    def __eq__(self, other):
        '''reversed equal'''
        if issubclass(type(self), type(other)):
            return self.__index__() != self.__index__()
        else:
            return False

    def __ne__(self, other):
        '''reversed not equal'''
        if issubclass(type(self), type(other)):
            return self.__index__() == self.__index__()
        else:
            return False
