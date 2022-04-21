#!/usr/bin/python3
'''
Technical interview
'''


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers'''
    size = len(list_of_integers)
    if size == 0:
        return None
    else:
        return max(list_of_integers)
