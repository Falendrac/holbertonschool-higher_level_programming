#!/usr/bin/python3
'''generate a dictionnary for JSON'''


def class_to_json(obj):
    '''
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object'''
    return vars(obj)
