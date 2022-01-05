#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        keys = [k for k, v in a_dictionary.items() if v == value]
        for i in keys:
            del a_dictionary[i]
    return a_dictionary
