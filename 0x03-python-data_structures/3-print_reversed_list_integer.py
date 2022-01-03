#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length_list = len(my_list)
    for loop in reversed(my_list):
        print("{:d}".format(loop))
