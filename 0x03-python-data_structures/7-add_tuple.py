#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = test_tuple(tuple_a)
    tuple_b = test_tuple(tuple_b)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple


def test_tuple(tuple_test=()):
    length_tuple = len(tuple_test)
    if length_tuple < 2 and length_tuple == 1:
        return (tuple_test[0], 0)
    elif length_tuple < 2 and length_tuple == 0:
        return (0, 0)

    return tuple_test
