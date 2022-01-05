#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(len(new_matrix)):
        new_matrix[i] = matrix[i].copy()
        for y in range(len(new_matrix[i])):
            new_matrix[i][y] *= new_matrix[i][y]
    return new_matrix
