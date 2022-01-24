#!/usr/bin/python3


def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in range(len(matrix)):
        if len(matrix[row]) != len(matrix[len(matrix) - 1]):
            raise TypeError("Each row of the matrix must have the same size")

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not isinstance(matrix[row][col], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = list(map(list, matrix))

    for row in range(len(new_matrix)):
        for col in range(len(new_matrix[row])):
            new_matrix[row][col] = round((new_matrix[row][col] / div), 2)

    return new_matrix
