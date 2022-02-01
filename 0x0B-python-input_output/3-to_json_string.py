#!/usr/bin/python3
'''
Starting with json manipulation
'''

import json


def to_json_string(my_obj):
    '''
    returns the JSON representation of an object (string)

    Parameter
    ---------
    my_obj
    '''
    return json.dumps(my_obj)
