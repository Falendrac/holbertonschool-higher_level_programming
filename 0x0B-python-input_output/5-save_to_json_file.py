#!/usr/bin/python3
'''
Third task for json, we generate a json file
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    writes an Object to a text file, using a JSON representation
    '''
    with open(filename, 'w+') as fd:
        fd.write(json.dumps(my_obj))
