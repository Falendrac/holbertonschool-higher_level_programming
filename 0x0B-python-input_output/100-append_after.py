#!/usr/bin/python3
'''
insert a new line in a txt file
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    insert a new_string in a txt file
    '''
    lines = []
    with open(filename, 'r+') as fd:
        for line in fd:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w') as fd:
        fd.writelines(lines)
