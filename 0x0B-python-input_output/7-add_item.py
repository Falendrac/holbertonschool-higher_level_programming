#!/usr/bin/python3
'''
adds all arguments to a Python list, and then save them to a file
'''

from os.path import exists
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

if exists(filename):
    my_list = load_from_json_file(filename)
    for i in range(len(sys.argv)):
        if i > 0:
            my_list.append(sys.argv[i])
    save_to_json_file(my_list, filename)
else:
    save_to_json_file(sys.argv[1:], filename)
