#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length_list = len(my_list)
    list_result = []

    for loop in range(0, length_list):
        if my_list[loop] % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)

    return list_result
