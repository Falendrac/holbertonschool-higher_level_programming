#!/usr/bin/python3
'''
Pascal triangle problem need to be resolved
'''


def pascal_triangle(n):
    '''
    create an pascal triangle of n size
    '''
    pascal = []

    if n > 0:
        for row in range(n):
            if row == 0:
                pascal.append([1])
            else:
                listRow = []
                for i in range(row + 1):
                    if i == 0:
                        listRow.append(1)
                    elif i == row:
                        listRow.append(1)
                    else:
                        listRow.append(pascal[row-1][i-1] + pascal[row-1][i])
                pascal.append(listRow)

    return pascal
