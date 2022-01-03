#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length_list = len(my_list)
    for loop in range(-1, -length_list - 1, -1):
        print("{}".format(my_list[loop]))
