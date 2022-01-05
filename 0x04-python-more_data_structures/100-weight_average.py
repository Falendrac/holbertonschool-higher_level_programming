#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        summ = 0
        weight = 0
        for i in range(len(my_list)):
            summ += my_list[i][0] * my_list[i][1]
            weight += my_list[i][1]
        return summ / weight
    else:
        return 0
