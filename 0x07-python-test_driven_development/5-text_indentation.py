#!/usr/bin/python3
"""
The fifth task of project driven test

...

Methods
-------

text_indentation(text)
    add a new line when we have a special character and print
"""


def text_indentation(text):
    """
    print the text and adding a new line when "?.:" is present

    ...

    Parameters
    ----------

    text : string
        The text to print
    """
    inspecial = False

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for loop in range(len(text)):
        if text[loop] in "?.:":
            print("{}".format(text[loop]))
            inspecial = True
        elif inspecial and text[loop] == ' ':
            pass
        else:
            print("{}".format(text[loop]), end="")
