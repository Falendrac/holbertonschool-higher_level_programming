#!/usr/bin/python3
for ten in range(0, 9):
    for unity in range(ten + 1, 10):
        if ten < 8:
            print("{0}{1}, ".format(ten, unity), end="")
        else:
            print("{0}{1}".format(ten, unity))
