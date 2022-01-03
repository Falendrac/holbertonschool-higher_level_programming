#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length_list = len(my_list)
    for loop in range(0, length_list):
        print("{:d}".format(my_list[loop]))
