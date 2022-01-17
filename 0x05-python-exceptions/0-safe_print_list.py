#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for elem in my_list[:x]:
        try:
            print("{}".format(elem), end="")
            count += 1
        except ValueError:
            break
    print("")
    return count
