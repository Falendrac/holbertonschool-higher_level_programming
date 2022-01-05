#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_copy = a_dictionary.copy()
    for i, v in sorted(dict_copy.items()):
        print("{:s}: {}".format(i, v))
