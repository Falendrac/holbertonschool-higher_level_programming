#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    summary = 0
    for element in my_list:
        if element not in uniq_list:
            uniq_list.append(element)
            summary += element
    return summary
