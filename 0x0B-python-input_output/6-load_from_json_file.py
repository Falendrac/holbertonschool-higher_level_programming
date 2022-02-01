#!/usr/bin/python3
'''
Fourth task for json
'''

import json


def load_from_json_file(filename):
    '''
    creates an Object from a “JSON file”
    '''
    with open(filename) as fd:
        return json.loads(fd.read())
