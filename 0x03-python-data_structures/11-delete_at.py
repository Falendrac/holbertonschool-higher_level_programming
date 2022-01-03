#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length_list = len(my_list)

    if idx < 0 or idx >= length_list:
        return my_list
    else:
        my_list[idx:idx + 1] = []
        return my_list
