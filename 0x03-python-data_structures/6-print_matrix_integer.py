#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for loop1 in range(0, len(matrix)):
        length_list_x = len(matrix[loop1])
        if length_list_x != 0:
            for loop2 in range(0, length_list_x):
                print("{:d}".format(matrix[loop1][loop2]), end=" ")
        print()
