#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length_list = len(my_list)

    if idx < 0 or idx >= length_list:
        return None
    else:
        my_list[idx] = element
        return my_list
