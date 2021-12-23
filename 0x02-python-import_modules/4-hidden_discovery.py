#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    for nameinHidden in dir(hidden_4):
        if nameinHidden[0: 1] != '_':
            print("{}".format(nameinHidden))
