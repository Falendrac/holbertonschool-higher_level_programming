#!/usr/bin/python3
def max_integer(my_list=[]):
    length_list = len(my_list)

    if length_list == 0:
        return None
    else:
        max_list = my_list[0]
        for loop in range(0, length_list):
            if my_list[loop] > max_list:
                max_list = my_list[loop]

        return max_list
