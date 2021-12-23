#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1
    import sys

    length = len(sys.argv)
    op = ['*', '+', '-', '/']
    argv = sys.argv

    def symbol():
        if any(c in sys.argv[2] for c in op):
            return True
        else:
            return False

    def operate():
        argop = argv[2]
        if argop == '*':
            return calculator_1.mul(int(argv[1]), int(argv[3]))
        elif argop == '/':
            return calculator_1.div(int(argv[1]), int(argv[3]))
        elif argop == '+':
            return calculator_1.add(int(argv[1]), int(argv[3]))
        elif argop == '-':
            return calculator_1.sub(int(argv[1]), int(argv[3]))

    if length < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif len(argv[2]) != 1 or not symbol():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], operate()))
