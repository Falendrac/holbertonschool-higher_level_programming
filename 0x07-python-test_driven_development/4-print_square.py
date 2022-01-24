#!/usr/bin/python3
"""
file that print a square

...

Methods
-------
print_square(size)
    print a square
"""


def print_square(size):
    """
    print a square

    ...

    Parameters
    ----------
    size : int
        the size of the square

    Raises
    ------
    TypeError
        if size is not an integer

    ValueError
        if size is less than 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for loop in range(size):
        print("#" * size)
