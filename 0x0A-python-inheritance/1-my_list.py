#!/usr/bin/python3
'''
File for the task 1, with the first class inherits of lists

...

Class
-----
My_list(list)
'''


class MyList(list):
    '''
    class MyList inherits of lists class

    ...
    Methods
    -------
    print_sorted(self)
        print list by sort
    '''
    def print_sorted(self):
        '''print a sorted list'''
        list_sorted = self.copy()
        list_sorted.sort()
        print(list_sorted)
