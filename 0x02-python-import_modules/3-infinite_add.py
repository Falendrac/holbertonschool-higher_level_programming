#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    length = len(sys.argv)
    addall = 0
    if length == 1:
        print("{}".format(addall))
    else:
        for loop in range(1, length):
            addall += int(sys.argv[loop])
        print("{}".format(addall))
