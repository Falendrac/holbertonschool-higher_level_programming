#!/usr/bin/python3
'''
module for the class student
'''


class Student():
    '''
    define a studen

    Attributes
    ----------
    first_name
        the first name of student
    last_name
        the last name of student
    age
        the age of student

    Methods
    -------
    to_json(self)
        return a dictionary representation of a Student instance
    '''

    def __init__(self, first_name, last_name, age):
        '''Init method for student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''return a dictionary representation of a Student instance'''
        return vars(self)
