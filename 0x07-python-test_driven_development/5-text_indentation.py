#!/usr/bin/python3


from re import L


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for loop in range(len(text)):
        if text[loop] in "?.:":
            print("{}".format(text[loop], end="\n\n"))
        elif text[loop - 1] not in "?.:":
            print("{}".format(text[loop]), end="")
