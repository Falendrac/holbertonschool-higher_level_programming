#!/usr/bin/python3
for element in range(90, 64, -1):
    if element % 2 == 0:
        element += 32
    print("{:c}".format(element), end="")
