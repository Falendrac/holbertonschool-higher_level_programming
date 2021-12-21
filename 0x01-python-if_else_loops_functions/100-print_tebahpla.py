#!/usr/bin/python3
i = 25
dif = 0
for element in range(65, 91):
    if element % 2 != 0:
        dif = 32
    print(chr(element + i + dif), end="")
    i -= 2
    dif = 0
