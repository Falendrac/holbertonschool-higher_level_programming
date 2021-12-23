#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        length = len(sys.argv)
        print("{} argument:".format(length - 1))
        for loop in range(1, length):
            print("{}: {}".format(loop, sys.argv[loop]))
