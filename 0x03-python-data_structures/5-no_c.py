#!/usr/bin/python3
def no_c(my_string):
    length_string = len(my_string)
    new_str = ''

    for loop in range(0, length_string):
        if my_string[loop] != 'C' and my_string[loop] != 'c':
            new_str += my_string[loop]

    return new_str
